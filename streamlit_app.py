import streamlit as st
import pandas as pd

from query_engine import run_query

df = pd.read_csv("data/mutual_funds.csv")

st.title("📈 Mutual Fund Screener")
st.write("Filter mutual funds using custom queries.")

st.subheader("Examples")

st.code("""
category == Flexi Cap
return_3y > 18
category == Flexi Cap AND expense_ratio < 0.7
""")

query = st.text_input("Enter Query")

if st.button("Search"):

    result = run_query(df, query)

    if result is not None:
        st.dataframe(result)