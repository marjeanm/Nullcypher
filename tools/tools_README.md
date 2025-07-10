# 🛠️ NullCypher Tools – Notion Bulk Importer

This folder contains utility scripts used to support the development, documentation, and integration pipelines of the **NullCypher Generative AI Assistant**.

---

## 📥 Script: `notion_bulk_importer_dotenv.py`

### 🔐 Purpose:
Pushes all your structured `.md` project files directly into a Notion database using the Notion API.

Each Markdown file should include a YAML-style metadata block like:

```yaml
---
title: SOP: Memory Chunk Ingestion
category: sop
priority: Medium
softday_relevant: True
status: Planned
owner: Marjean
tags: [nullcypher, foundation, sop]
---
```

This metadata is extracted and mapped to your Notion database fields.

---

## 🚀 How to Use

### 1. 🧪 Install dependencies

```bash
pip install python-dotenv requests
```

### 2. 🔑 Create a `.env` file in your project root:

```
NOTION_TOKEN=secret_your_token_here
DATABASE_ID=your_database_id_here
```

> Note: Your token must be from a Notion integration with access to your workspace.
> Share your database with the integration manually from Notion’s **Share** menu.

---

### 3. 📂 Update the script

Edit the last line in the script to point to your markdown directory:

```python
bulk_upload_markdown("L:/Nullcypher/docs")  # Example path
```

---

### 4. ▶️ Run the script

```bash
python tools/notion_bulk_importer_dotenv.py
```

Each `.md` file will create a page in your Notion DB with:
- Title
- Category
- Tags
- Softday flag
- Purpose
- Body content

---

## 🛡 Security Notes

- Your `.env` should be included in `.gitignore`
- Never commit your Notion token to GitHub or public repos

---

## 🧰 Coming Soon

- Blog/Journal sync tool
- Notion-to-local file exporter
- Audit tracker for training memory consistency

---

Built for **Project NullCypher** by Marjean Mayo-Baker 🛡️
