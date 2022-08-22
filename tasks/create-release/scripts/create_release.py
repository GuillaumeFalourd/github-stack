#!/usr/bin/python3
import requests
import json
import sys

# Extract values from inputs
token = sys.argv[1]
owner = sys.argv[2]
repository_name = sys.argv[3]
branch = sys.argv[4]
version = sys.argv[5]
description = sys.argv[6]

# Start script
github_api_url = f"https://api.github.com/repos/{owner}/{repository_name}/releases"

data = {}
data["body"] = description
data["target_commitish"] = branch
data["tag_name"] = version
data["name"] = f"Release {version}"
json_data = json.dumps(data)

authorization = f"token {token}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization" : authorization,
    }

r = requests.post(
    url = github_api_url,
    data = json_data,
    headers = headers
    )

if r.status_code == 201:
    print(f"✅ Release \033[36m{version}\033[0m successfully generated for {owner}'s \033[36m{repository_name}\033[0m repository")

else:
    print("❌ Couldn't generate repository release")
    print (r.status_code, r.reason)