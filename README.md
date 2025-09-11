# LLM-Powered SQL Insights Agent

A conversational analytics tool that transforms natural language business questions into executable SQL queries and interactive visualizations. This project serves as a portfolio piece demonstrating an end-to-end implementation of a production-style GenAI application.

## Demo


*(**TODO:** Replace this line with a screenshot of your running application. This is the most important part of the README for a portfolio project!)*

## Key Features

* **Natural Language to SQL:** Ask questions like "How many customers are in the UK?" and get a validated SQL query.
* **AI-Powered Answers:** Get direct, synthesized answers to your questions based on the queried data.
* **Data Modeling & Testing:** Uses a `dbt` pipeline to transform raw data into a clean, tested star schema, ensuring data reliability.
* **Cloud-Ready Foundation:** The entire application is containerized with Docker, and the infrastructure is designed to be defined with Terraform for future cloud deployment.

## Tech Stack

| Layer                 | Technology                               |
| --------------------- | ---------------------------------------- |
| **UI & Application** | Streamlit, Python 3.11                   |
| **LLM Orchestration** | LangChain, OpenAI (GPT-4o-mini)          |
| **Data Warehouse** | PostgreSQL (running in Docker)           |
| **Data Modeling** | dbt Core                                 |
| **Deployment** | Docker                                   |

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* Git
* Python 3.11+
* Docker Desktop (must be running)

### 1. Clone the Repository

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git clone [https://github.com/YOUR_USERNAME/sql-insights-agent.git](https://github.com/YOUR_USERNAME/sql-insights-agent.git)
cd sql-insights-agent

### 2. Set Up Environment Variables

1.  Create a file named `.env` in the root of the project.
2.  Add your credentials to this file. It will be ignored by Git.

    ```toml
    DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/mydatabase"
    OPENAI_API_KEY="sk-..."
    ```

### 3. Create Virtual Environment and Install Dependencies

```bash
# Create the virtual environment
# On Windows: python -m venv .venv
python3 -m venv .venv

# Activate the virtual environment
# On Windows: .venv\Scripts\activate
source .venv/bin/activate

# Install all required packages from the project configuration
pip install -e .

### 4. Run Backend Services and Data Pipeline

These commands only need to be run once for the initial setup.

```bash
# 1. Start the PostgreSQL database in Docker (this is one single command)
docker run --name sql-agent-db -d -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydatabase -p 5432:5432 postgres

# 2. Load the raw data into the database from the Excel file
python app/scripts/seed_db.py

# 3. Run the dbt models and tests to transform the raw data
# (You must be inside the dbt_project directory to run this)
cd dbt_project
dbt build
cd ..

### 5. Run the Streamlit Application

```bash
# Make sure you are in the root directory of the project
streamlit run app/app.py
