import pandas as pd
from constants import FILE_URL
from utils import get_data

data = get_data(FILE_URL)


def draw_plots(link_data):
    table = pd.read_json(data)
    return table


data_test = draw_plots(FILE_URL)

print(data_test)
