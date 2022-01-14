#!/bin/bash

shopt -s extglob

for version in ./services/*!(protos)/version; do
    semver="$(head -n 1 $version)"
    working_dir="$(dirname $version)"
    service_name="$(basename $working_dir)"
    image_tag="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$GCP_ARTIFACT_REPO_NAME/$service_name:$semver"
    
    gcloud_output="$(gcloud artifacts docker images describe $image_tag)"

    if [[ !$? -eq 0 ]]; then
        echo "Uploading new image for $service_name at version $semver with tag $image_tag"
        (cd "$working_dir"; make docker-build-ci tag="$image_tag")
        docker push "$image_tag"
    else
        echo "Image for $service_name at version $semver exists"
    fi
done