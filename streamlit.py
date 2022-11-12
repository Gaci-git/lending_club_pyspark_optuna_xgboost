import xgboost as xgb
import streamlit as st
import pandas as pd
import sklearn

model = xgb.XGBClassifier()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache(suppress_st_warning=True)

# Define the prediction function
def predict(loan_amnt, term, grade, home_ownership, annual_inc):
            #verification_status, purpose, dti, open_acc, 
            #revol_bal, revol_util, 
            #initial_list_status, application_type,
            #mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line):
  
    if term == '36 months':
        term = 0
    elif term == '60 months':
        term = 1

    
    if grade == 'A':
        grade = 1
    elif grade == 'B':
        grade = 2
    elif grade == 'C':
        grade = 3
    elif grade == 'D':
        grade = 4
    elif grade == 'E':
        grade = 5
    elif grade == 'F':
        grade = 6
    elif grade == 'G':
        grade = 7


    if home_ownership == 'Own':
        home_ownership = 0
    elif home_ownership == 'Mortgage':
        home_ownership = 1
    elif home_ownership == 'Rent':
        home_ownership = 2
          

    prediction = model.predict(pd.DataFrame([[loan_amnt, term, grade, home_ownership, annual_inc]],
                                              #verification_status, purpose, dti, open_acc, 
                                              #revol_bal, revol_util,
                                              #initial_list_status, application_type,
                                              #mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line]], 
            columns=['loan_amnt', 'term', 'grade', 
                      'home_ownership', 'annual_inc']))
                      #'verification_status', 'purpose', 'dti, open_acc', 
                      #'revol_bal', 'revol_util', 
                      #'initial_list_status', 'application_type',
                      #'mort_acc', 'pub_rec_bankruptcies', 'time_paid_back', 'cr_line']))
    return prediction
  
  
st.title('Loan Outcome Prediction')
#st.image(""".png""")
st.header('Fill your request:')

loan_amnt = st.number_input('Loan amount:', min_value=0.1, max_value=100000000000000.0, value=1.0)
term = st.selectbox('Term:', ['36 months', '60 months'])
grade = st.selectbox('Grade Rating:', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

#emp_length = st.selectbox('Employment Length:', ['less than 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', '8 years', '9 years', '10 years or more'])


home_ownership = st.selectbox('Home Ownerhip:', ['Rent', 'Own', 'Mortgage'])

annual_inc = st.number_input('Annual Income:', min_value=0.1, max_value=10000000000000.0, value=1.0)

#verification_status = st.selectbox('Verification Status:', ['Verified', 
                                                            #'Source verified', 
                                                            #'Not Verified'])

#purpose = st.selectbox('Verification Status:', ['debt consolidation', 
                                                #'credit card',
                                                #'home improvement',
                                                #'other',
                                                #'major purchase',
                                                #'car',
                                                #'vacation',
                                                #'moving',
                                                #'house',
                                                #'renewable energy',
                                                #'wedding',
                                                #'medical',
                                                #'small business'])

#dti = st.number_input('DTI:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#open_acc = st.number_input('How many accounts are open:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#revol_bal = st.number_input('Total credit revolving balance:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#revol_util = st.number_input('Revolving line utilization rate', min_value=0.1, max_value=10000000000000.0, value=1.0)

#initial_list_status = st.selectbox('Inital List Status:', ['W', 'F'])

#application_type = st.selectbox('Inital Listing Status:', ['Individual', 'Joint Application'])

#mort_acc = st.number_input('Number of mortgage accounts:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#pub_rec_bankruptcies = st.number_input('Reported Bankruptcies:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#time_paid_back = st.number_input('How long customer will take to repay:', min_value=0.1, max_value=10000000000000.0, value=1.0)
#cr_line = st.number_input('For many years Credit Line was open:', min_value=0.1, max_value=10000000000000.0, value=1.0)


if st.button('Predict Outcome'):
    outcome = predict(loan_amnt, term, grade, home_ownership, annual_inc)
                                             #verification_status, purpose, dti, open_acc, revol_bal, revol_util, initial_list_status, application_type, mort_acc, pub_rec_bankruptcies, time_paid_back, cr_line)
    
    st.success(f'The predicted outcome of the loan is ${outcome}')
