# -*- coding: utf-8 -*-
"""
Decision tree using scikit and iris data
Reference:
    http://scikit-learn.org/stable/modules/tree.html
Nothing really changed from the tutorial
This works by installing pydotplus
regular pydot didn't allow printing of tree
"""
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO  
import pydotplus
from IPython.display import Image 
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
with open("iris2.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
''' 
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf") 
'''
# Below is colored printing
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True) 

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
#in console, do:
#Image(graph.create_png()) 
#then just right click and save png