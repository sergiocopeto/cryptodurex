import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query
st.set_page_config(page_title="Market Overview", layout="wide")

st.write("# TREND 👋")
page_columns = [
    Columns.RECOMMEND_ALL,
    Columns.RECOMMEND_MA,
    Columns.RECOMMEND_OTHER,
    Columns.RECOMMENDATION_BUY,
    Columns.RECOMMENDATION_HOLD,
    Columns.RECOMMENDATION_TOTAL
]

results = generate_query(page_columns)
st.dataframe(results)