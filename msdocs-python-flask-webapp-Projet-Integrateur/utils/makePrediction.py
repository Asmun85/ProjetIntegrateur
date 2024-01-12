import pickle
import pandas as pd

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

def computeFollowersBotHumanPercentage(probabilities: list):
  # Utilisez zip pour séparer les deux éléments dans deux listes distinctes
    trust_bot, trust_human = zip(*probabilities)

    # Calculez les moyennes
    average_bot = sum(trust_bot) / len(trust_human)
    average_human = sum(trust_bot) / len(trust_human)

    return average_bot, average_human