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
    - Google Colab [notebook](https://colab.research.google.com/drive/1brRQMUM7SAXfF8Jf7eo8CskFXJ5nDBG2?usp=sharing)
    - Git hub repository for [Loan_club](https://github.com/Gaci-git/loan_club)
"""
)
