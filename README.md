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
- `imgs/`: A directory containing images used by the application.
- `README.md`: The markdown file providing a descriptive overview of the project, setup instructions, and additional information.
- `requirements.txt`: A text file listing the Python dependencies for the project, which can be installed using `pip`.

## Lessons Learned
- I learned the logic flow of how to build and host a website using Azure app service, sync with a Github repo. When deploying the website, the envrionment ```.venv``` cannot be included in the repo, otherwise the deployment would fail. It takes around 5 minutes to build and deploy everytime I update the website.
- I practiced how to use Streamlit to build the frontend page. It shares the similar logic with markdown.

## Questions
- I recieved App Service Validation Error when selecting US West 1 and West 2. The exact error is as below:
```
{"code":"InvalidTemplateDeployment","details":[{"code":"ValidationForResourceFailed","message":"Validation failed for a resource. Check 'Error.Details[0]' for more information.","details":[{"code":"SubscriptionIsOverQuotaForSku","message":"This region has quota of 0 instances for your subscription. Try selecting different region or SKU."}]}],"message":"The template deployment 'Microsoft.Web-FunctionApp-Portal-01b72bda-996c' is not valid according to the validation procedure. The tracking id is 'ed86df9b-5636-4adf-9e6c-4659d4ae6852'. See inner errors for details."}
```

The error disappears when selecting West 3 and the paid app plan B1. I'm still not sure how to solve this issue.
