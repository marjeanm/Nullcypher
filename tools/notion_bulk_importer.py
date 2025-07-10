import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_page(title, category, tags, softday, purpose, content):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Title": {
                "title": [{ "text": { "content": title } }]
            },
            "Category": {
                "select": { "name": category }
            },
            "Tags": {
                "multi_select": [{"name": tag.strip()} for tag in tags.split(",")]
            },
            "Softday Relevant": {
                "checkbox": softday
            },
            "Purpose": {
                "rich_text": [{ "text": { "content": purpose } }]
            }
        },
        "children": [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{ "type": "text", "text": { "content": content } }]
            }
        }]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to create page for: {title}")
