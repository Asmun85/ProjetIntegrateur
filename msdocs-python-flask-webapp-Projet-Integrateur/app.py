import os
import requests , pickle
from utils import userInfos , userInfosProcessor , makePrediction
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)



app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
   
@app.route('/user', methods=['POST'])
def user():
   name = request.form.get('name')

   if name:
       print('Informations on user for username=%s' % name)
       response = userInfos.getUserInfos(name)
       print(response)
       print("------------------------------------------------------------------------")
       print("------------------- Parsing the json to a df ---------------------------")
       extracted_features = userInfosProcessor.extract_features(response)
       res = makePrediction.predictionUser(extracted_features)
       print(res)
       return render_template('user.html', name = name, res = res)    
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/follower', methods=['POST'])
def follower():
   name = request.form.get('name')

   if name:
       print('Informations on user for username=%s' % name)
       response = userInfos.getUserFollowersInfos(name)
       print(response)
       print("------------------------------------------------------------------------")
       print("------------------- Parsing the json to a df ---------------------------")
       extracted_followers_features = userInfosProcessor.extract_followers_features(response)
       predictions, probabilities = makePrediction.predictionUserFollowers(extracted_followers_features)
       botRatio = makePrediction.computeBotRatio(predictions)
       followersBotHumanPercentage = makePrediction.computeFollowersBotHumanPercentage(probabilities)
       
       return render_template('follower.html', name = name, botRatio = botRatio, followersBotHumanPercentage = followersBotHumanPercentage)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)
