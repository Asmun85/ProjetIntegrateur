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