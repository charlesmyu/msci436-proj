import streamlit as st
import joblib
import pandas as pd

models = {
        'Low': 'model-23',
        'Medium-Low': 'model-19',
        'Medium-High': 'model-15',
        'High': 'model-11'
    }

def predict(df, strength):
    model = models.get(strength)

    transformer = joblib.load(f'model/{model}/transformer.sav')
    pca = joblib.load(f'model/{model}/pca.sav')
    bgc = joblib.load(f'model/{model}/bgc.sav')
    
    df = helper_func(df)
    
    df = transformer.transform(df)
    df = pca.transform(df)
    ypred = bgc.predict(df)
    
    return ypred

def input_func():
    Age = float(st.number_input('Applicant Age', min_value = 18))
    CreditScore = float(st.slider('Credit Score', min_value = 0, max_value = 850)) / 12.6866
    BankCustomer = int(binary_func(st.radio('Bank Customer?', options = ['Yes', 'No'])))
    DriversLicense = int(binary_func(st.radio('Driver\'s License?', options = ['Yes', 'No'])))
    Debt = float(st.number_input('Applicant Debt ($)', min_value = 0)) / 1000
    PriorDefault = int(binary_func(st.radio('Prior Defaults?', options = ['Yes', 'No'])))
    Employed = int(binary_func(st.radio('Employed?', options = ['Yes', 'No'])))
    Industry = st.selectbox('Industry', options = ['Utilities', 'Real Estate', 'Education', 'Research', 'Transport', 'Other'])
    YearsEmployed = float(st.number_input('Years Employed', min_value = 0))
    Income = float(st.number_input('Income ($)', min_value = 0)) / 1000
    
    df = pd.DataFrame({'Age':[Age], 'Debt': [Debt], 'BankCustomer': [BankCustomer], 'Industry':[Industry], 'YearsEmployed':[YearsEmployed], 'PriorDefault':[PriorDefault], 'Employed':[Employed], 'CreditScore':[CreditScore], 'DriversLicense':[DriversLicense], 'Income':[Income]})
    
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
with st.form(key='input'):
    df = input_func()
    strength = st.select_slider(label = 'Sensitivity', options = models.keys())
    if st.form_submit_button('Run Model'):
        res = predict(df, strength)
        a = st.header('Result: Recommend Accept Application') if res[0] else st.header('Result: Recommend Deny Application')
