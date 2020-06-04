#!/bin/sh



set -e
echo "---"
echo $COMMIT
echo $BRANCH
echo "---"



if [[ -z "$INPUT_GITHUB_TOKEN" ]]; then
  echo "Set the GITHUB_TOKEN environment variable."
  exit 1
fi

# Github actions no longer auto set the username and GITHUB_TOKEN
git remote set-url origin "https://$GITHUB_ACTOR:$INPUT_GITHUB_TOKEN@github.com/$GITHUB_REPOSITORY"

# Pull all branches references down locally so subsequent commands can see them
git fetch origin '+refs/heads/*:refs/heads/*' --update-head-ok

echo "Old set of branches"
# Print out all branches
git --no-pager branch -a -vv


COMMAND="git checkout $COMMIT"
echo $COMMAND
GO_TO_OBJECT=$(sh -c "$COMMIT")

if [["$?" != "0"]]; then
  exit 1
fi

COMMAND="git checkout -b $BRANCH"
echo $COMMAND
CREATE_LOCAL_BRANCH=$(sh -c "$COMMAND")

if [["$?" != "0"]]; then
  exit 1
fi

COMMAND="git push origin $TMPBRANCH"
echo $COMMAND
PUSH_BRANCH=$(sh -c "$COMMAND")

if [["$?" != "0"]]; then
  exit 1
fi

echo "New set of branches"
# Print out all branches
git --no-pager branch -a -vv