import json
from datetime import datetime

def extract_features(data):

    # Extract the desired features
    created_at_str = data["created_at"]
    created_at_datetime = datetime.strptime(created_at_str, '%a %b %d %H:%M:%S %z %Y')
    count = data['statuses_count']
    # Getting today's date
    today_datetime = datetime.now(created_at_datetime.tzinfo)

    # Calculating the age of the account in days
    account_age_days = (today_datetime - created_at_datetime).days
    features = {
        'default_profile': data['screen_name'] == 'default',  #'default_profile' means default screen name
        'default_profile_image': data['profile_image_url_https'].endswith('default_profile_normal.png'),
        'favourites_count': data['favourites_count'],
        'followers_count': data['followers_count'],
        'friends_count': data['friends_count'],
        'geo_enabled': data['geo_enabled'],
        'statuses_count': data['statuses_count'],
        'verified': data['verified'],
        'average_tweets_per_day' : round(count / account_age_days),
        'account_age_days' : account_age_days
    }
    #Returns a dictionnary of the features used for the training 
    return features

