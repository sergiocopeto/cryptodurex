from tradingview_screener import Scanner, Query

from c_screener.columns import Columns

def generate_query(fields,ticker= None, filter=True):
    base_fields = ["base_currency_logoid", "base_currency","base_currency_desc", "update_mode",Columns.CRYPTO_TOTAL_RANK, Columns.CLOSE]
    #columns_to_drop = ["ticker", "base_currency_logoid", "base_currency", "update_mode"]
    #columns_to_drop = ["base_currency_logoid", "base_currency", "update_mode"]
    columns_to_drop = []
    query = Query()
    query.set_markets("coin")
    query.order_by(Columns.CRYPTO_TOTAL_RANK, ascending=True)
    query.query["columns"] = base_fields + fields
    if ticker:
        query.set_tickers("CRYPTO:"+ticker.upper()+"USD")
    query.limit(300)
    results = query.get_scanner_data(verify=False)
    to_return = results[1]
    to_return_filtered = to_return.drop(columns_to_drop,axis=1)
    return to_return_filtered if filter else to_return