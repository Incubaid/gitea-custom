#!/usr/bin/env python3

import yaml

from js9 import j

with open("milestones.yaml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)

    except yaml.YAMLError as e:
        print(e)

token = data_loaded["token"]

gitea = j.clients.gitea.get_client("https://docs.grid.tf/api/v1", token)


for milestone in data_loaded["milestones"]:
    print(milestone)
    for repo in data_loaded["repos"]:
        gitea.repos.issueCreateMilestone(milestone, repo["name"], repo["owner"])
