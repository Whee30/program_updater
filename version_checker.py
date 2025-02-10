import json

with open('local_version.json', 'r') as local_file:
    local_data = json.load(local_file)

with open('remote_version.json', 'r') as remote_file:
    remote_data = json.load(remote_file)

print(f"Remote version is: {remote_data['v']}, Local version is: {local_data['v']}.")


if remote_data['v'] > local_data['v']:
    print("remote is bigger")
elif remote_data['v'] < local_data['v']:
    print("Remote is smaller")
elif remote_data['v'] == local_data['v']:
    print("They're the same")
else:
    print("something else happened")

