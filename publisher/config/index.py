import os
import json


p = os.path.join(os.path.dirname(__file__), "config.json")
config = json.load(open(p))
