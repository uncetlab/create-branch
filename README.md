# Github Create Branch

## Features
- Create a branch from a specific tag


## Options
```
jobs:
    <some job>:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
            - name: create-branch
              uses: et-lab/create-branch@v1
              with: 
                hash: "" #commit hash to start branch at. Conflicts and fails with tag.
                tag: "" #tag you want to start branch at Conflicts and fails with hash.
                name: "" #name of the branch (required)
                github_token:  ${{ secrets.GITHUB_TOKEN }} (required)
                
```