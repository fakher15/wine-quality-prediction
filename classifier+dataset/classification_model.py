import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib


red=pd.read_excel('C:/Users/hp/Desktop/dataset/winequalitywhite.xltx')

#Data descriptipn
red.info()
red.isnull().sum()
red.duplicated().sum()
red['quality'].value_counts()

#remove duplicates

red=red.drop_duplicates()


# rating function

def rate(x):
    if x>6.5:
        return 'good'
    else:
        return 'poor'
    
red['rating']=red['quality'].apply(lambda x: rate(x))

#data preparation

X=red.drop(labels=['quality','rating'],axis=1)
y=red['rating']


from sklearn.preprocessing import LabelEncoder
encode=LabelEncoder()
yNew=encode.fit_transform(y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,yNew, test_size=0.2, random_state=42)

#creating classification model

from xgboost import XGBClassifier

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
#model = RandomForestClassifier(n_estimators=100)
model=XGBClassifier()

model.fit(X_train, y_train)
y_pred=model.predict(X_test)
print("Accuracy score: {}".format(accuracy_score(y_test, y_pred)))
print("classification report\n")
print(classification_report(y_test,y_pred))
print("\n")
print("{} model has accuracy of {}".format(str(model),accuracy_score(y_test, y_pred)))


#vector prediction



v=np.array([[7.4,0.7,0,1.9,0.076,11,34,0.99,3.51,0.56,9.4]])
v=np.array([[7.4,0.24,0.36,2.0,0.031,27.0,139.0,0.99055,3.28,0.48,12.5]])

import statistics
v[0][0]=( v[0][0]-statistics.mean(red['fixed acidity'])) /statistics.stdev(red['fixed acidity'])
v[0][1]=( v[0][1]-statistics.mean(red['volatile acidity'])) /statistics.stdev(red['volatile acidity'])
v[0][2]=( v[0][2]-statistics.mean(red['citric acid'])) /statistics.stdev(red['citric acid'])
v[0][3]=( v[0][3]-statistics.mean(red['residual sugar'])) /statistics.stdev(red['residual sugar'])
v[0][4]=( v[0][4]-statistics.mean(red['chlorides'])) /statistics.stdev(red['chlorides'])
v[0][5]=( v[0][5]-statistics.mean(red['free sulfur dioxide'])) /statistics.stdev(red['free sulfur dioxide'])
v[0][6]=( v[0][6]-statistics.mean(red['total sulfur dioxide'])) /statistics.stdev(red['total sulfur dioxide'])
v[0][7]=( v[0][7]-statistics.mean(red['density'])) /statistics.stdev(red['density'])
v[0][8]=( v[0][8]-statistics.mean(red['pH'])) /statistics.stdev(red['pH'])
v[0][9]=( v[0][9]-statistics.mean(red['sulphates'])) /statistics.stdev(red['sulphates'])
v[0][10]=( v[0][10]-statistics.mean(red['alcohol'])) /statistics.stdev(red['alcohol'])

def rating(x):
    rate=model.predict(x)
    if rate[0]==1:
        print('poor')
    else : print ('good')

rating(v)

	
joblib.dump(model, 'C:/Users/hp/Desktop/classifier.sav')

