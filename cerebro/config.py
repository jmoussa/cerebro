from dotmap import DotMap
import json
import os

CONFIG_LOCATION = os.getenv("CONFIG_LOCATION")

if CONFIG_LOCATION is None:
    raise Exception("Please set environment variable `CONFIG_LOCATION`")

f = open(str(CONFIG_LOCATION) + "/config.json", "r")
data = json.load(f)
config = DotMap(**data)

if __name__ == "__main__":
    print(json.dumps(data, indent=2))
