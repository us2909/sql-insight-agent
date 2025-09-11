import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

# LangChain Imports
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase 
# --- SETUP ---
load_dotenv()

# --- UI CONFIGURATION ---
st.set_page_config(page_title="AI SQL Insights", layout="wide")
st.title("🤖 AI-Powered Business Insights")
st.write("Ask a question about your business data, and the AI will generate a SQL query and an answer.")

# --- AGENT LOGIC ---
def get_sql_agent():
    """Initializes and returns the LangChain SQL Agent."""
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    database_url = os.getenv("DATABASE_URL")

    if not openai_api_key or not database_url:
        st.error("🚨 Please make sure your OPENAI_API_KEY and DATABASE_URL are set in the .env file.")
        st.stop()
        
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=openai_api_key
    )

    db_engine = create_engine(database_url)
    
    # --- CHANGE IS HERE ---
    # 1. Wrap the engine in the SQLDatabase utility class
    db = SQLDatabase(db_engine)
    
    # 2. Pass the wrapped db object to the agent
    agent_executor = create_sql_agent(
        llm=llm,
        db=db, # <-- Use the wrapped db object
        agent_type="openai-tools",
        verbose=True,
        table_names=["dim_customers", "stg_orders"]
    )
    return agent_executor

# --- MAIN APP FLOW ---
user_question = st.text_input("Ask your question:", placeholder="How many customers are in the UK?")

if user_question:
    with st.spinner("The AI is thinking..."):
        try:
            sql_agent = get_sql_agent()
            response = sql_agent.invoke({"input": user_question})
            
            st.success("Here's the answer:")
            st.write(response["output"])

            with st.expander("Show Generated SQL"):
                sql_query = ""
                for step in response.get("intermediate_steps", []):
                    if "sql_cmd" in step[0].tool_input:
                        sql_query = step[0].tool_input["sql_cmd"]
                        break
                st.code(sql_query, language="sql")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")