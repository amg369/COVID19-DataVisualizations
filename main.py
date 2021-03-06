import matplotlib.pyplot as plt

# US Coronavirus Cases for the month of June
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

cases = [1.790, 1.810, 1.832, 1.853, 1.876, 1.897, 1.915, 1.932, 1.949, 1.969, 1.987, 2.011, 2.037, 2.059, 2.077,
         2.100, 2.124, 2.151, 2.182, 2.213, 2.242, 2.268, 2.301, 2.339, 2.378, 2.423, 2.467, 2.507, 2.544, 2.588]

deaths = [.0984, .0995, .100, .101, .1022, .1029, .1034, .1039, .1048, .1057, .1065, .1076, .1079, .1083, .1086, .1094,
          .1101, .1108, .1115, .1120, .1123, .1126, .1134, .1141, .1147, .1153, .1158, .1160, .1164, .1170]

# Line for cases 
plt.plot(days, cases, color=(234 / 255, 65 / 255, 178 / 255))

# Line for deaths
plt.plot(days, deaths, color=(.23, .75, .84))

# Labels
plt.ylabel("Cases by millions")
plt.xlabel("Day of June")

plt.title("US Coronavirus Cases in June")

plt.show()


