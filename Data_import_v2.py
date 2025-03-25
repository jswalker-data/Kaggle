import os
import subprocess
import zipfile

# Set the competition name
competition_name = "playground-series-s5e3"

# Define the target directory as ./<competition_name>/data/
base_dir = os.path.join(os.getcwd(), competition_name)
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Use Kaggle API to download competition files into the data directory
try:
    print(f"Downloading files for competition: {competition_name}")
    subprocess.run(
        ["kaggle", "competitions", "download", "-c", competition_name, "-p", data_dir],
        check=True,
    )
    print("Download complete.")
except subprocess.CalledProcessError as e:
    print("An error occurred while downloading the competition files:", e)
    exit(1)

# Unzip and remove any .zip files in the data directory
for file in os.listdir(data_dir):
    if file.endswith(".zip"):
        zip_path = os.path.join(data_dir, file)
        print(f"Extracting {file}...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(data_dir)
        os.remove(zip_path)
        print(f"Removed {file}")

print(f"All files are ready in: {data_dir}")
