import requests 
key = "3efe59a334msha059c985bfdfa0fp19b733jsn38325d8631fd"
# key = "b1d2779d85msh19c01a549d561f5p1154a4jsnd9c5aaeb5c5b"


url_user           = "https://twttrapi.p.rapidapi.com/get-user"
url_user_followers = "https://twttrapi.p.rapidapi.com/user-followers"

def getUserInfos(username):
  querystring = {"username":username}

  headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
  } 
  response = requests.get(url_user, headers=headers, params=querystring)
  ## Returns the Json(dictionnary) of the API call for User_infos
  return response.json()


def getUserFollowersInfos(username):
  querystring = {"username":username,
                 "count": "20"}

  headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
  } 
  response = requests.get(url_user_followers, headers=headers, params=querystring)
  ## Returns the Json(dictionnary) of the API call for User_infos
  return response.json()

