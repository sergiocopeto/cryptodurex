import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query

def write_metrics(df, fields):
    close = df["close"]
    for field in fields:
        value = df[field]
        change = ((close-value)/close)*100
        st.metric(field, value, change)

def write_mtf_metrics(df, fields):
    h4_col, day_col, week_col = st.columns(3)

    with day_col:
        st.write("### Day")
        write_metrics(result, fields)

    h4_fields = [field + "|240" for field in fields]

    with h4_col:
        st.write("### 4H")
        write_metrics(result, h4_fields)


    with week_col:
        st.write("### Week")
        h4_fields = [field + "|1W" for field in fields]
        write_metrics(result, h4_fields)

st.set_page_config(page_title="Coin Metrics", layout="wide")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.write("# Market Overview 👋")

title = st.text_input("Coin", "BTC")


page_columns = [
    Columns.DAILY_CLOSE_CHANGE_5,
    Columns.PERF_W,
    Columns.PERF_1M,
    Columns.PERF_3M,
    Columns.PERF_6M,
    Columns.PERF_Y,
    Columns.EMA8,
    Columns.EMA21,
    Columns.EMA50,
    Columns.EMA100,
    Columns.EMA200,
    Columns.EMA8_240,
    Columns.EMA21_240,
    Columns.EMA50_240,
    Columns.EMA100_240,
    Columns.EMA200_240,
    Columns.EMA8_1W,
    Columns.EMA21_1W,
    Columns.EMA50_1W,
    Columns.EMA100_1W,
    Columns.EMA200_1W,
    Columns.RSI,
    Columns.RSI_240,
    Columns.RSI_1W,
    Columns.RSI_1M
]

results = generate_query(page_columns, ticker=title)
result = results.iloc[0]

#st.dataframe(result, use_container_width=True)

coin_name = result["base_currency_desc"]

st.write(" # " + coin_name)

perf_tab, ema_tab, sma_tab, rsi_tab = st.tabs(["Performance", "EMA", "SMA", "RSI"])
with perf_tab:
    st.write("### Performance")
    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:
        current_price = result["close"]
        price_change = result["24h_close_change|5"]
        st.metric("Current Price", current_price, price_change)

    with c2:
        perf_w = result["Perf.W"]
        st.metric("Week Performance", perf_w)

    with c3:
        perf = result["Perf.1M"]
        st.metric("1 Month Performance", perf)

    with c4:
        perf = result["Perf.3M"]
        st.metric("3 Month Performance", perf)

    with c5:
        perf = result["Perf.6M"]
        st.metric("6 Month Performance", perf)

    with c6:
        perf = result["Perf.Y"]
        st.metric("1 Year Performance", perf)

with ema_tab:
    st.write("### EMAs")
    fields = ["EMA8", "EMA21", "EMA50", "EMA100"]
    write_mtf_metrics(result, fields)

with rsi_tab:
    st.write("### RSI")
    fields = ["RSI"]
    write_mtf_metrics(result,fields)