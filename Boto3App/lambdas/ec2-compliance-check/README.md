https://chatgpt.com/c/6879fd5a-de38-800d-a83c-9471bf25310c

📁 Project Structure
pgsql
Copy
Edit
ec2-config-rule-sam/
├── template.yaml               # SAM template
├── samconfig.toml             # Optional default deployment values
├── parameters/
│   ├── dev.json
│   ├── uat.json
│   ├── stage.json
│   └── prod.json
└── ec2_compliance/
    └── app.py                 # Lambda function

-------------
🚀 4. Deploy to Each Environment
-------------
for dev:
sam build
sam deploy --guided --parameter-overrides $(cat parameters/dev.json | jq -r 'to_entries|map("\(.key)=\(.value)")|.[]')

for prod:
sam deploy --stack-name ec2-compliance-prod \
  --parameter-overrides $(cat parameters/prod.json | jq -r 'to_entries|map("\(.key)=\(.value)")|.[]')
💡 Requires jq CLI tool to parse JSON params into CLI format.

-------------
🧹 5. Delete Per Environment
-------------
sam delete --stack-name ec2-compliance-prod
Repeat for dev, uat, etc.

