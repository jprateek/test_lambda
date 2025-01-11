import csv
import io
import boto3
import datetime

def lambda_handler(event, context):
    # Data to be written to CSV
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]
    
    # Create a CSV file in memory
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerows(data)
    
    # Generate a dynamic file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"test_{timestamp}.csv"
    
    # Upload the CSV file to S3
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket='mytestbucketpj', Key=file_name, Body=csv_buffer.getvalue())
        return {
            'statusCode': 200,
            'body': f'CSV file {file_name} created and uploaded to S3 successfully!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error uploading CSV file to S3: {str(e)}'
        }
