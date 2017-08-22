# -*- coding: utf-8 -*-
from coinmarketcap import Market
import pandas as pd
coinmarketcap = Market()
res = coinmarketcap.ticker(convert='CNY')
#labels = ['market_cap_usd', 'percent_change_1h', 'id', 'available_supply', 'name', '24h_volume_usd', 'total_supply', 'symbol', 'price_cny', 'price_btc', 'market_cap_cny', 'percent_change_24h', 'percent_change_7d', '24h_volume_cny', 'last_updated', 'rank', 'price_usd']
labels = ['rank', 'name', 'market_cap_cny', 'price_cny', 'available_supply', '24h_volume_cny', 'percent_change_24h']
df = pd.DataFrame.from_records(res, columns=labels)
df.rename(columns = {'rank':'排名', 'name':'币种','market_cap_cny':'市值', 'price_cny':'价格', 'available_supply':'流通数', '24h_volume_cny':'24小时成交量', 'percent_change_24h':'24小时涨跌'}, inplace=True)
df.to_csv('/static/data/data.csv', index=False)
