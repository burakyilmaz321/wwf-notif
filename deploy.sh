#!/bin/bash

pip install --target ./package -r requirements.txt
zip -r package.zip package
aws lambda update-function-code --function-name linkedin-company-jobs-service --zip-file fileb://main.zip
