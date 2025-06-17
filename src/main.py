''' ETL Pipeline to Extract, Load and Transfrom Data in python

Task 1 = Extract data from a CSV file. This will be done by calling the load_data.py module and calling a funtion.
         This funtion should be able to accept an argument, which is the file to work with.
         This file will be passed as an input in the terminal when the python script is called.
         The data in this file will be extracted and passed to a pandas dataframe and result will be printed out.
'''

from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator 
import pandas as pd
import sys
import argparse


print("********************Running ETL Pipeline*******************************\n")

try:
    raw_data = sys.argv[1]  # get the raw data from the terminal
    sensor_raw_data = load_csv(raw_data) # extract the data using
    print(sensor_raw_data.head())

    try:
        cleaned_data = clean_sensor_data(sensor_raw_data) # try to clean the data

        try:
            print(type(cleaned_data))
            evaluator = WaterQualityEvaluator()
            evaluated_data = evaluator.evaluate_data(cleaned_data)
            if evaluated_data is not None:
                evaluated_data.to_csv("data/results.csv", index=False)
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


except IndexError as e:
    print("Please provide source data")
