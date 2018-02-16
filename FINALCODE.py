#Import csv and pandas libraries to read the csv file.
import csv
import pandas as pd

data=pd.read_csv("/home/souny/Desktop/artivatic/Training.csv")
# gives the number of rows and columns in the dataset  
print(data.shape)
#categorical variables
df1=data[['Product_Info_1', 'Product_Info_2', 'Product_Info_3', 'Product_Info_5', 'Product_Info_6', 'Product_Info_7',
 'Employment_Info_2', 'Employment_Info_3', 'Employment_Info_5', 'InsuredInfo_1', 'InsuredInfo_2', 'InsuredInfo_3',
  'InsuredInfo_4', 'InsuredInfo_5', 'InsuredInfo_6', 'InsuredInfo_7', 'Insurance_History_1', 'Insurance_History_2',
   'Insurance_History_3', 'Insurance_History_4', 'Insurance_History_7', 'Insurance_History_8', 'Insurance_History_9',
    'Family_Hist_1', 'Medical_History_2', 'Medical_History_3', 'Medical_History_4', 'Medical_History_5', 'Medical_History_6',
     'Medical_History_7', 'Medical_History_8', 'Medical_History_9', 'Medical_History_11', 'Medical_History_12',
      'Medical_History_13', 'Medical_History_14', 'Medical_History_16', 'Medical_History_17', 'Medical_History_18',
       'Medical_History_19', 'Medical_History_20', 'Medical_History_21', 'Medical_History_22', 'Medical_History_23',
        'Medical_History_25', 'Medical_History_26', 'Medical_History_27', 'Medical_History_28', 'Medical_History_29',
         'Medical_History_30', 'Medical_History_31', 'Medical_History_33', 'Medical_History_34', 'Medical_History_35',
          'Medical_History_36', 'Medical_History_37', 'Medical_History_38', 'Medical_History_39', 'Medical_History_40',
            'Medical_History_41']]
            
#check for number of missing values
print(df1.isnull().sum(axis=0))
#for continous variables
df2=data[['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 'Employment_Info_4', 'Employment_Info_6',
 'Insurance_History_5', 'Family_Hist_2', 'Family_Hist_3', 'Family_Hist_4', 'Family_Hist_5']]
 
#check for number of missing values
print(df2.isnull().sum(axis=0))
#for discrete
df3=data[['Medical_History_1', 'Medical_History_10', 'Medical_History_15', 'Medical_History_24', 'Medical_History_32']]
#check for number of missing values
print(df3.isnull().sum(axis=0))
#for dummy
df4=data.loc[:, 'Medical_Keyword_1':'Medical_Keyword_48']
#check for number of missing values
print(df4.isnull().sum(axis=0))
#Employment_Info_4,Employment_Info_6,Insurance_History_5,Family_Hist_2,Family_Hist_3,Family_Hist_4, Family_Hist_5, Medical_History_1
#,Medical_History_10,Medical_History_15,Medical_History_24,Medical_History_32 -
# beacause these columns have more than 30-40% of the values missing. And replacing them with mean, median
# or mode would affect the accuracy of the model.'''

data= data.drop(['Employment_Info_4','Employment_Info_6','Insurance_History_5',
	'Family_Hist_2','Family_Hist_3','Family_Hist_4','Family_Hist_5','Medical_History_1','Medical_History_10','Medical_History_15',
	'Medical_History_24','Medical_History_32'], axis=1)
 
print(data.columns.values)
#The number of rows with missing values is only a small percent of the whole dataset. So, deleted them instead of replacing as there are good amount of rows to build the model and the model will give accurate results.data2=data.dropna()
data2=data.dropna()
#dataset aftr removing missing values
print(data2.shape)
#the continous variables in the new dataset
d2_cont=data2[['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1']]
print(d2_cont.columns.values)

#checking correlation among the continuous variables
d2_cont.corr()
#Here, Height and Weight are highly correlated with BMI. So removed the height and weight columns as they would not add any value to the model built.(BMI itself explains height and weight)
data_final=data2.drop(['Ht','Wt'],axis=1)
#final dataset after dropping heigt and weight columns.
print(data_final.columns.values)
#DEfine the REsponse variable 'y' and explanatory variables 'X'
y=data_final['Response']
X=data_final.iloc[:,0:113]

print(data_final.shape)
print(X.shape)
#print(X.columns.values)

#Divide the data into train and test data in a ratio 75:25
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test =train_test_split(X,y,test_size=0.25)

print(data_final.shape)
print("TRaining data: ",x_train.shape)
print("test data: ",x_test.shape)

#Logistic Regression Model Building.
from sklearn.linear_model import LogisticRegression
lr= LogisticRegression()
lr.fit(x_train, y_train)

#DEleted the 'Product_Info_2' column because it has discrete values A1-A8,B1-B8,.. . If these values are converted to numeric- say A1-1,A2-2..., the values become relative and the accuracy of the model decreases. 
finaldata=data_final.drop(['Product_Info_2'],axis=1)
print(finaldata.columns.values)

print(finaldata.shape)
#defining the columns for 'X' and 'y'
y=finaldata['Response']
X=finaldata.iloc[:,0:113]
print(finaldata.shape)
print(X.shape)
#print(X.columns.values)

#Divide the data into train and test data in a ratio 75:25
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test =train_test_split(X,y,test_size=0.25)

print("TRaining data: ",x_train.shape)
print("test data: ",x_test.shape)

#Logistic Regression Model Building.
from sklearn.linear_model import LogisticRegression
lr= LogisticRegression()
#lr.fit(x_train, y_train)

#MUltinomial logistic regression
from sklearn import metrics
mlr=LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(x_train, y_train)

#in MUltinomial regression, predicting the response variable (calculated value)
y_pred = mlr.predict(x_test)
from pandas import DataFrame
dd=DataFrame({'actual':y_test,'calculated(mlr)':y_pred})
dd

#Accuracy of Multinomial Logistic regression on test data
print("Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score( y_test, mlr.predict(x_test)))