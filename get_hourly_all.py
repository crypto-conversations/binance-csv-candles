# Original file: https://github.com/carlfarterson/token-sets/blob/master/data/prices.py

# Code to fetch OHLCV data used for backtests
import pandas as pd

import os.path

from datetime import datetime, timedelta

import ccxt
import time
import json
import pathlib

pathlib.Path('./data/binance').mkdir(parents=True, exist_ok=True)

binance = ccxt.binance()

def now():
  return datetime.now().timestamp() * 1000

def human_time(t):
  return datetime.fromtimestamp(t/1000)

print('now:', human_time(now()))

def market_loop(ticker, filename):
  # binance was created in 2017, so it should do
  start_date = datetime(year=2015, month=1, day=1, hour=0).timestamp() * 1000

  df_old = pd.DataFrame()
  df = []

  file_exists = os.path.isfile(filename)
  if file_exists:
    df_old = pd.read_csv(filename)
    start_date = df_old['date'].iat[-1] + (3600 * 1000) # next candle open time
    print(ticker, len(df_old), '🕯, last open candle is at', human_time(df_old['date'].iat[-1]), '👉 next start_date', human_time((start_date)))
  else:
    print(ticker, '👉 next start_date', human_time((start_date)))


  # Run until now
  while start_date < now():

      # Fetch 500 hours of OHLCV data
      data = binance.fetch_ohlcv(
          ticker,
          '1h',
          limit=500,
          since=int(start_date)
      )

      # Add results to master list
      df.extend(data)

      # Determine the last hour of OHLCV data pulled
      last_hour_pulled = data[-1][0]

      print('✅ %2.f' % (100 * ((now() - start_date) / (1000 * 3600 * 24))))

      # Increment last hour pulled by an hour for our next set of 500 hourly OHLCV data
      start_date = last_hour_pulled + (3600 * 1000)

      # Pause to prevent reaching an API limit
      time.sleep(.1)

  df = pd.DataFrame(df, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
  # Combine and save
  df_all = df_old.append(df, ignore_index=True)
  df_all.to_csv(filename, index=False)

# load all binance markets
markets = binance.load_markets()
market_ids = []
for symbol in markets:
  m = markets[symbol]
  if m['quote'] in ['BTC', 'ETH', 'USDT'] and m['active']:
    market_ids.append(symbol)

print(len(market_ids), '🚀')
#print(json.dumps(markets['ETH/BTC'], indent=4))

for ticker in market_ids:
  filename = f"data/binance/{ticker.replace('/', '-')}.csv"
  market_loop(ticker=ticker, filename=filename)