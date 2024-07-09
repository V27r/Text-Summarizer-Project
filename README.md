# End-to-End Text Summarizer Project

## Workflows

1. Update `config/config.yaml`
2. Update `params.yaml`
3. Update entities
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`
8. Update `app.py`

## How to Run?

### Steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/V27r/Text-Summarizer-Project
   ```

2. Create a conda environment after opening the repository:

   ```bash
   conda create -n summary python=3.11 -y
   conda activate summary
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Finally, run the following command:

   ```bash
   python app.py
   ```

5. Open this link in your browser: [http://localhost:8080/](http://localhost:8080/)

### Author Information:

- **Author**: Mahaveer
- **Role**: Data Scientist
- **Email**: [mahaveerr2703@gmail.com](mailto:mahaveerr2703@gmail.com)
- **Credits**: [Boktiar Ahmed Bappy](https://www.youtube.com/watch?v=p7V4Aa7qEpw)

# AWS CI/CD Deployment with GitHub Actions

## Steps:

1. **Login to AWS Console**.

2. **Create IAM User for Deployment** with specific access:

   - **EC2 Access**: Virtual machine
   - **ECR**: Elastic Container Registry to save your Docker image in AWS

   **Enable these policies**:

   - `AmazonEC2ContainerRegistryFullAccess`
   - `AmazonEC2FullAccess`

3. **Create ECR Repository** to store/save Docker image:

   - Save the URI: `975050007284.dkr.ecr.eu-north-1.amazonaws.com/text-s`

4. **Create EC2 Machine** (Ubuntu):

   - Open EC2 and install Docker on the EC2 machine by running the following commands one by one:

     ```bash
     sudo apt-get update -y
     sudo apt-get upgrade
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

5. **Configure EC2 as a Self-Hosted Runner**:

   - Go to GitHub `Settings > Actions > Runners > New Self-Hosted Runner`
   - Choose the OS and run the commands provided one by one

6. **Set Up GitHub Secrets**:

   - `AWS_ACCESS_KEY_ID`= 128379asjhd1290
   - `AWS_SECRET_ACCESS_KEY`= ajshd891246-29014sahjk
   - `AWS_REGION` = us-east-1
   - `AWS_ECR_LOGIN_URI` = `566373416292.dkr.ecr.ap-south-1.amazonaws.com`
   - `ECR_REPOSITORY_NAME` = simple-app

## Deployment Description:

1. Build the Docker image of the source code.
2. Push your Docker image to ECR.
3. Launch your EC2 instance.
4. Pull your image from ECR in EC2.
5. Launch your Docker image in EC2.

By following these steps, you can deploy your Text Summarizer Project using AWS and GitHub Actions for CI/CD.
