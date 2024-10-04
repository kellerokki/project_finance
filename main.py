import pandas as pd #Allows to load in the csv file and work with it faster
import csv #Imports csv file extension
from datetime import datetime #Module built in Python, that allows to work with dates and times.

class CSV:
    CSV_file = "finance_data.csv" #Defined a class with class variable

    @classmethod #Class decoration, has access to class itself, not to it´s instance.
    def initialize_csv(cls): #Class method
        try:
            pd.read_csv(cls.CSV_file) #Trying to read closed CSV_file
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"]) #If file not found, create one with given list.""
            #Data Frame in Pandas is an object, that allows easy access to rows and columns from something.