import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to Loan Prediction Project with XGBoost ")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a page from the sidebar** to see Machine Learning models
    for Loan Prediction!
    
    ### Want kind of models this app contains?
    - Loan Outcome prediction model
    - Loan Grading prediction model
    - Loan Sub-grading prediction model

    ### See full code here:
    - Git hub repository for [Loan_club](https://github.com/Gaci-git/loan_club)
"""
)
