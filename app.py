import pickle
import flask

from flask import Flask, request

app = Flask(__name__)


#loading the ML model
model_pickle = open("./classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "Pinging the NEWWWW model successful!!"}


@app.route("/predict", methods=['POST'])
def prediction():

    # loan_req = request.get_json()

    # if loan_req['Gender'] == "Male":
    #     gender = 0
    # else:
    #     gender = 1
    
    # if loan_req['Married'] == "Unmarried":
    #     marital_status = 0
    # else:
    #     marital_status = 1
        
    # if loan_req['Credit_History'] == "Uncleared Debts":
    #     credit_history = 0
    # else:
    #     credit_history = 1
    
    # applicant_income = loan_req['ApplicantIncome']
    # loan_amt = loan_req['LoanAmount'] / 1000

    # input_data = [[gender, marital_status, applicant_income, loan_amt, credit_history]]


    price_req = request.get_json()

    company = price_req['company']
    model_name = price_req['model_name']
    year = price_req['year']
    kms_driven = price_req['kms_driven']
    fuel_type = price_req['fuel_type']

    input_data = [[company, model_name, year, kms_driven, fuel_type]]

    # generate inference
    # prediction = clf.predict(input_data)
    # print(prediction)

    return {"Predicted price of your car": 458894.10960853}

@app.route("/get_params", methods=['GET'])
def get_application_params():

    parameters = {
        "Company": "Maruti",
        "ModelName": "Swift",
        "Year": 2011,
        "KMSDriven": 50000,
        "FuelType": "Petrol"
        }
    return parameters
