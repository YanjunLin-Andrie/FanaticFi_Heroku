# Imports
import pandas as pd
# from pathlib import Path
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('./NBA_20_yr.csv')

# Create a column to hold Group data
df.loc[:,'Group'] = 0
df.fillna(0, inplace = True)

# Create groups based on ranks
for index, row in df.iterrows():
    if row['Rk'] <= 15:
        df.at[index,'Group'] = 1
    else:
        df.at[index,'Group'] = 0

# Set Feature and Target
X = df.drop(columns=['Rk','Group'])
y = df['Group']


# Split dataset into train, test datasets
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state = 1)
# Initiate the scaler
X_scaler = StandardScaler()
# Fit the scaler to the features dataset
X_scaler = X_scaler.fit(X)
# Scale train, test datasets
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

import pickle

# save the scaler
Standard_Scaler = open("scaler.pkl","wb")
pickle.dump(X_scaler,Standard_Scaler) 
Standard_Scaler.close() 
# Load the scaler
model = open("scaler.pkl","rb")           
new_scaler = pickle.load(model)  

# From SVM, instantiate SVC classifier model instance
svm_model = svm.SVC(kernel = 'linear', random_state = 0)
 
# Fit the model to the data using the training data
svm_model = svm_model.fit(X_train_scaled, y_train)
 
# Use the testing data to make the model predictions
svm_pred = svm_model.predict(X_test_scaled)

# save the model
Support_Vector_Machine = open("model.pkl","wb")
pickle.dump(svm_model,Support_Vector_Machine) 
Support_Vector_Machine.close()