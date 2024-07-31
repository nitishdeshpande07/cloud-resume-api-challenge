GCP Cloud Resume API Challenge
Project Overview:

This project demonstrates a Google Cloud Function (GCF) that fetches resume data from a Firestore database and returns it in JSON format. The project includes a CI/CD pipeline using GitHub Actions to automate the deployment process.

Key Components:

Google Cloud Function: Handles HTTP requests, fetches resume data from Firestore, and returns JSON response.
Firestore Database: Stores resume data.
GitHub Actions: Automates the deployment process.
Project Structure:

functions: Contains the main Python code for the Cloud Function.
requirements.txt: Lists project dependencies.
.github/workflows/deploy.yml: Defines the CI/CD pipeline.
Getting Started:

Clone the repository:
Bash
git clone https://github.com/your-username/your-repository-name.git


Install dependencies:
Bash
pip install -r requirements.txt


Set up environment variables:
Create GitHub secrets for GCP_PROJECT_ID, GCP_REGION, GA_SERVICE_ACCOUNT_KEY.
Deploy Cloud Function:
Push changes to the main branch to trigger the CI/CD pipeline.


The project uses a service account for authentication with GCP.
The Cloud Function is configured to handle HTTP requests.
The CI/CD pipeline automatically deploys the Cloud Function on code changes.

Please Note : 
The Current URL is for the GCP region : [ asia-south1 ] 
