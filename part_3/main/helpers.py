import imp
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
import pandas as pd
from datetime import date
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler 

from pandas_datareader import data as pdr
import yfinance as yf
from . import model


def make_prediction(stock):
    try:
        start = '2010-01-01'
        # end = '2022-06-05'

        d = date.today()
        today = d.strftime("%Y-%m-%d")

        stock = stock.upper()
        df = pdr.get_data_yahoo(stock, start=start, end=today)

        dates = df.index
        dates = [d.strftime("%Y-%m-%d") for d in dates]

        pred_df = pd.DataFrame(df["Close"])
        
        scaler = MinMaxScaler(feature_range=(0,1))

        data_arr = scaler.fit_transform(pred_df)

        window = 80

        x_vals = []
        y_vals = []

        last_vals = data_arr[len(data_arr) - window:]

        for i in range(window, data_arr.shape[0]):
            x_vals.append(data_arr[i-window:i])
            y_vals.append(data_arr[i,0])

        x_vals, y_vals, last_vals = np.array(x_vals), np.array(y_vals), np.array([last_vals])
        

        model = load_model('stock_prediction_model.h5')
        predicted_vals = model.predict(x_vals)

        future_val = model.predict(last_vals)

        unscaled_predicted_vals = scaler.inverse_transform(predicted_vals)
        unscaled_y_actual = scaler.inverse_transform(np.reshape(y_vals, (y_vals.shape[0], 1)))
        future_val_unscaled = scaler.inverse_transform(future_val)

        predictions = unscaled_predicted_vals[:, 0].tolist()
        actual = unscaled_y_actual[:, 0].tolist()
        future_prediction = str(round(future_val_unscaled[0][0], 2))

        return predictions, actual, future_prediction, dates, ""
    except:
        return [], [], 0.0, [], "failed"

