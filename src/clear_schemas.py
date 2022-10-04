import json
from config import Config

config = Config()
client = config.get_client()

# delete all classes
client.schema.delete_all()

schema = client.schema.get()
print(json.dumps(schema))
