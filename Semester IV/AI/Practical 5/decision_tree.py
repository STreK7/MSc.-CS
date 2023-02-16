
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#func importing dataset
def importdata():
      balance_data=pd.read_csv("balance-scale.data")

      #print the dataset shape
      print("Dataset Length : ",len(balance_data))
      
      #printing the dataset observations
      print("Dataset : ",balance_data.head())
      return balance_data

#func to split the dataset
def splitdataset(balance_data):
      #seperating the target variable
      X=balance_data.values[:,1:5]
      Y=balance_data.values[:,0]

      #splitting the dataset into train and test
      X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)
      return X,Y,X_train,X_test,y_train,y_test

#function to perform training with entropy
def train_using_entropy(X_train,X_test,y_train,y_test):
      #decision tree with entropy
      clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)

      #performing training
      clf_entropy.fit(X_train,y_train)
      return clf_entropy

def prediction(X_test,clf_object):
      y_pred=clf_object.predict(X_test)
      print("Predicted Values : ")
      print(y_pred)
      return y_pred

def cal_accuracy(y_test,y_pred):
      print("Accuracy : ",accuracy_score(y_test,y_pred)*100)

def main():
      data=importdata()
      X,Y,X_train,X_test,y_train,y_test=splitdataset(data)
      
      clf_entropy=train_using_entropy(X_train,X_test,y_train,y_test)

      print("Results using entropy : ")
      y_pred_entropy=prediction(X_test,clf_entropy)
      cal_accuracy(y_test,y_pred_entropy)

main()