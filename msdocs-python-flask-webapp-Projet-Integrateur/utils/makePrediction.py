import pickle
import pandas as pd
import numpy as np

model  = pickle.load(open('../finalModel/best_rf_model.pkl','rb'))
scaler = pickle.load(open('../finalModel/scaler','rb'))

def predictionUser(user_data : dict):
  df = pd.DataFrame.from_dict([user_data])
  scaled_data = scaler.transform(df)
  predictions = model.predict(scaled_data)
  probabilities = model.predict_proba(scaled_data)


  print("Predictions:", predictions)
  print("Trust Percentages:", probabilities)

  return predictions , probabilities

## {prediction : 'human' or 'bot', 'trust_bot' : value , 'trust_human' : value}

def predictionUserFollowers(followers_data : list):
  all_predictions = []
  all_probabilities = []
  
  for follower_data in followers_data:
        predictions, probabilities = predictionUser(follower_data)

        all_predictions.append(predictions)
        all_probabilities.append(probabilities)
    

  return all_predictions , all_probabilities

def computeBotRatio(all_predictions : list):
  return all_predictions.count("bot")/len(all_predictions)

def computeFollowersBotHumanPercentage(probabilities):
    trust_bot, trust_human = zip(*[(arr[0][0], arr[0][1]) for arr in probabilities])

    # Convertissez les listes en tableaux NumPy
    trust_bot_array = np.array(trust_bot)
    trust_human_array = np.array(trust_human)

    # Calculez les moyennes
    average_bot = np.mean(trust_bot_array)
    average_human = np.mean(trust_human_array)

    return average_bot, average_human