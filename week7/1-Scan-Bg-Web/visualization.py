import matplotlib.pyplot as plt
from scan_bg_web import ScanBgWeb


web = ScanBgWeb('http://register.start.bg')
web.get_statistics()
h = web.histogram.get_dict()
keys = list(h.keys())
values = list(h.values())
X = list(range(len(keys)))
plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")
