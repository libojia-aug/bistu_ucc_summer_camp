#how many days did the close price of facebook go up and the one of apple go down?
import pandas as pd
import matplotlib.pyplot as plt
facebook = pd.read_csv("./fb_us_d.csv",index_col="Date",parse_dates=["Date"])
apple = pd.read_csv("./aapl.csv",index_col="date",parse_dates=["date"])

al = pd.concat([facebook, apple], axis=1)
# print al["2018-06-01":]
# facebook_up = facebook[(facebook["Close"]-facebook["Open"])>0]
# print facebook_up
# apple_down = apple[(apple["open"]-apple["close"])>0]
# print apple_down
facebook_up_apple_down = al[((al["Close"]-al["Open"])>0) & ((al["open"]-al["close"])>0)]
print facebook_up_apple_down
print len(facebook_up_apple_down)

print al.corr()

# al_close = al["Close","close"]
# print al_close.corr()

al.plot.scatter("Close","close")
plt.show()

