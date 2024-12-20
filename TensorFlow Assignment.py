# Import required libraries
import os
from google.cloud import storage
from google.cloud import aiplatform

# Set up project and region variables 
PROJECT_ID = "amiable-variety-440922-r1"
REGION = "us-central1"

#Set the bucket name
BUCKET_NAME = "my-new-bucket-987654321"

# Authenticate Google Cloud account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Owner\\Documents\\Google Cloud\\amiable-variety-440922-r1-bc8d1508fb31.json"

# Create Cloud Storage bucket
def create_bucket(bucket_name):
    """
    Create Cloud Storage bucket with the given name.
    """
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket created:", bucket.name)

# Upload dataset file to Cloud Storage bucket
def upload_dataset(bucket_name, dataset_path):
    """
    Create a Cloud Storage bucket with the given name.
    """
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    blob = bucket.blob(os.path.basename(dataset_path))
    blob.upload_from_filename(dataset_path)
    print("Dataset file upload to cloud Storage")

# Create Tabular Dataset in Vertex AI
def create_tabular_dataset(bucket_name, dataset_path):
    """
    Create a tabular Dataset in Vertex AI using the specified bucket and dataset file.
    """
    aiplatform.init(project=PROJECT_ID, location=REGION)

    gcs_source_uri = f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    dataset = aiplatform.TabularDataset.create(display_name="my-dataset", gcs_source=gcs_source_uri)
    print("Tabular Dataset created:", dataset.display_name)

# Analyze the dataset
def analyze_dataset(bucket_name, dataset_path):
    dataset = aiplatform.TabularDataset(
        Project=PROJECT_ID,
        loaction=REGION,
        display_name="my_dataset",
        gcs_source=f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    )
    analysis = dataset.analyze()
    print("Dataset analysis results:")
    print(analysis)

# Main function
def main():
    """
    Main function that orchestrates the steps to create the bucket, upload the dataset, and create the Tabular Dataset.
    """
    create_bucket(BUCKET_NAME)
    upload_dataset(BUCKET_NAME, r"C:\\Users\\Owner\\Documents\\GitHub\\Python_AI_Course\\image_dataset.csv")
    create_tabular_dataset(BUCKET_NAME, r"C:\\Users\\Owner\\Documents\\GitHub\\Python_AI_Course\\image_dataset.csv")

# Execute the main function
if __name__ == "__main__":
    main()



    
