# gitea-custom

The repo contains custom templates and locale to be added to gitea setup to apply custom modifications without conflicts for the gitea fork with the common files of the base gitea repo

Get in touch with the team on telegram: https://t.me/joinchat/BjVkRRCDNTlaMbHtus8uaQ

## roadmap / releases
- [1.0.0 kanban](https://waffle.io/gigforks/gitea?milestone=1.0.0)
  - Itsyouonline integration for registration / login
  - Support migration from old gogs installation
- [1.1.0 kanban](https://waffle.io/gigforks/gitea?milestone=1.1.0)
  - Webhooks for automation on issues
  - Issue reference overview in issue detail
  - Full text search

## Repository structure

### Gitea fork
Repo: https://github.com/gigforks/gitea
Branches:
- [master](https://github.com/gigforks/gitea): This branch is kept compatible with the upstream gitea repository of the gitea authors
- [iyo_integration](https://github.com/gigforks/gitea/tree/iyo_integration): In this branch we added custom features that need to be added in this repository. The main changes added here are about authentication via itsyou.online. This branch should only contain changes we cannot push upstream via PR, because they are too custom.
  - Configuration instructions for gitea - itsyou.online integration can be found here: https://github.com/gigforks/gitea/blob/iyo_integration/docs/itsyouonline.md

### Gitea custom
Repo: https://github.com/Incubaid/gitea-custom

This repo is used for gitea project management and custom layout templates

### Gitea kanban
Repo: https://github.com/Incubaid/gitea-kanban

This repo holds a kanban implementation for gitea

### Gitea mgmt
Repo: Repo: https://github.com/Incubaid/gitea-mgmt

This repo holds scripts for automating management tasks to gitea
