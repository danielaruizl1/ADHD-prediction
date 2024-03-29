#%%
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
import pandas as pd
import numpy as np

#%% Original data
original_data = pd.read_csv("data_before_pca.csv")
o_features = original_data.iloc[:,1:]
o_labels = original_data.iloc[:,0]
ft_train, ft_test, l_train, l_test = train_test_split(o_features, o_labels, test_size=0.3, random_state=42)

print("Original data uploaded successfully")

#%% Normalized original data
scaler = MinMaxScaler()
o_features = scaler.fit_transform(o_features)
ft_train, ft_test, l_train, l_test = train_test_split(o_features, o_labels, test_size=0.3, random_state=42)
print("Normalized original data uploaded successfully")

#%% PCA data
pca_data = pd.read_csv("data_after_pca.csv")
pca_features = pca_data.iloc[:,1:]
pca_labels = original_data.iloc[:,0]
ft_train, ft_test, l_train, l_test = train_test_split(pca_features, pca_labels, test_size=0.3, random_state=42)

print("PCA data uploaded successfully")

#%% Exp1
clf = LinearSVC(random_state=0)

#%% Exp2
clf = LinearSVC(random_state=0,penalty="l1",loss="squared_hinge", dual=False)

#%% Exp3
clf = LinearSVC(random_state=0,penalty="l2",loss="hinge")

#%% Exp4
clf = LinearSVC(random_state=0,penalty="l1",loss="squared_hinge", dual=False, C=0.1)

#%% Exp5
clf = LinearSVC(random_state=0,penalty="l1",loss="squared_hinge", dual=False, C=100)

#%% Exp6
clf = LinearSVC(random_state=0,penalty="l1",loss="squared_hinge", dual=False, C=1, class_weight="balanced")

#%% Scores

clf.fit(ft_train, l_train)
print('Accuracy of Linear SVC classifier on training set: {:.2f}'
     .format(clf.score(ft_train, l_train)))
print('Accuracy of Linear SVC classifier on test set: {:.2f}'
     .format(clf.score(ft_test, l_test)))

#%% Cross Validation

cv = cross_val_score(clf,o_features,o_labels)
cv2 = cross_val_score(clf,pca_features,pca_labels)
print("original:",np.mean(cv))
print("pca:",np.mean(cv2))

#Kernalized SVM
#%% Exp1
clf = SVC(random_state=0)

#%% Exp2
clf = SVC(random_state=0,C=0.1)

#%% Exp3
clf = SVC(random_state=0,kernel="sigmoid")

#%% Exp4
clf = SVC(random_state=0,kernel="sigmoid", C=0.1)

#%% Exp5
clf = SVC(random_state=0,kernel="poly")

#%% Exp6
clf = SVC(random_state=0,kernel="poly", C=100)

#%% Exp7
clf = SVC(random_state=0, class_weight="balanced")

#%% Exp8
clf = SVC(random_state=0,kernel="sigmoid", class_weight="balanced")

#%% Scores

clf.fit(ft_train, l_train)
print('Accuracy of kernelized SVMs on training set: {:.2f}'
     .format(clf.score(ft_train, l_train)))
print('Accuracy of kernelized SVMs on test set: {:.2f}'
     .format(clf.score(ft_test, l_test)))

#%% Cross Validation

#Accuracy
print("Accuracy")
cv = cross_val_score(clf,o_features,o_labels)
#cv2 = cross_val_score(clf,pca_features,pca_labels)
print("original:",round(np.mean(cv),3))
#print("pca:",round(np.mean(cv2),3))

#Precision
print("Precision")
cv = cross_val_score(clf,o_features,o_labels, scoring="precision")
#cv2 = cross_val_score(clf,pca_features,pca_labels, scoring="precision")
print("original:",round(np.mean(cv),3))
#print("pca:",round(np.mean(cv2),3))

#Recall
print("Recall")
cv = cross_val_score(clf,o_features,o_labels, scoring="recall")
#cv2 = cross_val_score(clf,pca_features,pca_labels, scoring="recall")
print("original:",round(np.mean(cv),3))
#print("pca:",round(np.mean(cv2),3))

#Area under the curve
print("AUC")
cv = cross_val_score(clf,o_features,o_labels, scoring="roc_auc")
#cv2 = cross_val_score(clf,pca_features,pca_labels, scoring="roc_auc")
print("original:",round(np.mean(cv),3))
#print("pca:",round(np.mean(cv2),3))