# SQL Insights Agent 

# LLM-Powered SQL Insights Agent

A conversational analytics tool that transforms natural language business questions into executable SQL queries and interactive visualizations. This project serves as a portfolio piece demonstrating an end-to-end implementation of a production-style GenAI application.

## Key Features

* **Natural Language to SQL:** Ask questions like "What was our monthly revenue last year?" and get a validated SQL query.
* **Automated Visualization:** Automatically generates interactive Plotly charts from the SQL query results.
* **Schema-Aware RAG:** Uses a vector database (Chroma) to provide the LLM with relevant table and column context, improving query accuracy.
* **Safety & Guardrails:** Implements checks to ensure only safe, `SELECT`-only queries are executed against the database.
* **Cloud-Ready:** The entire application is containerized with Docker and designed for deployment on AWS using Terraform.

## Tech Stack

| Layer                 | Technology                               |
| --------------------- | ---------------------------------------- |
| **UI & Application** | Streamlit, Python 3.11                   |
| **LLM Orchestration** | LangChain, OpenAI (GPT-4o)               |
| **Data Warehouse** | PostgreSQL (running in Docker)           |
| **Data Modeling** | dbt Core                                 |
| **Retrieval (RAG)** | ChromaDB, Sentence-Transformers          |
| **Deployment & IaC** | Docker, AWS (ECS, RDS), Terraform        |
| **Observability** | Langfuse                                 |

## Getting Started

*(This section will be filled out later with instructions on how to run the project locally.)*