import json
import requests

headers = {
    'Cache-Control': 'no-cache',
}

# Dictionary to store the different files to be updated
update_files = {
    "program": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/program.txt",
    "verbiage": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/verbiage.txt",
    "template": "https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/template.txt"
}

# Remote version to compare against
version_url = 'https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/remote_version.json'
version_response = requests.get(version_url, headers=headers)

def compare_versions():
    print(remote_data['template'])

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

with open('local_version.json', 'r') as local_file:
    local_data = json.load(local_file)

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
