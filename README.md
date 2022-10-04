# The Weaviate Tutorial
Weaviate is an open source vector-based search engine.
This repository is an example of how to complete the Weaviate tutorial found here: https://weaviate.io/developers/weaviate/current/getting-started/index.html

# How to interact with the repo

## Prequisites
- Docker and docker compose are installed on your local machine.
- Python 3 is installed on your machine.

## Steps
1. Launch the local weaviate cluster. Navigate to the __docker-compose__ folder and enter:
`docker-compose up -d && docker-compose logs -f weaviate`

2. While the containers are booting up, return to the root directory and create virtual environment:
  - Unix: `python3 -m venv venv && source venv/bin/active && pip3 install -r requirements.txt`
  - Windows: `python -m venv venv && source .\venv\Scripts\Active && pip install -r requirements.txt`

3. By now your docker containers should be running; test this by opening your browser and entering:
`http://[::]:8080/v1`
If you can see some unreadable JSON content, then you're in the right place.

4. Test your connection via the Python client. Navigate to the `src` folder and execute the file from your terminal: `connect.py`.
If your test was successful, you'll see an empty dictionary printed to the terminal.

5. To add schemas to your weaviate instance, execute from your terminal the file: `update_schemas.py`. (You can clear your schemas by running `clear_schemas.py`).

6. To enrich the schema with new properties, run the `add_props.py` file.

7. Now let's import data: run the `import.py` file.

8. View the results by naviagting to: `http://[::]:8080/v1/objects`
