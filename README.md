# AI Cloud Optimizer

A FinOps and DevOps tool designed to analyze AWS cloud infrastructure data and generate professional cost optimization reports using AI.

## Overview
This project evaluates AWS resource utilization to identify idle or over-provisioned assets. It processes infrastructure data and leverages an advanced AI model to provide actionable recommendations and estimated monthly savings.

**Note on Testing and Performance:** For demonstration and performance evaluation purposes, the current repository utilizes mock AWS infrastructure data (local JSON files). For production environments, the system is designed to seamlessly transition to live data retrieval.

## Architecture & Integration
This tool is built to integrate directly with AWS environments:
- **boto3:** Used for programmatic access to AWS services, allowing automated data collection from the infrastructure.
- **Amazon EC2:** Designed to operate on an EC2 instance, acting as a secure and centralized hub for execution and continuous analysis within the AWS ecosystem.

## Prerequisites & Requirements
To run this application, you must fulfill the following requirements:

1. **AWS Account Configuration:** Active AWS credentials configured on your execution environment (e.g., via `aws configure` or IAM roles if deployed on EC2).
2. **OpenRouter API Key:** A valid API key from OpenRouter is mandatory to access the AI models used for generating the optimization reports. 
   - You must generate your own key from OpenRouter and add it to your environment variables.

## Project Structure
- `app/`: Core application logic (Data collection, AI engine, and analysis).
- `config/`: Configuration settings and environment variable management.
- `data/`: Directory containing mock JSON data used for testing and demonstration.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [Your-Repository-URL]