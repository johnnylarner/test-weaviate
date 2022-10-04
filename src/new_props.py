from typing import Dict, List


props: List[Dict] = [
    {
        "class": "Author",  # Map to subject node
        "properties": {
            "dataType": ["Publication"],  # Map to object node
            "name": "writesFor",
        },
    },
    {"class": "Publication", "properties": {"dataType": ["Author"], "name": "has"}},
]
