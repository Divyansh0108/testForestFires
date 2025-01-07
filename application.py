from flask import Flask, request, jsonify, render_template #import main Flask class and request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#importing regressor and scaler
model = pickle.load(open('models/regressor.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

application = Flask(__name__) #create the Flask app
app = application #alias

@app.route('/') #define the default route
def index():
    return render_template('index.html') #return index.html

@app.route('/predictdata', methods=['GET','POST']) #define the predictdata route with GET and POST methods
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FMMC = float(request.form.get('FMMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Region = float(request.form.get('Region'))
        
        new_scaled_data = scaler.transform([[Temperature, RH, Ws, Rain, FMMC, DMC, ISI, Region]])
        result = model.predict(new_scaled_data)
        
        return render_template('home.html', result = result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__': #start the server with the 'run()' method
    app.run(debug=True) #enable debug mode