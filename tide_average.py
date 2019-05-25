import numpy as np
import pandas as pd
import os

def get_csv():

	data = pd.read_csv("~/Documents/Wind/tide_data.csv")

	return data


def get_average_tide_difference():

	data = get_csv()

	low_tides = data['Low Pred(cm)'] 

	high_tides = data['High Pred(cm)'] 

	difference = high_tides - low_tides

	lowest_tide = data.iloc[low_tides.idxmin()]

	highest_tide = data.iloc[high_tides.idxmax()]

	print("Date: " + lowest_tide['Date'] + ' ' + lowest_tide['Time Low'] + "\nTide Height: " + str(lowest_tide['Low Pred(cm)']) + "cm")

	print("Date: " + highest_tide['Date'] + ' ' + highest_tide['High Time'] + "\nTide Height: " + str(highest_tide['High Pred(cm)']) + "cm")

	print(difference.mean())


get_average_tide_difference()