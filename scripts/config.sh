## Docker install In ubuntu 22.04  lts
sudo apt-get update
sudo apt-get upgrade -y

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce -y
sudo systemctl status docker

# To install docker compose
sudo apt install docker-compose

# Add user into docker group
sudo usermod -aG docker ubuntu
newgrp docker

## Aws cli installation
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install

## Github Runner configuration
mkdir actions-runner && cd actions-runner
# Get config from runner page

## Important
./config.sh --url <url> --token <mention-you-token-here>
./run.sh

## Add Github runner as a service
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status

