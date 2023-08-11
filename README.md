# First Step in End to End Machine learning 


## Architecture Diagram
![image](https://github.com/ketangangal/ml_bootcamp_workshop/assets/40850370/a644d17a-c035-4133-96f1-111e201a5fad)


## Docker
![image](https://github.com/ketangangal/ml_bootcamp_workshop/assets/40850370/06a836d2-c027-48e0-89fe-6c9bb8132847)


## CICD
🔧 **CI/CD pipeline using GitHub Actions**

- Triggered on push to main, excluding README.md.
- Two jobs: integration and build-push-package.

1. **integration:**
- Matrix: Python 3.9, 3.10, 3.11.
- Setup Python, install deps.
- Lint code using ruff.

2. **build-push-package:**
- Depends on integration.
- Build Docker image, push to Docker Hub.
