import pandas as pd
import matplotlib.pyplot as plt

facebook = pd.read_csv("./fb_us_d.csv",index_col="Date",parse_dates=["Date"])

print facebook.tail(10)

facebook_avg = facebook
facebook_avg["avgOC"] = (facebook["Open"]+facebook["Close"])/2.0
print facebook_avg["2018-06-01":]

facebook_avg_los = facebook_avg
facebook_avg["loss"] = facebook["Open"]-facebook["avgOC"]

print facebook_avg[facebook_avg["loss"]>0]
print facebook_avg[facebook_avg["loss"]==0]
print facebook_avg[facebook_avg["loss"]<0]

print "Close price larger than the Open price: " + str(sum(facebook_avg["loss"]>0))
print "Close price equal than the Open price: " + str(sum(facebook_avg["loss"]==0))
print "Close price smaller than the Open price: " + str(sum(facebook_avg["loss"]<0))


facebook_avg_los_show = facebook_avg_los["2018-06-01":]
facebook_avg_los_show["Close"].plot()
facebook_avg_los_show["Open"].plot()
facebook_avg_los_show["avgOC"].plot()
facebook_avg_los_show.plot(y=["Close","Open","avgOC"])
plt.show()