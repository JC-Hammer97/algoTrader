import MetaTrader5 as mt5
from datetime import datetime


# Assign my account ID to a variable
account = int(41008665)

# Initialise connection to MT5
mt5.initialize()
authorized = mt5.login(account)

if authorized:
    print("connected: connecting to MT5 Client")
else:
    print("Failed to connect at account #{},"
          " error code: {}".format(account, mt5.last_error()))

# Set dates to pull data from and then pull that data
# Here we pull euro-dollar data on a 4 hour time frame
utc_from = datetime(2021, 2, 1)
utc_to = datetime(2021, 2, 4)

rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_H4,
                             utc_from, utc_to)

for rate in rates:
    print(rate)

