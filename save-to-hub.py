# Example usage:
# python save.py --model=./model-out/merged --hub_id=animuslabs/Xavier-R1

from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse
from huggingface_hub import HfApi
import os

api = HfApi()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str)
    parser.add_argument("--hub_id", type=str)
    return parser.parse_args()

def main():
    args = get_args()

    # Get all files in the specified directory
    local_file_paths = [os.path.join(args.model, f) for f in os.listdir(args.model) if os.path.isfile(os.path.join(args.model, f))]

    # Loop through each file and upload it
    for local_file_path in local_file_paths:
        # Extract the file name from the local file path
        file_name = os.path.basename(local_file_path)

        # Specify the path where you want the file to be uploaded in the repository
        path_in_repo = file_name

        # Upload the file
        api.upload_file(
            path_or_fileobj=local_file_path,
            path_in_repo=path_in_repo,
            repo_id=args.hub_id,
            repo_type="model"  # Assuming it's a model; can be "dataset" or "space" as well
        )
        print(f"Uploaded {file_name} to {args.hub_id}")

    print("Merged model uploaded to Hugging Face Hub!")

if __name__ == "__main__":
    main()