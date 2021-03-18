Recognize user provided hand-written numbers.  
Base_model is trained with MNIST dataset.  
<br/>
To run backend and frontend, run the following commands

- backend: uvicorn api.main:app --reload
- frontend: yarn start

## Deployment

### With Workbench Serving service

#### Deploy application

- On Workbench, naviagate to App Template tools (On sidebar or Tools)
- Click on Digit Classification application, waiting for application to be cloned successfully
- Navigate to Serving panel, select `DigitClassificationService` service
- Click Deploy button

#### Testing application

Use this command to test the API

```bash
curl --location --request POST '{URL}' --form 'upload_file=@{LOCAL_FILE_PATH}'
```
