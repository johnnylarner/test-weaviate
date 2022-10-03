from config import Config
import json

config = Config()
client = config.get_client()
schema = client.schema.get()
existing_classes = set()

for cls in schema["classes"]:
    existing_classes.add(cls["class"])

with open("tmp/data.json") as f:
    data: dict = json.load(f)

client.batch.configure(
    batch_size=len(list(data.keys())), dynamic=True, timeout_retries=3, callback=None
)


class ImportNotSchematizedClassException(Exception):
    pass


def capitalize_and_singularize(word: str) -> str:
    if word.endswith("ies"):
        return f"{ word[:-3] }y".capitalize()
    if word.endswith("s"):
        return word[:-1].capitalize()
    return word.capitalize()


for cls in data:
    print("Importing data for class: ", cls)
    class_in_schema = capitalize_and_singularize(cls)
    if class_in_schema not in existing_classes:
        raise ImportNotSchematizedClassException(
            f"Class `{class_in_schema}` not in schema: {existing_classes}"
        )

    data_objects_per_class = data[cls]
    for data_obj in data_objects_per_class:
        props = {k: v for k, v in data_obj.items() if k not in {"id", "vector"}}
        print("Importing data object: \n", props)
        client.batch.add_data_object(
            props,
            class_in_schema,
            data_obj["id"],
            data_obj["vector"],
        )

client.batch.flush()
