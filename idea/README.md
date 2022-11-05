**Bank of Baroda Hackathon - 2022**

**Problem Statement**

● Banks handle large volumes of cheques in the clearing process, leaving the system vulnerable to perpetrators, causing processing delays and human errors that are frequently misinterpreted as account holders' negligence.

● Cheque fraud is a type of criminal act that involves the illegal use of cheques to illegally acquire or borrow funds that do not exist within the account balance or legal ownership of the account-holder. The Reserve Bank of India (RBI) has directed banks to implement a system known as Positive Pay beginning in January 2021 in order to reduce cheque-related fraud.

**Solution**

● The proposed idea focuses on automatic cheque processing, which adds an extra layer of security to positive pay by automating the process of bank cheque leaf verification and fraud detection.

**Challenges & Target User Segment**

● With PPS, RBI is augmenting customer safety in high value cheque payments and reduce the fraud occurrences on account of tempering cheque leaves.

● This proposal targets PPS transactions 

● Current and target check clearing transaction distribution



**Share of CTS and PPS (India)**
|   | **By volume**  | **By Value**  |
|---|---|---|
| Current cheque clearing system CTS  |  2% of total retail payments |15% of total retail payments |
| PPS(>5 lakhs,saving A/C >10 lakhs, other) | 20% of total cheques issued | 80% of total cheques issued |

**Current Cheque clearing workflow**

● Cheque clearing cycle has been a manual process to till date resulting in delayed transactions, Frauds and customer dissatisfactions.
● Manual cheque clearing cycle requires human resources and cost more
● Current proposal augments the highlighted portion of the check clearing cycle

**Proposed Solution architecture- Azure stack**

**Solution Workflow**

### Data Collection
● User data collected directly from authenticated mobile application.
● Cheque image is collected using the App’s camera access feature.
● Azure form recognizer is used to extract the cheque information from the image.

### Data Transformation
Azure Translate API to translate regional languages to English

### Data Storage
Azure Cosmos DB and SQL DB are used to store the image and transaction related features

### Model Training and Governance
Azure anomaly detector to train the model.
Azure ML Studio - to evaluate the model, implement CICD pipeline, monitor for model and data drift and retrain the model.
Azure Container Registry - to register the trained model.

### Model Deployment
Azure ML Studio - deploy the candidate model.
Azure Inference Endpoint - to make realtime inference from the incoming data.

### Microservices
Microservice code pattern is managed under Azure Repository

### Front-end App
Mobile Banking App - to authenticate the user login and capture cheque using camera feature.
API to transfer image and user details to the backend database.
Model inference - app makes call to model API and populate the predicted results back to SQL database for the corresponding request id.
Validation results will be updated on the Mobile banking app.

### Monitoring and Logging
Realtime data is validated with trained data for model and data drift.
Threshold values are set to trigger model retraining.




Model Training and Governance

Front-end App

❖

❖

❖

User data collected directly from

❖

❖

Azure anomaly detector to train the

model.

❖

Mobile Banking App - to authenticate the

authenticated mobile application.

user login and capture cheque using

camera feature.

Cheque image is collected using the

App’s camera access feature.

Azure ML Studio - to evaluate the model,

implement CICD pipeline, monitor for

model and data drift and retrain the

model.

❖

❖

API to transfer image and user details to

the backend database.

Azure form recognizer is used to extract

the cheque information from the image.

Model inference - app makes call to

model API and populate the predicted

results back to SQL database for the

corresponding request id.

❖

Azure Container Registry - to register the

trained model.

Data Transformation

Model Deployment

❖

Validation results will be updated on the

Mobile banking app.

❖

Azure Translate API to translate regional

languages to English

❖

❖

Azure ML Studio - deploy the candidate

model.

Monitoring and Logging

Data Storage

Azure Inference Endpoint - to make

realtime inference from the incoming

data.

❖

❖

Realtime data is validated with trained

data for model and data drift.

❖

Azure Cosmos DB and SQL DB are used

to store the image and transaction

related features

Threshold values are set to trigger model

retraining.

Microservices

❖

Microservice code pattern is managed

under Azure Repository





**Solution Advantages:**

\1. Mobile App Inbuilt solution - user don’t have to download new software packages to use this

solution.

\2. End to End Azure Stack - solution can be implemented end to end using Azure tech stack

\3. Multilingual Support - Azure Translate SDK can be used to translate regional languages

\4. Highly Scalable with low latency - Azure’s Cosmos DB / SQL database solution can be leveraged for

deployment.

\5. Modular Code Pattern - microservice based deployment is adopted to scale the service on demand

and add new services like advanced fraud detection in future.

\6. Custom ML models - models can be developed and deployed based on the requirements.





**References**

● [https://economictimes.indiatimes.com/wealth/save/what-is-positive-pay-system-for-cheques-how-](https://economictimes.indiatimes.com/wealth/save/what-is-positive-pay-system-for-cheques-how-does-it-work/articleshow/92762477.cms)

[does-it-work/articleshow/92762477.cms](https://economictimes.indiatimes.com/wealth/save/what-is-positive-pay-system-for-cheques-how-does-it-work/articleshow/92762477.cms)

● <https://nanonets.com/blog/positive-pay/#what-is-positive-pay>

● <https://indianexpress.com/article/explained/positive-pay-system-bank-cheque-rs-50000-7111239/>

● <https://testbook.com/current-affairs/positive-pay-system-for-high-value-cheques/>

● [https://www.npci.org.in/PDF/cts/notified-](https://www.npci.org.in/PDF/cts/notified-documents/CTS_Fraud_Awareness_Training_Mumbai_15_Sep_15.pdf)

[documents/CTS_Fraud_Awareness_Training_Mumbai_15_Sep_15.pdf](https://www.npci.org.in/PDF/cts/notified-documents/CTS_Fraud_Awareness_Training_Mumbai_15_Sep_15.pdf)

● [https://www.bankofbaroda.in/-/media/project/bob/countrywebsites/india/pdfs/key-features-and-](https://www.bankofbaroda.in/-/media/project/bob/countrywebsites/india/pdfs/key-features-and-confirmation-format-for-branchess.pdf)

[confirmation-format-for-branchess.pdf](https://www.bankofbaroda.in/-/media/project/bob/countrywebsites/india/pdfs/key-features-and-confirmation-format-for-branchess.pdf)





\1.

\2.

\3.

