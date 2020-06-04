import os
import sys

commithash = os.getenv("INPUT_HASH")
tag = os.getenv("INPUT_TAG")

if commithash == "" and tag == "":
    print("Must provide either a commit hash or tag")
    sys.exit(1)

if commithash != "" and tag != "":
    print("Can not provide both a commit hash and tag")
    sys.exit(1)

os.environ['COMMIT'] =  commithash if commithash != "" else tag
os.environ['BRANCH'] = os.getenv("INPUT_BRANCH")
os.system("./createtmpbranch.sh")


