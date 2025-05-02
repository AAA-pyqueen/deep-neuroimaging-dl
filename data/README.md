# Neuroimaging Data

This folder contains data used in the Deep Learning for Neuroimaging project.

## Structure
- `raw/` — Original `.nii.gz` NIfTI files downloaded from OpenNeuro or ADNI.
- `processed/` — Numpy arrays and preprocessed slices ready for model input.
- `labels.csv` — Diagnosis and metadata labels for supervised learning.

## Note on ADNI/HCP
ADNI and HCP datasets require account approval and data use agreements.

## Sample Data: Psilocybin Precision Functional Mapping
*Open Neuro Accession Number ds006072*
This dataset is hosted at: <https://openneuro.org/datasets/ds006072>

📝 Optional Customizations
- To download other modalities or sessions, change file_path to the desired relative path from the OpenNeuro dataset structure.
- You can also loop over multiple subjects like sub-01, sub-02, etc., if you're scaling up.
