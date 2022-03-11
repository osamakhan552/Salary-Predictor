import imp
import numpy as np 
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

def shortenCategories(categories, cutoff):
    categoricalMap = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categoricalMap[categories.index[i]] = categories.index[i]
        else:
            categoricalMap[categories.index[i]] = "Other"
    return categoricalMap



def cleanExperience(x):
        if x == 'More than 50 years':
            return 50
        if x == 'Less than 1 year':
            return 0.5
        return float(x)





def cleanEducation(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Professional or Other doctoral degree'
    return 'Less than a bachelors'

@st.cache
def loadData():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country","EdLevel","YearsCodePro","Employment","ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)  
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment",axis=1)

    countryMap = shortenCategories(df.Country.value_counts(),400)

    df['Country'] = df['Country'].map(countryMap)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != 'Other']

    df["YearsCodePro"] = df["YearsCodePro"].apply(cleanExperience)
    df['EdLevel'] = df['EdLevel'].apply(cleanEducation)   

    return df


df = loadData()

def showGraph():

    st.title("Graphical Representation")

    st.write("""  ### Developer Salary Data 2021 """)

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()

    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")

    st.write(""" #### Number of data from different countries""")

    st.pyplot(fig1)

    st.write(""" #### Mean salary based on country""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)

    st.bar_chart(data)

    st.write(""" #### Mean salary based on experience""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)

    st.line_chart(data)

