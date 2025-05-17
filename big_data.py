import meilisearch
import json

# Connect to MeiliSearch
client = meilisearch.Client('http://localhost:7700', '_r0BYxHVyU7qvaNaedwC0fr9As-fFrgGFYv52hL8IFQ')
index = client.index('products')

# Optional: Make product_category searchable
index.update_searchable_attributes(["product_category", "product_clicked", "country", "gender"])

# Load and add documents
with open('dataset.json', encoding='utf-8') as f:
    products = json.load(f)

response = index.add_documents(products)
print("Documents added. Update ID:", response.status)

# ✅ Corrected multi-search
multi_query = [
    {"indexUid": "products", "q": "Electronics"},
    {"indexUid": "products", "q": "Beauty"}
]

results = client.multi_search(multi_query)
print(json.dumps(results, indent=2))
