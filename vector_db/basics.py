import chromadb

client = chromadb.Client()
collection = client.create_collection("news_articles")

collection.add(
    ids=["id1", "id2", "id3", "id4"],
    documents=[
        "Thoroughly work over the materials in your mind. During this stage, you examine what you have learned by looking at the facts from different angles and experimenting with fitting various ideas together.",
        "Step away from the problem. Next, you put the problem completely out of your mind and go do something else that excites you and energizes you.",
        "Let your idea return to you. At some point, but only after you have stopped thinking about it, your idea will come back to you with a flash of insight and renewed energy.",
        "Shape and develop your idea based on feedback. For any idea to succeed, you must release it out into the world, submit it to criticism, and adapt it as needed."
    ]
)

# Get data + embeddings
data=collection.get(
    include=["documents","embeddings", "metadata"]
)

# Get embeddings
for i, emb in enumerate(data["embeddings"]):
    print(f"\nDocument {i+1}")
    print("Text:", data["documents"][i])
    print("Embedding length:", len(emb))
    print("First 10 values:", emb[:10])