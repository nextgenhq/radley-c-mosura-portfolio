import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from google.cloud import bigquery
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Lead Analytics Agent", page_icon="📊")
st.title("📊 Lead Analytics AI Assistant")
st.write("Ask any question about your BigQuery leads in plain English!")

# 1. Setup BigQuery Execution Tool (LangChain Core)
@tool
def execute_bigquery_sql(sql_query: str) -> str:
    """Executes a SQL query against BigQuery."""
    client = bigquery.Client(project="project-abcf14c5-b467-4586-839")
    query_job = client.query(sql_query)
    results = [dict(row) for row in query_job.result()]
    return str(results[:15])

# 2. Dynamic Schema Fetching & LangGraph Initialization
@st.cache_resource
def get_agent():
    client = bigquery.Client(project="project-abcf14c5-b467-4586-839")
    table = client.get_table("project-abcf14c5-b467-4586-839.leads_analytics.raw_leads")
    schema_info = ", ".join([f"`{field.name}` ({field.field_type})" for field in table.schema])
    
    tools = [execute_bigquery_sql]
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        project="project-abcf14c5-b467-4586-839",
        location="us-central1",
        temperature=0
    )
    
    agent_app = create_react_agent(llm, tools)
    return agent_app, schema_info

agent_app, schema_info = get_agent()

# 3. Streamlit Interface & Execution Loop
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("e.g., How many businesses in Santa Rosa don't have a website?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing BigQuery data via LangGraph ReAct Agent..."):
            user_prompt = (
                f"You are querying BigQuery table: `project-abcf14c5-b467-4586-839.leads_analytics.raw_leads`\n\n"
                f"Table Schema Fields:\n{schema_info}\n\n"
                f"User Question: {prompt}\n\n"
                f"SQL RULES:\n"
                f"- Query strictly from `project-abcf14c5-b467-4586-839.leads_analytics.raw_leads`.\n"
                f"- Wrap column names in backticks (e.g., `Website URL`, `City`).\n"
                f"- For missing websites, check: (`Website URL` IS NULL OR `Website URL` = '' OR LOWER(`Website URL`) LIKE '%none%' OR LOWER(`Website URL`) LIKE '%n/a%')\n"
                f"- Treat 'santa rosa', 'sta rosa', and 'sta.rosa' identically using `LOWER(City) LIKE '%santa rosa%' OR LOWER(City) LIKE '%sta%rosa%'`.\n\n"
                f"FINAL RESPONSE RULE:\n"
                f"- Call `execute_bigquery_sql` to fetch data.\n"
                f"- Read the output data and synthesize it into a complete, plain-English summary. Never output raw dictionaries or lists.\n"
            )
            result = agent_app.invoke({"messages": [("user", user_prompt)]})
            
            def extract_text(content):
                if isinstance(content, str):
                    return content
                if isinstance(content, list):
                    texts = []
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            texts.append(item.get("text", ""))
                    return " ".join(texts)
                return str(content)

            response_text = ""
            for msg in reversed(result["messages"]):
                if hasattr(msg, "content") and msg.content:
                    if getattr(msg, "type", "") == "tool":
                        continue
                    cleaned = extract_text(msg.content)
                    if cleaned.strip():
                        response_text = cleaned
                        break

            if not response_text:
                response_text = "Query executed successfully, but could not format text summary."

            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
