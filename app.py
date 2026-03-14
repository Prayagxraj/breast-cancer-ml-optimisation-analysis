import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

#''' this loads the data'''
df = pd.read_csv("data/data.csv")

#'''Cleaning the dataset'''
df = df.drop(["id", "Unnamed: 32"], axis=1)
df["diagnosis"] = df["diagnosis"].map({"M":1,"B":0})

#'''Splitting the features'''
X = df.drop("diagnosis", axis=1)
y = df["diagnosis"]

#''' Training the model '''
model = RandomForestClassifier()
model.fit(X, y)

st.title("Breast Cancer Prediction ")

st.write("Dataset Preview")
st.dataframe(df.head())

#''' Class distribution'''
st.subheader("Diagnosis Distribution")

fig, ax = plt.subplots()
sns.countplot(x="diagnosis", data=df, ax=ax)
st.pyplot(fig)

#''' Feature importance '''
st.subheader("Feature Importance")

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

st.bar_chart(importance.head(10))

# ''' visualization too understand the type of distribution'''
st.subheader("Feature Distribution")

feature = st.selectbox("Select Feature", X.columns)

fig2, ax2 = plt.subplots()
sns.histplot(df[feature], kde=True, ax=ax2)
st.pyplot(fig2)