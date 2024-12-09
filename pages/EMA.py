import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query
st.set_page_config(page_title="Market Overview", layout="wide")

st.write("# EMA 👋")
page_columns = [
    Columns.EMA50_240,
    Columns.EMA100_240,
    Columns.EMA200_240,
    Columns.EMA10,
    Columns.EMA50,
    Columns.EMA100,
    Columns.EMA200,
]

results = generate_query(page_columns)
st.dataframe(results)