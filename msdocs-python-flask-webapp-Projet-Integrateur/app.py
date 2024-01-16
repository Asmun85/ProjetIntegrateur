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
       try:
            extracted_user_features = userInfosProcessor.extract_user_features(response)
            res = makePrediction.predictionUser(extracted_user_features)
            res[1][0][1] = round(res[1][0][1],4)
            res[1][0][0] = round(res[1][0][0],4)
            return render_template('user.html', name = name, res = res)
       except KeyError as e:
            return render_template('error.html', name = name)   
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
        try:
            extracted_followers_features = userInfosProcessor.extract_followers_features(response)
            predictions, humanprobabilities, botprobabilities = makePrediction.predictionUserFollowers(extracted_followers_features)
            botRatio = makePrediction.computeBotRatio(predictions)
            botpercentage, humanpercentage = makePrediction.computeFollowersBotHumanPercentage(humanprobabilities, botprobabilities)
            botRatio = round(botRatio,4)
            botpercentage = round(botpercentage,4)
            humanpercentage = round(humanpercentage,4)
            return render_template('follower.html', name = name, botRatio = botRatio, followersBotHumanPercentage = [botpercentage, humanpercentage])
        except KeyError as e:
            return render_template('error.html', name = name) 
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)
