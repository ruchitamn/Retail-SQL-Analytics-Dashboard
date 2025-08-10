import streamlit as st
import pandas as pd
from db_connect import get_connection
from queries import queries

st.title("Retail SQL Analytics Dashboard")

# Dropdown to select an insight
selected = st.selectbox("Choose an Insight to Run", list(queries.keys()))

# Button to run the query
if st.button("Run"):
    with st.spinner("Fetching results..."):
        try:
            # Establish connection
            conn = get_connection()
            
            # Run the selected query and fetch result
            df = pd.read_sql(queries[selected], conn)
            conn.close()

            # Show how many rows are returned
            st.write("Returned rows:", len(df))

            # Display results in a table
            st.dataframe(df)

        except Exception as e:
            st.error(f"An error occurred: {e}")
