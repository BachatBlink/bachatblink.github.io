import os
import json
import requests

API_KEY = os.environ.get("CLICKWISE_API_KEY")
headers = {"X-API-Key": API_KEY}

# Pulls products from your approved Clickwise programs
url = "https://partners.clickwise.net/api/v1/publisher/products/?limit=50"
response = requests.get(url, headers=headers)

products = []
if response.status_code == 200:
    data = response.json()
    items = data.get("results", data if isinstance(data, list) else [])
    for item in items:
        products.append({
            "title": item.get("title"),
            "price": item.get("price"),
            "image": item.get("image"),
            "merchant": item.get("merchant_name"),
            "affiliate_url": item.get("url")
        })

os.makedirs("data", exist_ok=True)
with open("data/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
