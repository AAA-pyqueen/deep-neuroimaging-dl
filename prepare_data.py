import os
import requests

# Customize for OpenNeuro ds006072 and desired file path
accession = "ds006072"
snapshot = "1.0.0"
subject = "sub-01"
file_path = f"{subject}/anat/{subject}_T1w.nii.gz"

# Construct the download URL
url = f"https://openneuro.org/crn/datasets/{accession}/snapshots/{snapshot}/files/{file_path}"

# Create output directory
output_dir = os.path.join("data", "raw")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"{subject}_T1w.nii.gz")

# Download the file
print(f"Downloading NIfTI file from:\n{url}\n")
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"[✓] Downloaded: {output_file}")
else:
    print(f"[✗] Failed to download file. HTTP status code: {response.status_code}")

