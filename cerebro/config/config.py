from dotmap import DotMap
import json

f = open("./config.json", "r")
data = json.load(f)
config = DotMap(**data)
