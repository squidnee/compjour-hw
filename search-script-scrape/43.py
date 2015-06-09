# The number of citations that resulted from FDA inspections in fiscal year 2012.

import pandas as pd
csv = 'http://www.fda.gov/downloads/ICECI/Inspections/UCM346093.csv'
f = pd.read_csv(csv)
print(len(f))