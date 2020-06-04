import os
import sys

print("New Action")

commithash = os.getenv("INPUT_HASH")
tag = os.getenv("INPUT_TAG")

print(commithash)
print(tag)

if commithash is None and tag is None:
    print("Must provide either a commit hash or tag")
    sys.exit(1)

if (not commithash is None) and (not tag is None):
    print("Can not provide both a commit hash and tag")
    sys.exit(1)

os.environ['COMMIT'] =  commithash if commithash is None else tag
os.environ['BRANCH'] = os.getenv("INPUT_BRANCH")
os.system("./createtmpbranch.sh")


