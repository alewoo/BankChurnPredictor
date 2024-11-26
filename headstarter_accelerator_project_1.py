# -*- coding: utf-8 -*-
"""Headstarter Accelerator Project 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e2DMratZbWOwzDhbMQUekwsxQjPVn1b-
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("churn.csv")

df

df.describe()

sns.set_style(style="whitegrid")
plt.figure(figsize=(12, 10))

sns.countplot(x="Exited", data=df)
plt.title("Distribution of Churn")

sns.histplot(data=df, x="Age", kde=True)
plt.title("Age Distribution")

sns.scatterplot(data=df, x="CreditScore", y="Age", hue="Exited")
plt.title("Credit Score vs Age")

sns.boxplot(x="Exited", y="Balance", data=df)
plt.title("Balance Distribution by Churn")

sns.boxplot(x="Exited", y="CreditScore", data=df)
plt.title("Credit Score Distribution by Churn")

features = df.drop("Exited", axis=1)

features

target = df["Exited"]

target

features = features.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

features

features = features.dropna()

features

features = pd.get_dummies(features, columns=["Geography", "Gender"])

features

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

X_train[0]

X_train[1]

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

lr_model = LogisticRegression(random_state=42)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_predictions

lr_accuracy = accuracy_score(y_test, lr_predictions)

lr_accuracy

def evaluate_and_save_model(model, X_train, X_test, y_train, y_test, filename):
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  print(f"{model.__class__.__name__} Accuracy: {accuracy:.4f}")
  print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
  print("--------------")

  with open(filename, "wb") as file:
    pickle.dump(model, file)

  print(f"Model Saved as {filename}")

xgb_model = xgb.XGBClassifier(random_state=42)
evaluate_and_save_model(xgb_model, X_train, X_test, y_train, y_test, "xgb_model.pkl")

dt_model = DecisionTreeClassifier(random_state=42)
evaluate_and_save_model(dt_model, X_train, X_test, y_train, y_test, "dt_model.pkl")

rf_model = RandomForestClassifier(random_state=42)
evaluate_and_save_model(rf_model, X_train, X_test, y_train, y_test, "rf_model.pkl")

nb_model = GaussianNB()
evaluate_and_save_model(nb_model, X_train, X_test, y_train, y_test, "nb_model.pkl")

knn_model = KNeighborsClassifier()
evaluate_and_save_model(knn_model, X_train, X_test, y_train, y_test, "knn_model.pkl")

svm_model = SVC(random_state=42)
evaluate_and_save_model(svm_model, X_train, X_test, y_train, y_test, "svm_model.pkl")

feature_importances = xgb_model.feature_importances_
feature_names = features.columns

feature_importances

feature_names

feature_importances_df = pd.DataFrame({
    'feature': feature_names,
    'importance': feature_importances
})

feature_importances_df

feature_importances_df = feature_importances_df.sort_values('importance', ascending=False)

feature_importances_df

plt.figure(figsize=(10, 6))
plt.bar(feature_importances_df['feature'], feature_importances_df['importance'])
plt.xticks(rotation=90)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

features

features['CLV'] = df['Balance'] * df['EstimatedSalary'] / 100000

features

features['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 45, 60, 100], labels=['Young', 'MiddleAge', 'Senior', 'Elderly'])

features

features['TenureAgeRatio'] = df['Tenure'] / df['Age']

features

features = pd.get_dummies(features, drop_first=True)

features

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

X_train

xgboost_model = xgb.XGBClassifier(random_state=42)

evaluate_and_save_model(xgboost_model, X_train, X_test, y_train, y_test, "xgboost-featureEngineered.pkl")

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

evaluate_and_save_model(xgboost_model, X_resampled, X_test, y_resampled, y_test, "xgboost-SMOTE.pkl")

from sklearn.ensemble import VotingClassifier

voting_clf = VotingClassifier(
    estimators=[('xgboost', xgb.XGBClassifier(random_state=42)), ('rf', RandomForestClassifier(random_state=42)), ('svm', SVC(random_state=42, probability=True))],
    voting='hard'
)

evaluate_and_save_model(voting_clf, X_resampled, X_test, y_resampled, y_test, "voting_clf.pkl")

