# Welcome to your CDK TypeScript project
This is a blank project for CDK development with TypeScript.
The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands
* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests

* 'aws configure --profile profile-name'
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

* `npm install -g aws-cdk` 
* `cdk init app --language typescript` 
* `cdk ls` 

# Local lambda test
* `sam local invoke --event events/event.json -t ./cdk.out/myLambdaStack.template.json demo-lambda` 

# Run tests
* `cd test` 
* `python3 -m pip install -r requirements.txt` 
* `pytest test_demo_lambda.py`
