import json
import os

# Define the input directory where your JSONL files are located
input_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/data"

# Create output directories for train, dev, and test data
output_train_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/output/train"
output_dev_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/output/dev"
output_test_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/output/test"

# List of languages you have JSONL files for
languages = ["de-DE", "en-US", "sw-KE"]

# Function to write data to a JSONL file
def write_to_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as outfile:
        for item in data:
            json.dump(item, outfile, ensure_ascii=False, indent=4)  # Pretty print with an indent of 4
            outfile.write("\n")

# Iterate through each language
for language in languages:
    input_filename = os.path.join(input_directory, f"{language}.jsonl")

    # Initialize lists to store train, dev, and test data
    train_data = []
    dev_data = []
    test_data = []

    # Read the JSONL file and split data into train, dev, and test
    with open(input_filename, "r", encoding="utf-8") as infile:
        for line in infile:
            item = json.loads(line.strip())
            if item.get("partition") == "train":
                train_data.append(item)
            elif item.get("partition") == "dev":
                dev_data.append(item)
            elif item.get("partition") == "test":
                test_data.append(item)

    # Write train, dev, and test data to separate JSONL files
    write_to_jsonl(train_data, os.path.join(output_train_directory, f"{language}_train.jsonl"))  #it would've been better to concurtinate
    write_to_jsonl(dev_data, os.path.join(output_dev_directory, f"{language}_dev.jsonl"))
    write_to_jsonl(test_data, os.path.join(output_test_directory, f"{language}_test.jsonl"))


'''
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# Specify the directory path of the client secrets file
client_secrets_path = "C:/Users/andym_000/PycharmProjects/cg_cat/venv/Scripts/client_secret_37267321135-7smrbc3fo0nikv5vd6saghsdsmhhfdb2.apps.googleusercontent.com"

# Authenticate and create a GoogleDrive instance
gauth = GoogleAuth(settings_file=client_secrets_path)
gauth.LocalWebserverAuth()  # This creates a local webserver and automatically handles authentication.
drive = GoogleDrive(gauth)

# Define the Google Drive folder ID where you want to upload the files
folder_id = '1JFDuuuiL55ZVYn_XGj5gmJ7XN8HyYZ4J'

# Define a list of file paths to upload
output_files = [
    os.path.join(output_train_directory, f"{language}_train.jsonl"),
    os.path.join(output_dev_directory, f"{language}_dev.jsonl"),
    os.path.join(output_test_directory, f"{language}_test.jsonl")
]

# Upload each file to the specified folder
for file_path in output_files:
    file_name = os.path.basename(file_path)
    file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
    file.Upload()
    print(f"Uploaded {file_name} to Google Drive folder with ID {folder_id}")
'''
