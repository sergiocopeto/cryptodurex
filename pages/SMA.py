import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query
st.set_page_config(page_title="Market Overview", layout="wide")

st.write("# SMA 👋")
page_columns = [
    Columns.SMA50_240,
    Columns.SMA100_240,
    Columns.SMA200_240,
    Columns.SMA10,
    Columns.SMA50,
    Columns.SMA100,
    Columns.SMA200,
]

results = generate_query(page_columns)
st.dataframe(results)