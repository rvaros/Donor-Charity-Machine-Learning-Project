import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


def ValuePredictor(result_list):
    print (result_list)
    result = np.array(result_list).reshape(1,-1)
    loaded_model = pickle.load(open("tree_classifier.pkl","rb"))
    predict = loaded_model.predict(result)
    return predict[0]

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
         result_list = request.form.to_dict()
         result_list=list(result_list.values())
         result_list = list(map(int, result_list))
         predict = ValuePredictor(result_list)

    if int(predict)==1:
           prediction='Potential Donor Identified'
    else:
            prediction='Not a Potential Donor'
    return render_template("predict.html",prediction=prediction)

if __name__ == '__main__':
    app.run(port=5000, debug=True)