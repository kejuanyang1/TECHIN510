# TECHIN 510 LAB 1
Kejuan Yang's Personal Website


## Getting Started
Open the terminal and run the following commands:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then activte the envrionment:
```
source .venv/bin/activate
```
If you want to run the app locally:
```
streamlit run app.py
```

## What's Included
- ```app.py```: The main Flask application

## Lessons Learned
- How to use Streamlit to create a simple website
- How to use requirements.txt to manage Python dependencies
- How to use GitHub Actions to deploy a website to Azure App Service

## Questions
1. I recieved App Service Validation Error when selecting US West 1 and West 2. The exact error is as below:
```
{"code":"InvalidTemplateDeployment","details":[{"code":"ValidationForResourceFailed","message":"Validation failed for a resource. Check 'Error.Details[0]' for more information.","details":[{"code":"SubscriptionIsOverQuotaForSku","message":"This region has quota of 0 instances for your subscription. Try selecting different region or SKU."}]}],"message":"The template deployment 'Microsoft.Web-FunctionApp-Portal-01b72bda-996c' is not valid according to the validation procedure. The tracking id is 'ed86df9b-5636-4adf-9e6c-4659d4ae6852'. See inner errors for details."}
```

The error disappears when selecting West 3 and the paid app plan B1.
