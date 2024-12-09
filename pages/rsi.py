import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query
st.set_page_config(page_title="Market Overview", layout="wide")

st.write("# RSI 👋")
page_columns = [
    Columns.RSI_240,
    Columns.RSI_1__240,
    Columns.RSI_1,
    Columns.RSI_1__1W,
]

results = generate_query(page_columns)
st.dataframe(results)