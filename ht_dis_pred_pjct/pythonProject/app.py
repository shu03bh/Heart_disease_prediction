from flask import Flask, request, render_template

import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('models/rf_classifier.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))


def predict(model, scaler, male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose):

    #encoding categorical variable

    male_encoded = 1 if male.lower() == "male" else 0
    currentSmoker_encoded = 1 if currentSmoker.lower() =="yes" else 0
    BPMeds_encoded = 1 if BPMeds.lower() == "yes" else 0
    prevalentStroke_encoded = 1 if prevalentStroke.lower() == "yes" else 0
    prevalentHyp_encoded = 1 if prevalentHyp.lower() == "yes" else 0
    diabetes_encoded = 1 if diabetes.lower() == "yes" else 0


    #prepare features array
    features = np.array([[male_encoded, age, currentSmoker_encoded, cigsPerDay, BPMeds_encoded, prevalentStroke_encoded, prevalentHyp_encoded, diabetes_encoded, totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    #scalling
    scaled_features = scaler.transform(features)

    #predict by model
    result = model.predict(scaled_features)

    return result[0]


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pred", methods=['GET', 'POST'])
def pred():
    if request.method =='POST':
        male = request.form.get('gender')
        age = int(request.form['age'])
        currentSmoker = request.form['currentSmoker']
        cigsPerday = int(request.form['cigsPerDay'])
        BPMeds = request.form['BPMeds']
        prevalentStroke = request.form['prevalentStroke']
        prevalentHyp = request.form['prevalentHyp']
        diabetes = request.form['diabetes']
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])



        prediction = predict(model, scaler, male, age, currentSmoker, cigsPerday, BPMeds, prevalentHyp, prevalentStroke, diabetes, sysBP, diaBP, totChol, BMI, glucose, heartRate)
        prediction_text = "The patient has heart disease!" if prediction == 1 else "The patient does not have any heart disease!"

        return render_template('index.html', prediction = prediction_text)


if __name__ == '__main__':
    app.run(debug = True)