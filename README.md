# MSCI 436 Team Project
This project is a DSS for credit card applications, aiming to assist those who review credit card applications with an applicant's risk and rating. 

## Getting Started
Install dependencies using `pip install -r requirements.txt`, then use `streamlit run main.py` to run the application. 

## Data
***Add blurb here on data, why it's relevant, and how it was cleaned/updated for the model***

## Model
Model used was trained by Saumya Shah using Python (original notebook can be found [here](https://www.kaggle.com/code/sns5154/credit-approval-system-val-92-86-test-82-61) and in the `original-model` folder). A wealth of classifiers were attempted, but the K Neighbors Classifier with Bagging was ultimately selected, yielding a 82.35% F1-Score. This model was saved into three separate files stored in the `models` folder (`bgc.sav`, `pca.sav`, and `transformer.sav`) and imported into the DSS for use.

## UI
The UI was created using the Streamlit library, which was configured to take in the input parameters from the decision makers, before running those inputs through the model and displaying a result.  

## Sources
Data: https://www.kaggle.com/datasets/samuelcortinhas/credit-card-approval-clean-data  
Model: https://www.kaggle.com/code/sns5154/credit-approval-system-val-92-86-test-82-61 