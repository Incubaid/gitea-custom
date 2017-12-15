#!/usr/bin/env python3

import yaml
from js9 import j

with open("labels.yaml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)

    except yaml.YAMLError as e:
        print(e)

token = data_loaded["token"]

gitea = j.clients.gitea.get_client("https://docs.grid.tf/api/v1", token)


for label in data_loaded["labels"]:
    print(label)
    for repo in data_loaded["repos"]:
        gitea.repos.issueCreateLabel(label, repo["name"], repo["owner"])
