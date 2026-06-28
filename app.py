import chromadb
chromadb_client = chromadb.Client()

collection_name = "test_collection"
collection = chromadb_client.get_or_create_collection(name=collection_name)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {"id": "doc4", "text": "Hello, again!."},
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query = "Hello, world!"

results = collection.query(query_texts=[query], n_results=3)
print(results)