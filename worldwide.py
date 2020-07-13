import matplotlib.pyplot as plt
import numpy as np

def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height*1.05, '%d' % int(height), ha='center', va='bottom')


# Top Ten Countries by Thousands of COVID Cases
col_count = 1
bar_width = .1

country = {"USA": 3.304, "Brazil": 1.864, "India": .878, "Russia": .726, "Peru": .326,
           "Chile": .315, "Mexico": .299, "UK": .291, "South Africa": .276, "Iran": .257}

index = np.arange(col_count)

b = 0
for key in sorted(country):
    bars = plt.bar(index + b, country[key], bar_width, label=key, alpha=.6)
    b = b + .1
    CreateLabels(bars)



plt.xticks([])
plt.title("Worldwide COVID-19 Cases")
plt.xlabel("Countries")
plt.ylabel("Cases by Millions")
plt.grid(True)
plt.legend(edgecolor=None, shadow=False)
plt.show()
