class AWSCollector:

    def collect_ec2_data(self):
        print("[INFO] Using Mock AWS Data for testing purposes...")
        
        mock_data = [
            {
                "service": "EC2",
                "instance_id": "i-0123456789abcdef0",
                "instance_type": "m5.4xlarge",
                "state": "running",
                "cpu_utilization_percent": 4,  
                "monthly_cost_usd": 680.00
            },
            {
                "service": "EC2",
                "instance_id": "i-0abcdef1234567890",
                "instance_type": "t3.micro",
                "state": "running",
                "cpu_utilization_percent": 85,
                "monthly_cost_usd": 15.50
            },
            {
                "service": "EC2",
                "instance_id": "i-0987654321fedcba0",
                "instance_type": "c5.large",
                "state": "stopped", 
                "attached_ebs_volume_cost": 25.00,
                "monthly_cost_usd": 25.00 
            },
            {
                "service": "S3",
                "bucket_name": "old-backups-bucket-2021",
                "storage_class": "Standard",
                "size_gb": 5000,
                "last_accessed_days_ago": 400,
                "monthly_cost_usd": 115.00
            }
        ]

        return mock_data