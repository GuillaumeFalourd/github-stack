#!/usr/bin/python3
import requests
import json
import re
import os
import sys

def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s\-]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s

# Extract values from inputs
token = sys.argv[1]
repository_name = sys.argv[2]
private = sys.argv[3]
clone = sys.argv[4]

# Start script
repository = urlify(repository_name)

github_api_url = f"https://api.github.com/user/repos"

data = {}
data["name"] = repository
data["description"] = "Project created using StackSpot Platform"
data["homepage"] = "https://stackspot.com"
data["auto_init"] = True
if private == "no":
    data["private"] = False
else:
    data["private"] = True

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
    print(r.json())
    full_name = r.json()["full_name"]
    print(f"✅ Repository successfully created on \033[36mhttps://github.com/{full_name}\033[0m!")

    if clone == "yes":
        os.system(f"git clone -q https://github.com/{full_name}.git")
        print(f"✅ Repository successfully cloned on the \033[36mcurrent directory\033[0m!")

else:
    print(f"❌ Couldn't create new repository")
    print(f"🤖 Please: check your PAT scope permission, or if a repo with this name already exists!")
    print (r.status_code, r.reason)
