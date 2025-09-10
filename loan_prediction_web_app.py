import numpy as np
import pickle
import streamlit as st


# #loading the saved model
loaded_model = pickle.load(open(r"C:\Users\TEMITOPE\Desktop\GOMYCODE\Cohort_2_2025\loan_prediction_model_v2.pkl", "rb"))

def loan_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand I am making prediction for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    

    #making prediction on the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return("This customer is not eligible for a loan")
    else:
        return("This customer is eligible for a loan")
    

def main():

    # giving the app a title
    st.title("Loan Prediction Web App")
    # getting the input data from user

    gender = st.text_input("gender: enter 1 for male and 0 for female")
    married = st.text_input("married")
    education = st.text_input("education")
    self_employed = st.text_input("self_employed")
    applicant_income = st.text_input("applicant_income")
    coapplicant_income = st.text_input("coapplicant_income")
    loan_amount = st.text_input("loan_amount")
    loan_amount_term = st.text_input("loan_amount_term")
    dependents_1 = st.text_input("dependents_1")
    dependents_2 = st.text_input("dependents_2")
    dependents_3 = st.text_input("dependents_3+")
    credit_history = st.text_input("credit_history")
    property_area_Semiurban = st.text_input("property_area_Semiurban")
    property_area_Urban = st.text_input("property_area_Urban")


    # code for Prediction
    performance = ""

    # creating a button for prediction

    if st.button("Loan status"):
        performance = loan_prediction(
            [gender, married, education, self_employed, applicant_income, coapplicant_income,
             loan_amount, loan_amount_term, dependents_1, dependents_2, dependents_3,
             credit_history, property_area_Semiurban, property_area_Urban])
        st.success(performance)

if __name__ == "__main__":
    main()