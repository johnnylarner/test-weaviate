from typing import Dict, List, TypedDict


props: List[Dict] = [
    {
        "class": "Author",  # Map to subject node
        "properties": {
            "dataType": ["Publication"],  # Map to object node
            "name": "writesFor",
        },
    },
    {"class": "Author", "properties": {"dataType": ["Author"], "name": "has"}},
]
