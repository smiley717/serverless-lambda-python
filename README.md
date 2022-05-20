# Get customer Name by id
Get the customer name using the customer id from the customers

## Testing
1. Create a virtual enviroment to test
'''
virtualenv -p python3 venv
'''
2. Install requirements
'''
source venv/bin/activate
pip install -r requirements.txt
'''

## Test URL
```
https://q9a8nfege5.execute-api.us-east-1.amazonaws.com/customer/{id}
```

- **URL**: `/customer/3`
- **METHOD**: `GET`
- **PATH PARAMS**:

```json
{
  "id": "3"
}
```

- **QUERY PARAMS**: N/A
- **REQUEST BODY**: N/A
- **RESPONSE BODY**:

```json
{
    "body": "{\"message\": \"You have retrieved customer name successfully!\", \"name\": \"Jordan Shamir\"}",
    "statusCode": 200,
    "headers": {
        "access-control-allow-origin": "*"
    }
}
```

## Debug Lambda function locally

You can run your lambda function locally by running
`sls invoke local --function MyFunction --path ./sampleInputs/input.json --stage dev`

## Manual deployment

Run `sls deploy --aws-profile YOUR_AWS_PROFILE` to deploy your cloudformation stack to your AWS Account.
