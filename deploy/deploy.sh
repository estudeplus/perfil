
#!/bin/bash

echo "Setting up GCLOUD auth\n"
gcloud auth activate-service-account --key-file ${TRAVIS_BUILD_DIR}/deploy/gcloud-key.json

gcloud --quiet config set project $PROJECT_ID
gcloud --quiet config set container/cluster $CLUSTER 
gcloud --quiet config set compute/zone $ZONE 

echo "Getting cluster credentials\n"
gcloud --quiet container clusters get-credentials $CLUSTER

echo "Authenticating on DockerHub\n"
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin


echo "Pushing new image\n"
docker push ${ORG_NAME}/${IMAGE_NAME}:$TRAVIS_COMMIT

echo "Setting new image on deployment\n"
kubectl set image deployment/${DEPLOYMENT} ${CONTAINER}=${ORG_NAME}/${IMAGE_NAME}:$TRAVIS_COMMIT
