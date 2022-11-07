# BoB Techgig Hackathon

## Problem Statement:
Banks handle large volumes of cheques in the clearing process, leaving the system vulnerable to perpetrators, causing processing delays and human errors that are frequently misinterpreted as account holders' negligence. 

Cheque fraud is a type of criminal act that involves the illegal use of cheques to illegally acquire or borrow funds that do not exist within the account balance or legal ownership of the account-holder. The Reserve Bank of India (RBI) has directed banks to implement a system known as Positive Pay beginning in January 2021 in order to reduce cheque-related fraud. 

The proposed idea focuses on automatic cheque processing, which adds an extra layer of security to positive pay by automating the process of bank cheque leaf verification and fraud detection.

## Challenges and Target User segment:
With PPS, RBI is augmenting customer safety in high value cheque payments and reduce the fraud occurrences on account of tempering cheque leaves.
This proposal targets PPS transactions 
Current and target check clearing transaction distribution

## Current Cheque Clearning Workflow:
Cheque clearing cycle has been a manual  process to till date resulting in delayed transactions, Frauds and customer dissatisfactions.
Manual cheque clearing cycle requires human resources and cost more 
Current proposal augments the highlighted portion of the check clearing cycle

![image](https://raw.githubusercontent.com/vvijay83/BoB_LJMU_Warriors/main/Cheque%20Clearing%20Cycle.png)

## Proposed Solution Workflow:
![image](https://github.com/vvijay83/BoB_LJMU_Warriors/blob/5aee41ee47cde5b68b67690fabcf2f3b7d640cfd/Workflow.png)

## Azure Architecture:
![image](https://github.com/vvijay83/BoB_LJMU_Warriors/blob/5aee41ee47cde5b68b67690fabcf2f3b7d640cfd/Architecture.jpg)

## Solution Workflow:

#### Data Collection:

- User data collected directly from authenticated mobile application.
- Cheque image is collected using the App’s camera access feature.
- Azure form recognizer is used to extract the cheque information from the image.

#### Data Transformation:

- Azure Translate API to translate regional languages to English

#### Data Storage:

- Azure Cosmos DB and SQL DB are used to store the image and transaction related features

#### Model Training and Governance:

- Azure anomaly detector to train the model.
- Azure ML Studio - to evaluate the model, implement CICD pipeline, monitor for model and data drift and retrain the model.
- Azure Container Registry - to register the trained model.

#### Model Deployment:

- Azure ML Studio - deploy the candidate model.
- Azure Inference Endpoint - to make realtime inference from the incoming data.

#### Microservices:

- Microservice code pattern is managed under Azure Repository

#### Front-end App:

- Mobile Banking App - to authenticate the user login and capture cheque using camera feature.
- API to transfer image and user details to the backend database.
- Model inference - app makes call to model API and populate the predicted results back to SQL database for the corresponding request id.
- Validation results will be updated on the Mobile banking app.

#### Monitoring and Logging:

- Realtime data is validated with trained data for model and data drift.
- Threshold values are set to trigger model retraining.

## Solution Advantage:
1. Mobile App Inbuilt solution - user don’t have to download new software packages to use this solution.
2. End to End Azure Stack - solution can be implemented end to end using Azure tech stack
3. Multilingual Support - Azure Translate SDK can be used to translate regional languages
4. Highly Scalable with low latency - Azure’s Cosmos / SQL database solution can be leveraged for deployment.
5. Modular Code Pattern - microservice based deployment is adopted to scale the service on demand and add new services like advanced fraud detection in future.
6. Custom ML models - models can be developed and deployed based on the requirements.


# Submission Template for BoB Hackathon

Please use ONLY this template as a starting point to setup your repository for submission into the BoB hackathon.

To get started, click on the green [Use this template](https://github.com/bob-hackathon/submission-template/generate) button, and create a repository within your GitHub Account.

Once you have created your repository within your GitHub account, [Install](https://github.com/bob-hackathon/hackathon-submitter#install) or [Configure](https://github.com/bob-hackathon/hackathon-submitter#configure) the Hackathon Submitter GitHub App on this repository.

When you want to submit an idea/source code, go to the **Issues** tab of your repository, and and click on the **Get Started** button for the `Submit Idea` or `Submit Source Code`, based on what submission you want to make.

For FAQs on how to structure your repository, please check [FAQs.md on the Hackathon Submitter repo](https://github.com/bob-hackathon/hackathon-submitter/blob/main/FAQ.md).
