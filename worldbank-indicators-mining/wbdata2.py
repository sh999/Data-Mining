# -*- coding: utf-8 -*-
"""
Decision tree with many indicators
"""
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO  
import pydotplus
from IPython.display import Image 
import datetime
import wbdata
import numpy as np
import pandas as pd

# Createa a pandas.dataframe from wbdata, which is restricted by the given
# date and indicators
indicators = {
              "EN.ATM.CO2E.PC": "co2",
              "GC.DOD.TOTL.GD.ZS": "debt",
              "SE.ENR.TERT.FM.ZS": "gender edu",
              "SI.DST.10TH.10": "topincome"
              }   
data_date = (datetime.datetime(2011,1,1), datetime.datetime(2011,1,1))  # Only year 2011
df = wbdata.get_dataframe(indicators, 
                          country="all", 
                          convert_date=True, 
                          data_date=data_date)
df = df.fillna(df.mean())   # replace missing values with mean
print ("All data:")
dfgdp = wbdata.get_dataframe({"NY.GDP.PCAP.PP.KD": "gdppc"}, 
                             country="all", 
                             convert_date=True, 
                             data_date=data_date)
gdp_numeric = df.values
gdp_numeric = gdp_numeric.tolist()
gdp_numeric = [i[0] for i in gdp_numeric]
#print (gdp_numeric)  
# The quartile values below are found by finding quartile info from df.describe()
q1 = 5000
q2 = 15000
q3 = 20000
q4 = 150000
gdp_classes = np.array(gdp_numeric)
bin_labels = ['q1','q2','q3','q4']
gdp_classes = pd.cut(gdp_numeric,[-0.1,q1,q2,q3,q4],labels=bin_labels)
print(gdp_classes)
gdp_classes = [i for i in gdp_classes]
print("classes:",gdp_classes)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(df.values, gdp_classes)
with open("iris2.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
''' 
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf") 
'''

fnames = ['gdpval']
cnames = bin_labels
# Below is colored printing
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=fnames,  
                         class_names=cnames,  
                         filled=True, rounded=True,  
                         special_characters=True) 

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
#in console, do:
#Image(graph.create_png()) 
#then just right click and save png