import os
import sys

print("New Action")

commithash = os.getenv("INPUT_HASH")
tag = os.getenv("INPUT_TAG")

print(commithash)
print(tag)

if commithash == "" and tag == "":
    print("Must provide either a commit hash or tag")
    sys.exit(1)

if (not commithash == "") and (not tag == ""):
    print("Can not provide both a commit hash and tag")
    sys.exit(1)

os.environ['COMMIT'] =  commithash if commithash != "" else tag
os.environ['BRANCH'] = os.getenv("INPUT_BRANCH")
os.system("./createtmpbranch.sh")


