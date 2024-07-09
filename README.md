# End-to-End Text Summarizer Project

## Workflows

1. **Update `config/config.yaml`**:

   - Modify the project's configuration settings as needed.

2. **Update `params.yaml`**:

   - Adjust the parameters, such as hyperparameters and settings.

3. **Update entities**:

   - Define and update core data structures and components.

4. **Update the configuration manager in `src/config`**:

   - Ensure the configuration management code correctly applies settings.

5. **Update the components**:

   - Implement and update project modules like data processing and models.

6. **Update the pipeline**:

   - Set up the sequence of steps for data processing and model training.

7. **Update `main.py`**:

   - Modify the main script for loading data, initializing models, and running the pipeline.

8. **Update `app.py`**:
   - Update the web application code for serving the project.

## How to Run?

### Steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/V27r/Text-Summarizer-Project
   ```

2. **Create a conda environment**:

   ```bash
   conda create -n summary python=3.11 -y
   conda activate summary
   ```

3. **Install the requirements**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Open the link in your browser**:

   [http://localhost:8080/](http://localhost:8080/)

### Author Information:

- **Author**: Mahaveer
- **Role**: Data Scientist
- **Email**: [mahaveerr2703@gmail.com](mailto:mahaveerr2703@gmail.com)
- **Credits**: [Boktiar Ahmed Bappy](https://www.youtube.com/watch?v=p7V4Aa7qEpw)

# AWS CI/CD Deployment with GitHub Actions

## Steps:

1. **Login to AWS Console**:

   - Log in to the AWS Management Console.

2. **Create IAM User for Deployment**:

   - Create a user with `AmazonEC2ContainerRegistryFullAccess` and `AmazonEC2FullAccess` policies.
   - Save the access key ID and secret access key.

3. **Create ECR Repository**:

   - Open ECR and create a repository named `text-s`.
   - Save the repository URI.

4. **Create EC2 Machine (Ubuntu)**:

   - Launch an Ubuntu EC2 instance.
   - Connect via SSH and install Docker with the following commands:

     ```bash
     sudo apt-get update -y
     sudo apt-get upgrade
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

5. **Configure EC2 as a Self-Hosted Runner**:

   - Go to GitHub `Settings > Actions > Runners > New Self-Hosted Runner`.
   - Follow the provided commands to set up the runner on your EC2 instance.

6. **Set Up GitHub Secrets**:

   - In your GitHub repository, go to `Settings > Secrets and variables > Actions > New repository secret`.
   - Add the following secrets:

     - `AWS_ACCESS_KEY_ID` = your-aws-access-key-id
     - `AWS_SECRET_ACCESS_KEY` = your-aws-secret-access-key
     - `AWS_REGION` = your-aws-region
     - `AWS_ECR_LOGIN_URI` = your-ecr-login-uri
     - `ECR_REPOSITORY_NAME` = text-s

## Deployment Description:

1. **Build Docker Image**:

   - Use GitHub Actions to build the Docker image of your source code.

2. **Push Docker Image to ECR**:

   - Push the built image to your ECR repository.

3. **Launch EC2 Instance**:

   - Ensure your EC2 instance is running as a self-hosted runner.

4. **Pull Docker Image from ECR in EC2**:

   - Pull the Docker image from your ECR repository on the EC2 instance.

5. **Launch Docker Container in EC2**:
   - Run the Docker container on your EC2 instance using `docker run`.

By following these steps, you can deploy your Text Summarizer Project using AWS and GitHub Actions for CI/CD.
