import os
import json
import pandas as pd
import requests

from constants import FILE_URL, FILE_NAME
from utils import get_data


# реализовать сохранение в файл джейсон по урл
data = get_data(FILE_URL, FILE_NAME)
print(data)

"""
def draw_plots(data):
    table = pd.read_json(data)
    print(table.head())


draw_plots(data)
"""
"""
→ reads json file passed as parameter as a pandas dataframe
→ draws plot for comparing different columns
→ saves plots in a folder called “plots”
→ returns paths to all plots
"""
