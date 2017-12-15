# Scripts

First get a personal access token (PAT) on Gitea.

Copy this PAT in both `labels.yaml` and `milestones.yaml`.

The below script are intended to set the labels and milestones of repositories.

In order to execute these scripts you'll need to have [JumpScale9](https://github.com/Jumpscale/bash/blob/master/README.md) installed and [PyYaml](https://github.com/yaml/pyyaml).

## Labels

Make sure to update the file `labels.yaml`:
- labels: list of labels
- label: 
    - name: string
    - color: string (hex color code, make sure to include the #)
- repos: list of repositories
- repository:
    - name: string
    - owner: string

Here's an example:
```yaml
token: <$PAT>

labels:
  -
    name: priority_critical
    color: '#b60205'
  -
    name: priority_major
    color: '#f9d0c4'

repos:
  -
      name: yves_repo
      owner: yves@vreegoebezig.be
  -
      name: yves_repo2
      owner: yves@vreegoebezig.be
```

Execute the script as follows:
```bash
./label.py
```


## Milestones

Make sure to update the file `milestones.yaml`:
- milestoneS: list of milestone
- milestone: 
    - title: string
    - description: string 
    - (optional) due_on: string (date time format, RFC 3339)
- repos: list of repositories
- repository:
    - name: string
    - owner: string
    

Here's an example:
```yaml
token: <$PAT>

milestones:
  - 
    title: RC2
    due_on: "2017-12-15T15:22:43.188Z"
    description: test 
  - 
    title: RC3
    description: test 

repos:
  -
      name: yves_repo
      owner: yves@vreegoebezig.be
```

Execute the script as follows:
```bash
./milestones.py
```