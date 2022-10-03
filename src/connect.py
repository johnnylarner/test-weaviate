import weaviate
import json
from config import Config

config = Config()
client = config.get_client()

schema = client.schema.get()
print(json.dumps(schema))
