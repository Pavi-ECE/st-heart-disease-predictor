import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("https://github.com/Pavi-ECE/st-heart-disease-predictor/blob/main/KNN_Algo_trained.sav",'rb'))

def heart_disease_prediction(input):
    # preprocessing the input

    inp = np.asarray(input)
    # reshape the  input array
    inp_rshp = inp.reshape(1,-1)

    #predict the output
    prediction = loaded_model.predict(inp_rshp)

    if (prediction[0]==1):
        return 'The person has risk of heart disease'
    else:
        return 'The person has no risk of heart disease'

def main():
    # giving a title for a webpage
    st.title('Heart Disease Prediction Web App')

    # getting input data from the user
    
    bmi = st.number_input("Enter your BMI")

    if (st.selectbox("Smoking", ('Yes','No'))=='Yes'):
        smoking = 1
    else:
        smoking = 0

    if (st.selectbox("Alcohol Drinking", ('Yes','No'))=='Yes'):
        alcho_drink = 1
    else:
        alcho_drink = 0

    if (st.selectbox("Have you ever had Stroke", ('Yes', 'No'))=='Yes'):
        stroke = 1
    else:
        stroke = 0

    phy_ill = st.number_input("Physical illness")
    ment_ill = st.number_input("Mental illness")

    if (st.selectbox("Difficulty in walking or climbing stairs?",('Yes','No'))=='Yes'):
        diff_walk = 1
    else:
        diff_walk = 0

    if (st.selectbox("Sex",('Male','Female'))=='Female'):
        sex = 1
    else:
        sex = 0
    val2 = st.selectbox("Age Categary",('18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'))
    if (val2 =='18-24'):
        age = 0
    elif (val2 =='25-29'):
        age = 1
    elif(val2 =='30-34'):
        age = 2
    elif(val2 =='35-39'):
        age = 3
    elif(val2 =='40-44'):
        age = 4
    elif(val2=='45-49'):
        age = 5
    elif(val2 =='50-54'):
        age = 6
    elif(val2 =='55-59'):
        age = 7
    elif(val2 =='60-64'):
        age = 8
    elif(val2 =='65-69'):
        age = 9
    elif (val2 =='70-74'):
        age = 10
    elif (val2 =='75-79'):
        age = 11
    else:
        age = 12

    if (st.selectbox("Do you have diabetes",('Yes','No'))=='Yes'):
        diab = 1
    else:
        diab = 0
    
    if (st.selectbox("Physically Active?",('Yes','No'))=='Yes'):
        phy_act = 1
    else:
        phy_act = 0
    val = st.selectbox("What do you think about your general health?",('Excellent','Very Good','Good', 'Fair','Poor'))
    if (val =='Excellent'):
        general_health = 0
    elif(val =='Very Good'):
        general_health = 1
    elif (val =='Good'):
        general_health = 2
    elif (val =='Fair'):
        general_health = 3
    else:
        general_health = 4
    sleep_time = st.number_input("sleep time")
    
    if (st.selectbox("Are you an asthma patient?", ('Yes', 'No'))=='Yes'):
        asthma = 1
    else:
        asthma = 0
    
    if (st.selectbox("Do you ever had kidney disease?", ('Yes', 'No'))=='Yes'):
        kid_dis = 1
    else:
        kid_dis = 0
    
    if (st.selectbox("Do you have skin cancer?", ('Yes', 'No'))=='Yes'):
        skin_can = 1
    else:
        skin_can = 0

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction
    if st.button("Heart Disease Test Result"):
        diagnosis = heart_disease_prediction([bmi, smoking,alcho_drink, stroke, phy_ill, ment_ill, diff_walk, sex, age, diab, phy_act, general_health, sleep_time, asthma, kid_dis, skin_can])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()

# streamlit run "F:\SSN COLLEGE\SEMESTER 6\ML\Mini Project\Streamlit App\heart_dis_pred_webapp.py"
