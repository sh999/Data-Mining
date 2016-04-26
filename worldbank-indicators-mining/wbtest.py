import wbdata
import datetime
countries = [i['id'] for i in wbdata.get_country(incomelevel="OEC", display=False)]
indicators = {"SP.URB.TOTL.IN.ZS": "urban%", "NY.GDP.PCAP.PP.KD": "gdppc"}
#indicators = {"NY.GDP.PCAP.PP.KD": "gdppc"}
data_date = (datetime.datetime(2010,1,1), datetime.datetime(2011,1,1))
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True, data_date=data_date)
print (df.describe())
print ("lol")