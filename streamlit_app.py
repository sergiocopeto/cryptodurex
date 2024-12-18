import streamlit as st
from tradingview_screener import Query

from c_screener.columns import Columns
from c_screener.generate_query import generate_query

def write_stuff(text, color = None, title = 0):
    to_write = []
    if title > 0:
        for i in range(title):
            to_write.append("#")
        to_write.append(" ")
    if color:
        to_write.append(":"+color+"[")
    to_write.append(text)
    if color:
        to_write.append("]")
    final_string = "".join(text for text in to_write)
    print(final_string)
    st.markdown(final_string)

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


# Using "with" notation

st.write("### Market Overview")

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

results_all = generate_query(page_columns)

step = 20

def next_button(start, step):
    start = start + step


pageno = st.number_input(label="PAGE",min_value=1)


results = results_all.iloc[step*(pageno - 1) : step*(pageno - 1) + step]

t0, t1, t2, t3 = st.columns(4)
with t0:
    st.write("## Coin")
with t1:
    st.write("## Price")
with t2:
    st.write("## Week Performance")
with t3:
    st.write("## 6 Month Performance")


#"https://s3-symbol-logo.tradingview.com/crypto/XTVCBTC.svg"

for i in range(step):
    result = results.iloc[i]
    coin_name = result["base_currency_desc"]
    coin_icon = result["base_currency_logoid"]
    c0, c1, c2, c3, c4, c5 = st.columns(6)
    c0, c1, c2, c5 = st.columns(4)


    with c0:
        #st.metric("", coin_name, "")
        t1, t2 = st.columns((0.25, 0.75))
        with t1:
            st.image("https://s3-symbol-logo.tradingview.com/" + coin_icon + ".svg", width= 200)
        with t2:
            #st.metric("oal", coin_name, label_visibility="hidden" )
            #st.write(" ## " + coin_name)
            write_stuff(coin_name, color=None, title=2)
            #st.markdown("## :red["+coin_name+"]")

    with c1:
        current_price = result["close"]
        price_change = result["24h_close_change|5"]
        #st.metric("Current Price", current_price, price_change)
        write_stuff(str(current_price)+" USD", color=None, title=2)
        #st.write(current_price)

    with c2:
        perf_w = result["Perf.W"]
        color = "green" if perf_w > 0 else "red"
        write_stuff("{:.2f}".format(perf_w) + "%", color=color, title=2)
        #st.metric("Week Performance", perf_w)
        #st.write(perf_w)



    with c5:
        perf = result["Perf.6M"]
        write_stuff("{:.2f}".format(perf) + "%", color=color, title=2)
        #st.metric("6 Month Performance", perf)
        #st.write(perf)
