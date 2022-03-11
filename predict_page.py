import streamlit as st 
import pickle
import numpy as np 



def loadModel():
    with open('saved_step.pkl', 'rb') as file:
        data = pickle.load(file)

    return data

data = loadModel()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def showPredictPage():
    st.title("Software developer salary predictor")


    countries = (
    "United States of America",                            
    "India",                                                    
    "Germany",                                                 
    "United Kingdom of Great Britain and Northern Ireland",     
    "Canada"  ,                                                 
    "France" ,                                                  
    "Brazil",                                                   
    "Spain",                                                     
    "Netherlands",                                               
    "Australia",                                                 
    "Poland",                                                    
    "Italy",                                                     
    "Russian Federation",                                       
    "Sweden",                                                    
    "Turkey" ,                                                   
    "Switzerland",                                               
    "Israel" ,                                                   
    "Norway"
    )


    education = ('Master’s degree', 'Bachelor’s degree', 'Post grad',
        'Less than a bachelors')

    country = st.selectbox("Country", countries)
    edu = st.selectbox("Education Level", education)
    print(edu)
    print(country)
    exp = st.slider("Year of Experience", 0, 50, 3)

    submit = st.button("predict")

    if submit:
        x = np.array([[country,edu,exp]])
        x[:, 0] = le_country.transform(x[:, 0])
        x[:, 1] = le_education.transform(x[:, 1])
        x = x.astype(float)
        salary = regressor.predict(x)

        st.subheader(f"predicted salary ${salary[0]:.2f}")


