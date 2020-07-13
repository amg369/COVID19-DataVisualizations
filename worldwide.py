import matplotlib.pyplot as plt
import numpy as np

# Top Ten Countries by Thousands of COVID Cases

# Function to show case numbers as a label above each bar
def CreateLabels(data):
    for item in data:
        height = str(item.get_height())
        print(height)
        plt.text(item.get_x() + item.get_width() / 2., float(height)*1.00, height, ha='center', va='bottom')


col_count = 1
bar_width = .1

country = {"USA": 3.304, "Brazil": 1.864, "India": .878, "Russia": .726, "Peru": .326,
           "Chile": .315, "Mexico": .299, "UK": .291, "South Africa": .276, "Iran": .257}

index = np.arange(col_count)

# Make the bars
b = 0
for key in sorted(country):
    bars = plt.bar(index + b, country[key], bar_width, label=key, alpha=.6)
    b = b + .1
    CreateLabels(bars)


# Axis Labels and Legend
plt.xticks([])
plt.title("Worldwide COVID-19 Cases")
plt.xlabel("Countries")
plt.ylabel("Cases by Millions")
plt.grid(True)
plt.legend(edgecolor=None, shadow=False)
plt.show()
