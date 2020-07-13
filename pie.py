import matplotlib.pyplot as plt

# Top Ten States by Coronavirus Count as of July 13th

states = ["California", "Florida", "Texas", "New York", "New Jersey", "Illinois", "Arizona", "Georgia",
          "Massachusetts", "Pennsylvania"]
# Case Counts
cases = [312344, 250984, 250462, 402861, 174959, 154094, 119930, 114401, 111398, 95266]

# Separation / Emphasis on NY
separated = (0, 0, 0, .3, 0, 0, 0, 0, 0, 0)

plt.pie(cases, labels=states, explode=separated)
plt.axis("equal")
plt.show()
