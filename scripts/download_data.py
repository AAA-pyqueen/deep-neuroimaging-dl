from nilearn import datasets

def download_openneuro_data():
    # Example: ADHD resting-state data
    data = datasets.fetch_adhd(n_subjects=1)
    print("Downloaded files:", data)

if __name__ == "__main__":
    download_openneuro_data()
