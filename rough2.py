import csv
import pandas as pd 
import numpy as np 
from sklearn.cross_validation import train_test_split
d=pd.read_csv("/home/souny/artivicat/finalll.csv")
'''print(d.shape)
print(d.dtypes)'''


y=finaldata['Response']
X=finaldata.iloc[:,0:113]


x_train, x_test, y_train, y_test =train_test_split(X,y,test_size=0.25)
print("TRaining data: ",x_train.shape)
print("test data: ",x_test.shape)




from sklearn.linear_model import LogisticRegression
lr= LogisticRegression()
lr.fit(x_train, y_train)

#for logistic
y_pred = lr.predict(x_test)
#print(y_pred)

from pandas import DataFrame
df=DataFrame({'actual':y_test,'calculated':y_pred})
print(df)
df.to_excel('output_lr.xlsx', sheet_name='sheet1', index=False)





from sklearn import metrics

mlr=LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(x_train, y_train) 
#for multiomial
y_pred = mlr.predict(x_test)
#print(y_pred)

from pandas import DataFrame
dff=DataFrame({'actual':y_test,'calculated':y_pred})
print(dff)
dff.to_excel('output_mlr.xlsx', sheet_name='sheet1', index=False)


#print("Logistic regression Train Accuracy :: ", metrics.accuracy_score(y_train, lr.predict(x_train)))
print("Logistic regression Test Accuracy :: ", metrics.accuracy_score(y_test, lr.predict(x_test)))
#print("Multinomial Logistic regression Train Accuracy :: ", metrics.accuracy_score(y_train, mul_lr.predict(x_train)))
print("Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score( y_test, mlr.predict(x_test)))


'''from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print("THe confusion matrix: \n",confusion_matrix)'''
