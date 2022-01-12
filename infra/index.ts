import * as gcp from '@pulumi/gcp'

const { GCP_PROJECT_ID: project, GCP_REGION: region, GCP_ARTIFACT_REPO_NAME: artifactRepoName } = process.env

const network = new gcp.compute.Network('speiss-vpc', {
  autoCreateSubnetworks: true,
  project,
})

const router = new gcp.compute.Router(
  'speiss-router',
  {
    network: network.name,
    project,
    region,
  },
  { dependsOn: [network] }
)

new gcp.compute.RouterNat(
  'speiss-nat',
  {
    natIpAllocateOption: 'AUTO_ONLY',
    project,
    router: router.name,
    region: router.region,
    sourceSubnetworkIpRangesToNat: 'ALL_SUBNETWORKS_ALL_IP_RANGES',
  },
  { dependsOn: [router] }
)

new gcp.container.Cluster(
  'speiss-cluster',
  {
    enableAutopilot: true,
    location: region,
    masterAuthorizedNetworksConfig: {
      cidrBlocks: [],
    },
    network: network.selfLink,
    privateClusterConfig: {
      enablePrivateEndpoint: true,
      enablePrivateNodes: true,
      masterIpv4CidrBlock: '172.16.0.0/28',
    },
    project,
  },
  { ignoreChanges: ['verticalPodAutoscaling'], dependsOn: [network] }
)

new gcp.artifactregistry.Repository(artifactRepoName!, {
  format: 'DOCKER',
  location: region,
  project,
  repositoryId: artifactRepoName!,
})
