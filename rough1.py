#import the csv file
import csv
import pandas as pd 
data=pd.read_csv("/home/souny/Desktop/artivatic/Training.csv")
#print the header names
#print(data.columns.values)
print(data.shape)


#considering categorical variables and checking for missing values
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
print(df1)
print(df1.columns.values)


#for continous variables
df2=data[['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 'Employment_Info_4', 'Employment_Info_6',
 'Insurance_History_5', 'Family_Hist_2', 'Family_Hist_3', 'Family_Hist_4', 'Family_Hist_5']]
print(df2)
print(df2.columns.values)


#discrete
df3=data[['Medical_History_1', 'Medical_History_10', 'Medical_History_15', 'Medical_History_24', 'Medical_History_32']]
print(df3)
print(df3.columns.values)

#dummy
df4=data.loc[:, 'Medical_Keyword_1':'Medical_Keyword_48']
print(df4.columns.values)

#check for missing values
print(df1.isnull().sum(axis=0))
print(df2.isnull().sum(axis=0))
print(df3.isnull().sum(axis=0))
print(df4.isnull().sum(axis=0))
#summary of the dataset
#print(data.describe())



data= data.drop(['Employment_Info_4','Employment_Info_6','Insurance_History_5',
	'Family_Hist_2','Family_Hist_3','Family_Hist_4','Family_Hist_5','Medical_History_1','Medical_History_10','Medical_History_15',
	'Medical_History_24','Medical_History_32'], axis=1)
#print(data.columns.values)

#dataset aftr removing missing values
data2=data.dropna()
print(data2.shape)
'''writer = pd.ExcelWriter('finaldata.xlsx')
print(data2.to_excel(writer,'Sheet1'))
writer.save()'''



#correlation among continous variables
d2_cont=data2[['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1']]
print(d2_cont.columns.values)
df=d2_cont.corr()
writer = pd.ExcelWriter('output.xlsx')
print(df.to_excel(writer,'Sheet1'))
writer.save()

#the correlation of height and weight with BMI is high. 
data_final=data2.drop(['Ht','Wt'],axis=1)	
print(data_final.columns.values)


finaldata=data_final.drop(['Product_Info_2'],axis=1)
print(finaldata.columns.values)

'''#Dividing data into test and train
len_data_final=len(data_final)
len_train=int(0.75*len_data_final)
train_data=data_final[0:len_train]
test_data=data_final[len_train:]
print(train_data.shape)
print(test_data.shape)'''


