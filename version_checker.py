import json
import requests

headers = {
    'Cache-Control': 'no-cache'
}

remote_data = {}

# Dictionary to store the different files to be updated
remote_files = {
    "program": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/program.txt",
    "verbiage": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/verbiage.txt",
    "template": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/template.txt"
}

local_files = {
    "program": "program.txt",
    "verbiage": "verbiage.txt",
    "template": "template.txt"
}

# Load local versions
with open('local_version.json', 'r') as local_version_file:
    local_version_data = json.load(local_version_file)

# Remote version to compare against
version_url = 'https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/remote_version.json'
version_response = requests.get(version_url, headers=headers)


def compare_versions():
    if local_version_data['program'] < remote_data['program']:
        download_update(remote_files['program'], local_files['program'])
    if local_version_data['verbiage'] < remote_data['verbiage']:
        download_update(remote_files['verbiage'], local_files['verbiage'])
    if local_version_data['template'] < remote_data['template']:
        download_update(remote_files['template'], local_files['template'])

def download_update(remote_version, local_version):
    print(remote_version)
    file_response = requests.get(remote_version, headers=headers)
    with open(local_version, 'wb') as file:
        file.write(file_response.content)
    print(f"{local_version} was updated.")

if version_response.status_code == 200:
    remote_data = version_response.json()
    compare_versions()
else:
    print(f"Failed to fetch data: {version_response.status_code}")

'''
def update_local(new_version):
    with open(p_dest, 'wb') as file:
        #file.write(p_response.content)
    with open('local_version.json', 'r') as local_v:
        local_d = json.load(local_v)
        local_d['v'] = new_version
    with open('local_version.json', 'w') as local_v_w:
        json.dump(local_d, local_v_w, indent=4)



print(f"Remote version is: {remote_data['v']}, Local version is: {local_data['v']}.")

if remote_data['v'] > local_data['v']:
    print("remote is bigger")
    update_local(remote_data['v'])
elif remote_data['v'] < local_data['v']:
    print("Remote is smaller")
elif remote_data['v'] == local_data['v']:
    print("They're the same")
else:
    print("something else happened")
'''
