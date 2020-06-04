import os
import sys


commithash = os.getenv("INPUT_HASH")
tag = os.getenv("INPUT_TAG")


if commithash is None and tag is None:
    print("Must provide either a commit hash or tag")
    sys.exit(1)

if (not commithash is None) and (not tag is None):
    print("Can not provide both a commit hash and tag")
    sys.exit(1)

os.environ['COMMIT'] =  commithash if (not commithash is None) else tag
os.environ['BRANCH'] = os.getenv("INPUT_BRANCH")
os.system("/createbranch.sh")


