import requests 

url_user           = "https://twttrapi.p.rapidapi.com/get-user"
# url_user_followers = "https://twttrapi.p.rapidapi.com/user-followers"

def getUserInfos(username):
  querystring = {"username":username}

  headers = {
    "X-RapidAPI-Key": "b1d2779d85msh19c01a549d561f5p1154a4jsnd9c5aaeb5c5b",
    "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
  } 
  response = requests.get(url_user, headers=headers, params=querystring)
  ## Returns the Json(dictionnary) of the API call for User_infos
  return response.json()