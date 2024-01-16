import os
import requests 
from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
app = Flask(__name__)
port_number = 5001

key= "0e9f15a352msh4ac3bd376e93cb7p16f666jsnd96a9dd3dfad"
url_user           = "https://twttrapi.p.rapidapi.com/get-user"
url_user_followers = "https://twttrapi.p.rapidapi.com/user-followers"


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/userInfos/<name>', methods=['Get'])
def callUserInfos(name):
    if name:
        print('Request Get UserInfos with name=%s' % name)
        querystring = {"username":name}

        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        } 
        response = requests.get(url_user, headers=headers, params=querystring)
        ## Returns the Json(dictionnary) of the API call for User_infos
        if response.status_code != 200:
            return jsonify({'error': response.json()['message']}), response.status_code
        else:
            return response.json()
    else:
        content = 'Request for hello page received with no name or blank name'
        ## Render Template Error
        return content ,201


@app.route('/userFollowersInfos/<name>')
def callUserFollowersInfos(name):
    if name:
        print('Request Get UserFollowersInfos with name=%s' % name)
        querystring = {"username":name,"count":20}

        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        } 
        response = requests.get(url_user_followers, headers=headers, params=querystring)
        ## Returns the Json(dictionnary) of the API call for User_infos
        if response.status_code != 200:
            return jsonify({'error': response.json()['message']}), response.status_code
        else:
            return response.json()
    else:
        content = 'Request for hello page received with no name or blank name'
        ## Render Template Error
        return content ,201


if __name__ == '__main__':
   app.run(debug=True,port=port_number)
