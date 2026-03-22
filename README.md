# DBMind Agent

Ask your database questions in plain English.

## What it does

- You describe your database schema once (tables, columns, business rules)
- DBMind stores that knowledge using embeddings + pgvector
- You ask questions like "how many users signed up this month?"
- DBMind finds the relevant tables, writes the SQL, runs it, and explains the answer

## Tech

Python · FastAPI · PostgreSQL · pgvector · sentence-transformers · Claude API

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your values
3. Run `pip install -r requirements.txt`
4. Run `python scripts/setup_db.py` to create the vector tables
5. Run `python scripts/ingest_schema.py` to feed your schema
6. Start the server: `uvicorn app.main:app --reload`
7. Ask a question: POST /ask { "question": "find all unpaid orders" }

## Project status

Work in progress — built for backend + AI system design.
