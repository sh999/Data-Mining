'''
gdp per capita conversion to low, med,  hi
'''

import wbdata
import pandas as pd
import datetime
import numpy as np
#countries = [i['id'] for i in wbdata.get_country(incomelevel="all", display=False)]
#countries = [i['id'] for i in wbdata.get_country(country_id=None, display=False)]
countries = "all"
indicators = {"NY.GDP.PCAP.PP.KD": "gdppc"}
#indicators = {"NY.GDP.PCAP.PP.KD": "gdppc"}
data_date = (datetime.datetime(2011,1,1), datetime.datetime(2011,1,1))
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True, data_date=data_date)
df = df.fillna(df.mean())   # replace missing values with mean
print ("All data:")
gdp_numeric = df.values
gdp_numeric = gdp_numeric.tolist()
gdp_numeric = [i[0] for i in gdp_numeric]
print (gdp_numeric)  
print ("All GDP numeric values:")
print (df.describe()) 
q1 = 5000
q2 = 15000
q3 = 20000
q4 = 150000
#a = [i for i in range(0,10)]
a = gdp_numeric

gdp_classes = np.array(gdp_numeric)
bin_labels = ['q1','q2','q3','q4']
gdp_classes = pd.cut(gdp_numeric,[-0.1,q1,q2,q3,q4],labels=bin_labels)
print(gdp_classes)
gdp_classes = [i for i in gdp_classes]
print("classes:",gdp_classes)