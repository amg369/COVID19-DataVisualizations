import matplotlib.pyplot as plt
import pandas as pd
# Difference between March COVID Case Numbers and June Case Numbers by State
raw_data = {'States': ["California", "Florida", "Texas", "New York", "New Jersey", "Illinois", "Arizona", "Georgia",
                       "Massachusetts", "Pennsylvania"],
            'Mar': [8155, 6741, 3266, 83712, 22255, 5994, 1289, 4117, 6620, 4843],
            'Apr': [50442, 33690, 28087, 308314, 121190, 52918, 7648, 26260, 62205, 45763],
            'May': [113006, 56163, 64287, 371711, 160918, 120260, 19936, 47063, 96965, 71926],
            'Jun': [232657, 152434, 159986, 394079, 171928, 143185, 79215, 81291, 108802, 86606],
            }

df = pd.DataFrame(raw_data, columns=['States', 'Mar', 'Apr', 'May', 'Jun'])
color = [(.3, .2, .7), (.99, .5, .2), (.4, .7, .4), (.34, .45, .9), (.6, .33, .8), (.9, .4, .4), (.4, .7, .9),
         (.8, .17, .4), (.76, .63, .9), (.2, .4, .1)]

# Make pie chart
df['inc'] = df['Jun'] - df['Mar']
plt.pie(df['inc'], labels=df['States'], colors=color)
plt.show()
