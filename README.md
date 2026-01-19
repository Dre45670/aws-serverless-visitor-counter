# AWS Serverless Visitor Counter

A serverless visitor counter built using AWS Lambda, API Gateway, and DynamoDB.
The counter increments on each page load and displays the total number of visitors
on a static portfolio website.

## Architecture
Browser → API Gateway → Lambda → DynamoDB

## Services Used
- AWS Lambda
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## Features
- Serverless architecture (no EC2 or servers)
- DynamoDB atomic counter updates
- REST API endpoint returning JSON
- CORS-enabled for browser access
- Least-privilege IAM execution role
- CloudWatch logging and monitoring

## How It Works
1. Website loads and triggers a JavaScript fetch request
2. API Gateway invokes Lambda
3. Lambda increments and retrieves count from DynamoDB
4. Count is returned as JSON and displayed on the page

## Example API Response
```json
{ "count": 42 }
