# MyProject

- add new environment to deploy-config
- create a new feature branch with new colour
- switch to master, update deploy-config so an environment points at the new branch
- merge branch with master, show changes to other environments
- create a tag (0.0.1), add mapping for prod for tag
- add a bug to master, create a tag (0.0.2) and apply to prod.
- merge in to master a new feature that we dont want to release yet
- show the bug in prod.
- now the prod bug is noticed, but we cant release prod from master as it contains a feature we're not ready to release yet
- create a hotfix branch from the previous release tag (0.0.2)

```
git checkout -b <New Branch Name> <TAG Name>
```

- tag the hotfix branch (0.0.3). release this to prod
- show prod fixed
- merge the branch to master
- tag master (0.0.4) to indicate the pending feature is ready, show in prod