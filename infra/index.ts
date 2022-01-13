import * as gcp from '@pulumi/gcp'
import * as pulumi from '@pulumi/pulumi'

const gcpConfig = new pulumi.Config('gcp')

const {
  GCP_ARTIFACT_REPO_NAME: artifactRepoName,
  GCP_K8S_CLUSTER_NAME: clusterName,
  GCP_K8S_PROXY_NAME: k8sProxyName,
  GCP_K8S_PROXY_PORT: k8sProxyPort,
} = process.env

const network = new gcp.compute.Network('speiss-vpc', { autoCreateSubnetworks: false })

const subnet = new gcp.compute.Subnetwork('speiss-subnet', {
  network: network.name,
  ipCidrRange: '10.142.0.0/20',
})

const router = new gcp.compute.Router('speiss-router', { network: network.name }, { dependsOn: [network] })

new gcp.compute.RouterNat(
  'speiss-nat',
  {
    natIpAllocateOption: 'AUTO_ONLY',
    router: router.name,
    sourceSubnetworkIpRangesToNat: 'ALL_SUBNETWORKS_ALL_IP_RANGES',
  },
  { dependsOn: [router] }
)

const staticIp = new gcp.compute.Address(`${k8sProxyName}-static-ip`, {})

new gcp.compute.Instance(
  k8sProxyName!,
  {
    name: k8sProxyName,
    machineType: 'e2-micro',
    bootDisk: {
      initializeParams: { image: 'debian-cloud/debian-9' },
    },
    metadataStartupScript: `
      #! /bin/bash
      apt-get update
      apt-get install -y tinyproxy
      grep -qxF 'Allow localhost' /etc/tinyproxy/tinyproxy.conf || echo 'Allow localhost' >> /etc/tinyproxy/tinyproxy.conf
      sudo sed -i 's/8888/${k8sProxyPort}/g' /etc/tinyproxy/tinyproxy.conf
      service tinyproxy restart`,
    networkInterfaces: [
      {
        accessConfigs: [{ natIp: staticIp.address }],
        network: network.name,
        subnetwork: subnet.name,
      },
    ],
    tags: [k8sProxyName!],
  },
  { dependsOn: [network, staticIp, subnet] }
)

new gcp.compute.Firewall(
  `${k8sProxyName}-ssh-rule`,
  {
    direction: 'INGRESS',
    network: network.name,
    allows: [{ ports: ['22'], protocol: 'tcp' }],
    targetTags: [k8sProxyName!],
  },
  { dependsOn: [network] }
)

new gcp.container.Cluster(
  clusterName!,
  {
    name: clusterName,
    enableAutopilot: true,
    masterAuthorizedNetworksConfig: {
      cidrBlocks: [{ cidrBlock: subnet.ipCidrRange }],
    },
    location: gcpConfig.get('region'),
    network: network.name,
    subnetwork: subnet.name,
    privateClusterConfig: {
      enablePrivateEndpoint: true,
      enablePrivateNodes: true,
      masterIpv4CidrBlock: '172.16.0.0/28',
    },
  },
  { ignoreChanges: ['verticalPodAutoscaling'], dependsOn: [network, subnet] }
)

new gcp.artifactregistry.Repository(artifactRepoName!, {
  format: 'DOCKER',
  location: gcpConfig.get('region'),
  repositoryId: artifactRepoName!,
})
