import json
from config import Config
from new_props import props
from weaviate.exceptions import UnexpectedStatusCodeException

config = Config()
client = config.get_client()

for p in props:
    object_class = p.get("class", "")
    new_prop = p.get("properties", {})
    try:
        # Add the property
        client.schema.property.create(object_class, new_prop)
    except UnexpectedStatusCodeException:
        print(f"Object class {object_class} already has property `{new_prop['name']}`")


# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=2))
