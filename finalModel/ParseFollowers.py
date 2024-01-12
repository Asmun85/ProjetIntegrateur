import requests

url = "https://twttrapi.p.rapidapi.com/user-followers"

querystring = {"username":"Santoryuu85","count":"20"}

headers = {
	"X-RapidAPI-Key": "b1d2779d85msh19c01a549d561f5p1154a4jsnd9c5aaeb5c5b",
	"X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
}
user_followers = []
response  = requests.get(url, headers=headers, params=querystring)
followers = response.json()["data"]["user"]["timeline_response"]["timeline"]["instructions"][3]["entries"]
for f in followers:
  if (f["content"]["__typename"] == 'TimelineTimelineItem'):
    user_followers.append(f["content"]["content"]["userResult"]["result"]["legacy"])
    
for followers in user_followers:
  print("-------------------------------------")
  print(followers)

		




