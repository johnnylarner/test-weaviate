from config import Config
import json
from schemas import schema
from weaviate.exceptions import UnexpectedStatusCodeException

config = Config()
client = config.get_client()

for cl in schema:
    try:
        client.schema.create_class(cl)
    except UnexpectedStatusCodeException:
        print(f"Schema class {cl['class']} already exists.")

schema = client.schema.get()
print("Current schema: \n", json.dumps(schema, indent=4))
