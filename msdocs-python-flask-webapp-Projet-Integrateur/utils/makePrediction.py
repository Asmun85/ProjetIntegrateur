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
  all_human_probabilities = []
  all_bot_probabilities = []
  
  for follower_data in followers_data:
        predictions, probabilities = predictionUser(follower_data)
        print(probabilities)
        all_predictions.append(predictions)
        if predictions == 'human':
           all_human_probabilities.append(probabilities[0][1])
        else : 
           all_bot_probabilities.append(probabilities[0][0])
    

  return all_predictions , all_human_probabilities, all_bot_probabilities

def computeBotRatio(all_predictions : list):
  return all_predictions.count("bot")/len(all_predictions)

def computeFollowersBotHumanPercentage(humanprobabilities, botprobabilities):
    # Convertissez les listes en tableaux NumPy
    trust_bot_array = np.array(botprobabilities)
    trust_human_array = np.array(humanprobabilities)

    # Calculez les moyennes
    average_bot = round(np.mean(trust_bot_array),4)
    average_human = round(np.mean(trust_human_array),4)

    return average_bot, average_human