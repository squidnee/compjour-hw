# The number of U.S. congressmembers who have Twitter accounts,
# according to Sunlight Foundation data.`

import pandas as pd
data = pd.read_csv('http://unitedstates.sunlightfoundation.com/legislators/legislators.csv')
count=data.count()
print(count.loc['twitter_id'])