pip install --user awscli
export PATH=$PATH:$HOME/.local/bin

docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PASSWORD

docker build -t retrieval-system .
docker tag retrieval-system $IMAGE_REPO_URL
docker push $IMAGE_REPO_URL:latest

aws configure set aws_access_key_id $AWS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set default.region us-east-2

aws ecs update-service --cluster main --service retrieval-system --force-new-deployment
