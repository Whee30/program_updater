import json
import requests

headers = {
    'Cache-Control': 'no-cache'
}

# Placeholder dictionary
remote_data = {}

# Dictionary to store the different files to be updated
remote_files = {
    "program": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/program.txt",
    "verbiage": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/verbiage.txt",
    "template": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/template.txt"
}

# Declare the local filepaths for potential update
local_files = {
    "program": "program.txt",
    "verbiage": "verbiage.txt",
    "template": "template.txt"
}

# Load local version numbers
with open('local_version.json', 'r') as local_version_file:
    local_version_data = json.load(local_version_file)

# Remote version to compare against
version_url = 'https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/remote_version.json'
version_response = requests.get(version_url, headers=headers)


def compare_versions():
    if local_version_data['program'] < remote_data['program']:
        download_update('program', remote_data['program'])
    if local_version_data['verbiage'] < remote_data['verbiage']:
        download_update('verbiage', remote_data['verbiage'])
    if local_version_data['template'] < remote_data['template']:
        download_update('template', remote_data['template'])
    print('Everything is up to date!')

def download_update(target, version):
    print(target)
    file_response = requests.get(remote_files[target], headers=headers)
    with open(local_files[target], 'wb') as file:
        file.write(file_response.content)
    local_version_data[target] = version
    with open('local_version.json', 'w') as file:
        json.dump(local_version_data, file, indent=4)
    print(f"{target} was updated.")

# Check for a valid connection to the remote version file
if version_response.status_code == 200:
    remote_data = version_response.json()
    compare_versions()
else:
    print(f"Failed to fetch data: {version_response.status_code}")