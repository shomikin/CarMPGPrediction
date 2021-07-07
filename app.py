import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('SB-MPG')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
	cyl = int(request.form['cyl'])
	Disp = int(request.form['Disp'])
	Power = int(request.form['Power'])
	Weight = int(request.form['Weight'])
	Acc = float(request.form['Acc'])
	year = int(request.form['Year of Manufacture (Enter in YY format)'])
	CarType = int(request.form['Car Type (Enter 1 for cars with cylinder 3,4 and 5, 0 for cars with cylinder 6 and 8)'])
	Origin = request.form['Coubtry']
	OriginDummy = ohe.transform(np.array([[Origin]]))
	compatibleFeatureSet = np.concatenate((OriginDummy,np.array([[cyl,Disp,Power,Weight,Acc,year,CarType]])), axis=1)
	mpg=model.predict(compatibleFeatureSet)


    return render_template('index.html', prediction_text='Estimated Mpg is  $ {}'.format(round(mpg[0][0]))


if __name__ == "__main__":
    app.run(debug=True)
