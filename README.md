# Artivatic-Assignment
For the dataset given, "Training.csv", I had to find out the risk class of the applicant given the attributes of the applicant.
This is a classification problem where the response variable ,i.e risk value has to be predicted. 
For this, the models that can be applied are KNN, decision tree and Regression. 

This dataset has more than 50,000 rows. So KNN will not be able to classify as it can't handle such a large dataset accurately.

There are more than 100 variables in this dataset. Applying decision tree will be too complex on such a large width of data.

As the dependent variable here is ordinal, we cannot use Linear Regression.

The dependent variable has many categories. Hence chose Multinomial regression which perfectly fits here. 

# the final code - FINALCODE.py

After I built the model on train data, it was tested on test data which shows 97% accuracy. 
The model accurately predicted the risk class of the test data



