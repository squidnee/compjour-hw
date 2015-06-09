# Total number of wildlife strike incidents reported at San Francisco International Airport.

import pandas as pd
data = pd.read_csv('http://wildlife.faa.gov/downloads/fieldlist.xls')
print(len(data))