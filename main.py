import streamlit as st
import joblib
import pandas as pd

def main():
    pass

def predict(df):
    transformer = joblib.load('models/transformer.sav')
    pca = joblib.load('models/pca.sav')
    bgc = joblib.load('models/bgc.sav')
    
    df = helper_func(df)
    
    df = transformer.transform(df)
    df = pca.transform(df)
    ypred = bgc.predict(df)
    
    return ypred

def input_func():
    # Need to natively scale some of the inputs (e.g. debt, income, credit score are all funky atm)
    Age = float(st.number_input('Applicant Age', min_value = 18))
    Debt = float(st.number_input('Applicant Debt (Thousands of Dollars)', min_value = 0))
    BankCustomer = int(binary_func(st.radio('Bank Customer?', options = ['Yes', 'No'])))
    Industry = st.selectbox('Industry', options = ['Utilities', 'Real Estate', 'Education', 'Research', 'Transport', 'Other'])
    YearsEmployed = float(st.number_input('Years Employed', min_value = 0))
    PriorDefault = int(binary_func(st.radio('Prior Defaults?', options = ['Yes', 'No'])))
    Employed = int(binary_func(st.radio('Employed?', options = ['Yes', 'No'])))
    CreditScore = float(st.number_input('Credit Score', min_value = 0))
    DriversLicense = int(binary_func(st.radio('Driver\'s License?', options = ['Yes', 'No'])))
    Income = float(st.number_input('Income (Thousands of Dollars)', min_value = 0))
    
    df = pd.DataFrame({'Age':[Age], 'Debt': [Debt], 'BankCustomer': [BankCustomer], 'Industry':[Industry], 'YearsEmployed':[YearsEmployed], 'PriorDefault':[PriorDefault], 'Employed':[Employed], 'CreditScore':[CreditScore], 'DriversLicense':[DriversLicense], 'Income':[Income]})
    
    # Output is currently unformatted, need to clean up
    return df
    
def binary_func(input):
    return 1 if input == 'Yes' else 0

# Helper function taken from "credit-approval-system-val-92-86-test-82-61.ipynb"
def helper_func(df):
    for idx, row in df.iterrows():
        if df.loc[idx, 'Age']< 30:
            df.loc[idx, 'Age'] = 'youth'
        elif df.loc[idx, 'Age']>=30 and df.loc[idx, 'Age']<40:
            df.loc[idx, 'Age'] = 'youthWithResponsibility'
        elif df.loc[idx, 'Age']>=40 and df.loc[idx, 'Age']<55:
            df.loc[idx, 'Age'] = 'midLife'
        elif df.loc[idx, 'Age']>=55:
            df.loc[idx, 'Age'] = 'towardsRetirement'
    for idx, row in df.iterrows():
        if df.loc[idx, 'Debt']>=0 and df.loc[idx, 'Debt']<5:
            df.loc[idx, 'Debt'] = 'Green'
        elif df.loc[idx, 'Debt']>=5 and df.loc[idx, 'Debt']<10:
            df.loc[idx, 'Debt'] = 'Yellow'
        elif df.loc[idx, 'Debt']>=10 and df.loc[idx, 'Debt']<15:
            df.loc[idx, 'Debt'] = 'Orange'
        elif df.loc[idx, 'Debt']>=15:
            df.loc[idx, 'Debt'] = 'Red'
    for idx, row in df.iterrows():
        if df.loc[idx, 'CreditScore']>=0 and df.loc[idx, 'CreditScore']<5:
            df.loc[idx, 'CreditScore'] = 'Red'
        elif df.loc[idx, 'CreditScore']>=5 and df.loc[idx, 'CreditScore']<10:
            df.loc[idx, 'CreditScore'] = 'Yellow'
        elif df.loc[idx, 'CreditScore']>=10:
            df.loc[idx, 'CreditScore'] = 'Green'
    for idx, row in df.iterrows():
        if df.loc[idx, 'YearsEmployed']>=0 and df.loc[idx, 'YearsEmployed']<0.5:
            df.loc[idx, 'YearsEmployed'] = 'Fresher'
        elif df.loc[idx, 'YearsEmployed']>=0.5 and df.loc[idx, 'YearsEmployed']<2.56:
            df.loc[idx, 'YearsEmployed'] = 'Experienced'
        elif df.loc[idx, 'YearsEmployed']>=2.56:
            df.loc[idx, 'YearsEmployed'] = 'Expert'
    for idx, row in df.iterrows():
        if df.loc[idx, 'Income']==0.0:
            df.loc[idx, 'Income'] = 'Poor'
        elif df.loc[idx, 'Income']>=0.0 and df.loc[idx, 'Income']<150.0:
            df.loc[idx, 'Income'] = 'Middle Class'
        elif df.loc[idx, 'Income']>=150.0:
            df.loc[idx, 'Income'] = 'Rich'
    for idx, row in df.iterrows():
        if df.loc[idx, 'Industry'] in ['Utilities', 'Real Estate', 'Education', 'Research', 'Transport']:
            df.loc[idx, 'Industry'] = 'Others'
    return df

st.title('Credit Card Application DSS')
df = input_func()
if st.button('Run Model'):
    st.write(predict(df))