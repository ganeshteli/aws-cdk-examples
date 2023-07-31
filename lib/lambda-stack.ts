import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class LambdaStack extends cdk.Stack{

  public readonly lambdaFunction: lambda.Function;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    this.lambdaFunction = new lambda.Function(this, 'demo-lambda', {
        functionName: 'demo-lambda',
        runtime: lambda.Runtime.PYTHON_3_9,
        code: lambda.Code.fromAsset('src/lambdas'),
        handler: "demo_lambda.lambda_handler"
    });
  }
}