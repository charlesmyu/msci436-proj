# MSCI 436 Team Project
This project is a DSS for credit card applications, aiming to assist those who review credit card applications with an applicant's risk and rating. 

## Getting Started
Install dependencies using `pip install -r requirements.txt`, then use `streamlit run main.py` to run the application. 

## Data
The leveraged dataset (found on Kaggle) is "Credit Card Approvals (Clean Data)" by Samual Cortinhas and contains 15 columns of identifying information commonly leveraged when evaluating an individual’s financial status for financial decisions. Cortinas adapted this dataset from from the University of California’s School of Information and Computer Science’s machine learning repository ("Credit Approval Dataset").

To clean the data, Cortinhas had inferred feature names that were initially unclear to clarify their contexts and filled missing values to allow all rows to be eligible for credit applications. Any identifiers that may induce bias on an application’s decision have been removed. These features include gender, ethnicity and zip code to prevent racism, sexism, and geographical bias respectively.

## Model
Model used was trained by Saumya Shah using Python (original notebook can be found [here](https://www.kaggle.com/code/sns5154/credit-approval-system-val-92-86-test-82-61) and in the `original-model` folder). A wealth of classifiers were attempted, but the K Neighbors Classifier with Bagging was ultimately selected, yielding a 82.35% F1-Score. These models were saved into the `model` folder and imported into the DSS for use.

## UI
The UI was created using the Streamlit library, which was configured to take in the input parameters from the decision makers, before running those inputs through the model and displaying a result. It also includes capabilities for the user to specify the "strictness" of the model, or how closely it vets applications. A lower strictness implies more relaxed attitude to accepting applicants, whereas a higher strictness implies stronger vetting. This is achieved through adjusting the hyperparameters used for the K Means Classfiication model.

## Sources
Data: https://www.kaggle.com/datasets/samuelcortinhas/credit-card-approval-clean-data 
Data origin: https://archive.ics.uci.edu/ml/datasets/Credit+Approval?msclkid=200008bdc4a311ec9f500a3245a2bfb1
Model: https://www.kaggle.com/code/sns5154/credit-approval-system-val-92-86-test-82-61 
