import streamlit as st
import tensorflow as tf

from tensorflow import keras 
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np

@st.cache(suppress_st_warning=True)


model = keras.models.load_model('tf_model')

# Define the prediction function
def predict(loan_amnt, term,
            emp_length,
            home_ownership, annual_inc,
            verification_status,
            purpose, 
            dti, 
            open_acc, 
            revol_bal, revol_util, 
            initial_list_status, application_type,
            mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line):
  
    if term == '36 months':
        term = 0
    elif term == '60 months':
        term = 1

    if emp_length == 'less than 1 year':
         emp_length = 0
    elif emp_length == '1 year':
         emp_length = 1
    elif emp_length == '2 years':
         emp_length = 2
    elif emp_length == '3 years':
         emp_length = 3
    elif emp_length == '4 years':
         emp_length = 4
    elif emp_length == '5 years':
         emp_length = 5
    elif emp_length == '6 years':
         emp_length = 6
    elif emp_length == '7 years':
         emp_length = 7
    elif emp_length == '8 years':
         emp_length = 8
    elif emp_length == '9 years':
         emp_length = 9
    elif emp_length == '10 years or more':
         emp_length = 10

    if home_ownership == 'Own':
        home_ownership = 0
    elif home_ownership == 'Mortgage':
        home_ownership = 1
    elif home_ownership == 'Rent':
        home_ownership = 2

    if verification_status == 'Source verified':
        verification_status = 0
    elif verification_status == 'Verified':
        verification_status = 1
    elif verification_status == 'Not verified':
        verification_status = 2

    if purpose == 'debt consolidation':
        purpose = 0
    elif purpose == 'credit card':
        purpose = 1
    elif purpose == 'home improvement':
        purpose = 2
    elif purpose == 'other':
        purpose = 3
    elif purpose == 'major purchase':
        purpose = 4
    elif purpose == 'car':
        purpose = 5
    elif purpose == 'vacation':
        purpose = 6
    elif purpose == 'moving':
        purpose = 7
    elif purpose == 'house':
        purpose = 8
    elif purpose == 'renewable energy':
        purpose = 9
    elif purpose == 'wedding':
        purpose = 10
    elif purpose == 'medical':
        purpose = 11
    elif purpose == 'small business':
        purpose = 12
        
    if application_type == 'Individual':
        application_type = 0
    elif application_type == 'Joint Application':
        application_type = 1

    if initial_list_status == 'W':
        initial_list_status = 0
    elif initial_list_status == 'F':
        initial_list_status = 1
          

    prediction = model.predict(pd.DataFrame([[loan_amnt, term,  
                                              emp_length,
                                              home_ownership, annual_inc,
                                              verification_status,
                                              purpose, 
                                              dti, 
                                              open_acc, 
                                              revol_bal, revol_util,
                                              initial_list_status, application_type,
                                              mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line]], 
                                            
            columns=['loan_amnt', 'term',
                     'emp_length',
                     'home_ownership', 'annual_inc',
                     'verification_status',
                     'purpose',
                     'dti', 'open_acc', 
                     'revol_bal', 'revol_util', 
                     'initial_list_status', 'application_type',
                     'mort_acc', 'pub_rec_bankruptcies', 'time_paid_back', 'cr_line']))
    return prediction
  
  
st.title('Loan Sub-grading Prediction')
#st.image(""".png""")
st.header('Fill your request:')

loan_amnt = st.number_input('Loan amount:', min_value=0.1, max_value=100000000000000.0, value=1.0)
term = st.selectbox('Term:', ['36 months', '60 months'])

emp_length = st.selectbox('Employment Length:', ['less than 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', '8 years', '9 years', '10 years or more'])


home_ownership = st.selectbox('Home Ownerhip:', ['Rent', 'Own', 'Mortgage'])

annual_inc = st.number_input('Annual Income:', min_value=0.1, max_value=10000000000000.0, value=1.0)

verification_status = st.selectbox('Verification Status:', ['Verified', 
                                                            'Source verified', 
                                                            'Not verified'])

purpose = st.selectbox('Purpose', ['debt consolidation', 
                                                'credit card',
                                                'home improvement',
                                                'other',
                                                'major purchase',
                                                'car',
                                                'vacation',
                                                'moving',
                                                'house',
                                                'renewable energy',
                                                'wedding',
                                                'medical',
                                                'small business'])
                                                


dti = st.number_input('DTI:', min_value=0.1, max_value=10000000000000.0, value=1.0)
open_acc = st.number_input('How many accounts are open:', min_value=0.1, max_value=10000000000000.0, value=1.0)

revol_bal = st.number_input('Total credit revolving balance:', min_value=0.1, max_value=10000000000000.0, value=1.0)
revol_util = st.number_input('Revolving line utilization rate', min_value=0.1, max_value=10000000000000.0, value=1.0)
initial_list_status = st.selectbox('Inital List Status:', ['W', 'F'])
application_type = st.selectbox('Inital Listing Status:', ['Individual', 'Joint Application'])

mort_acc = st.number_input('Number of mortgage accounts:', min_value=0.1, max_value=10000000000000.0, value=1.0)
pub_rec_bankruptcies = st.number_input('Reported Bankruptcies:', min_value=0.1, max_value=10000000000000.0, value=1.0)
time_paid_back = st.number_input('How long customer will take to repay:', min_value=0.1, max_value=10000000000000.0, value=1.0)
cr_line = st.number_input('For many years Credit Line was open:', min_value=0.1, max_value=10000000000000.0, value=1.0)


if st.button('Predict Outcome'):
    outcome = predict(loan_amnt, term,  
                      emp_length,
                      home_ownership, annual_inc,
                      verification_status,
                      purpose, 
                      dti, open_acc,
                      revol_bal, revol_util, initial_list_status, application_type,
                      mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line)
    

            
my_dict = {'A1': 0, 'A2' : 1, 'A3': 2, 'A4': 3, 'A5': 4,
           'B1': 5, 'B2' : 6, 'B3': 7, 'B4': 8, 'B5': 9,
           'C1': 10, 'C2' : 11, 'C3': 12, 'C4': 13, 'C5': 14,
           'D1': 15, 'D2' : 16, 'D3': 17, 'D4': 18, 'D5': 19,
           'E1': 20, 'E2' : 21, 'E3': 22, 'E4': 23, 'E5': 24,
           'F1': 25, 'F2' : 26, 'F3': 27, 'F4': 28, 'F5': 29,
           'G1': 30, 'G2' : 31, 'G3': 32, 'G4': 33, 'G5': 34}         
            
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

st.success(f'Loan sub-grading: {get_key(outcome)}')
