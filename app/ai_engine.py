import requests
import json
from config.settings import OPENROUTER_API_KEY, MODEL

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

class AIEngine:
    def build_prompt(self, aws_data):
        prompt = f"""
You are a senior Cloud FinOps and DevOps engineer specialized in AWS cost optimization.

Your task is to analyze AWS cost and usage data and produce a professional cost optimization report.

Follow these rules strictly:

1. Identify the most expensive AWS services
2. Detect underutilized resources
3. Suggest cost optimization strategies
4. Estimate potential savings
5. Prioritize recommendations

Focus on services like:
- EC2
- S3
- RDS
- Lambda
- Data Transfer

Return the result in this format:

Summary:
(short explanation of the main cost drivers)

Issues Found:
- issue 1
- issue 2

Recommendations:
- recommendation 1
- recommendation 2

Estimated Savings:
Approximate percentage or dollar savings.

AWS Data:
{json.dumps(aws_data, indent=2)}
"""
        return prompt

    def analyze(self, aws_data):
        prompt = self.build_prompt(aws_data)

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a cloud cost optimization expert."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            raise Exception(f"AI request failed: {response.text}")

        result = response.json()
        return result["choices"][0]["message"]["content"]