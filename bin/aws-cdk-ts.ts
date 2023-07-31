#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3Stack } from '../lib/s3-stack';
import { LambdaStack } from '../lib/lambda-stack';

const app = new cdk.App();

const lambda_stack = new LambdaStack(app, 'myLambdaStack');

const s3_stack = new S3Stack(app, 'myS3Stack', { lambdaFunction: lambda_stack.lambdaFunction});

const bucket = s3_stack.bucket;