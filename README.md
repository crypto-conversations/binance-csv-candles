# binance-csv-candles

Create/update hourly candles csv files. Files are stored in `./data/binance`

```python
python get_hourly_all.py
```

Each csv file contains 5 columns:
* date (unix timestamp),
* open,
* high,
* low,
* close,
* volume