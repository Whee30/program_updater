import json
import requests

v_url = 'https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/remote_version.json'
v_response = requests.get(v_url)
p_url = 'https://raw.githubusercontent.com/Whee30/program_updater/refs/heads/main/program.txt'
p_response = requests.get(p_url)

# Local path where you want to save the downloaded file
p_dest = 'file.txt'

if v_response.status_code == 200:
    remote_data = v_response.json()
    print(remote_data['v'])
else:
    print(f"Failed to fetch data: {v_response.status_code}")

def update_local(new_version):
    with open(p_dest, 'wb') as file:
        file.write(p_response.content)
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

