import os
import subprocess

def main():
    # Define the AWS credentials file
    aws_credentials_file = "~/.aws/credentials"

    # Define the AWS region
    aws_region = "us-west-2"

    # Define the command to run
    command = f"aws s3 sync s3://my-bucket /tmp/my-bucket --delete"

    # Define the script to run in the AWS console
    script = f"""
    aws configure set aws_access_key_id {os.environ['AWS_ACCESS_KEY_ID']}
    aws configure set aws_secret_access_key {os.environ['AWS_SECRET_ACCESS_KEY']}
    aws s3 sync s3://my-bucket /tmp/my-bucket --delete
    """

    # Run the script in the AWS console
    subprocess.run(script, shell=True, env={"AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"), "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY")})

if __name__ == "__main__":
    main()