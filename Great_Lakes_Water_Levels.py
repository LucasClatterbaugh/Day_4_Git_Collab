"""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
"""
#=======
# +

## To use this notebook for your in-class assignment, you will need these 
## files, which you shoujld have downloaded:
## * mhu.csv -- Lake Michigan and Lake Huron
## * sup.csv -- Lake Superior
## * eri.csv -- Lake Erie
## * ont.csv -- Lake Ontario

## As instructed in the in-class activity notebook for today, you are 
## only expected to complete one PART below. Do not worry if your group 
## is not big enough to finish all parts below, but if you have extra 
## time, you're welcome to do so.

# Merrick
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years
mhu = pd.read_csv("mhu.csv")
plt.plot(mhu["time"],mhu["lake average"])
plt.xlabel("Year")
plt.ylabel("Water Level")
plt.title("Lake Michigan/Huron Water Level")


# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
## Beans
# -

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

Erie = pd.read_csv('eri.csv')
Erie_time = Erie['time']
Erie_water = Erie['water level']
plt.plot(Erie_time,Erie_water)
plt.xlabel('Time')
plt.ylabel('Water Level')

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ont.csv')
data
plt.plot(data['year'], data['Lake Ontario annual averages'])
plt.xlabel('Year')
plt.ylabel('Lake Ontario annual averages')
# -

# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.
Mi = pd.read_csv('mhu.csv')
Su = pd.read_csv('sup.csv')
plt.plot(Mi)
plt.plot(Su)


# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


