import json
from config import Config

config = Config()
client = config.get_client()

schema = client.schema.get()
print(json.dumps(schema, indent=4))
results = client.data_object.get()
print(json.dumps(results, indent=4))
