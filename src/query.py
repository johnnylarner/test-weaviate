from config import Config

config = Config()
client = config.get_client()

where_filter = {"operator": "Equal", "valueString": "Vogue", "path": ["name"]}

query_result = client.query.get("Publication", ["name"]).with_where(where_filter).do()
print(query_result)
