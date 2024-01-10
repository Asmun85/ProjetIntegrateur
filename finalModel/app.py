from flask import Flask, request
from pickle import load
import numpy as np

app=Flask(__name__)

@app.route('/user_prediction',methods=['GET'])
def user_prediction():
  model = load(open('best_rf_model.pkl','rb'))
  scaler = load(open('scaler','rb'))
