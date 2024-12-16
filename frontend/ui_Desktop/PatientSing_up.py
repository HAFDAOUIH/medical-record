import requests

def upload_to_ipfs(file_path):
    try:
        # Read the file content
        with open(file_path, "rb") as f:
            response = requests.post("http://127.0.0.1:5001/api/v0/add", files={"file": f})
            response.raise_for_status()
            ipfs_hash = response.json()["Hash"]
            return ipfs_hash
    except Exception as e:
        print(f"Error uploading to IPFS: {e}")
        return None

# Test the function
if __name__ == "__main__":
    file_path = r"C:/Users/Hanane/Desktop/Projet1_CBIR_G3.pdf"  # Replace with your file's path
    ipfs_hash = upload_to_ipfs(file_path)
    if ipfs_hash:
        print(f"File uploaded to IPFS: https://ipfs.io/ipfs/{ipfs_hash}")
    else:
        print("Failed to upload file.")
