import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query
st.set_page_config(page_title="Market Overview", layout="wide")

st.write("# Market Overview 👋")
page_columns = [
    Columns.DAILY_CLOSE_CHANGE_5,
    Columns.PERF_W,
    Columns.PERF_1M,
    Columns.PERF_3M,
    Columns.PERF_6M,
    Columns.PERF_Y
]

results = generate_query(page_columns)
st.dataframe(results)