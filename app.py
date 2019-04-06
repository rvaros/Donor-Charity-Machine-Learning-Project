import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    print (to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1,-1)
    loaded_model = pickle.load(open("tree_classifier.pkl","rb"))
    predict = loaded_model.predict(to_predict)
    return predict[0]

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
         to_predict_list = request.form.to_dict()
         to_predict_list=list(to_predict_list.values())
         to_predict_list = list(map(int, to_predict_list))
         predict = ValuePredictor(to_predict_list)

    if int(predict)==1:
           prediction='Potential Donor Identified'
    else:
            prediction='Not a Potential Donor'
    return render_template("predict.html",prediction=prediction)

if __name__ == '__main__':
    app.run(port=5000, debug=True)