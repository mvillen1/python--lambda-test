#!/bin/bash
echo "Lambda files got changed. Going to update lambda function code"
aws ssm get-parameters-by-path --path /Test-LAMBDA --region us-west-2 | jq -r '.Parameters | map(.Name+"="+.Value)| join("\n") | sub("/Test-LAMBDA/"; ""; "g")  ' > .env
mkdir -p /tmp/lamda/Test
echo Copying Files from Project to Temp Folder
rsync -a  Test/ /tmp/lamda/Test/
mv /tmp/lamda/Test/Test.py /tmp/lamda/Test/lambda_function.py
cp .env /tmp/lamda/Test/.env
cd /tmp/lamda/Test/ && zip -rq ../Test.zip .
aws s3 cp /tmp/lamda/Test.zip s3://codepipeline-us-east-1-170278925856/lambda_functions/Test-Lambda/Test.zip
aws lambda update-function-code --function-name TestLambda --s3-bucket codepipeline-us-east-1-170278925856 --s3-key lambda_functions/Test-Lambda/Test.zip