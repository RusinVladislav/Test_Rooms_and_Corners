import os
import random

import pandas as pd
from matplotlib import pyplot as plt

from constants import FILE_URL
from utils import get_data


def draw_plots():
    data_file = get_data(FILE_URL)
    table_data = pd.read_json(data_file)
    name_colum = [name for name in table_data]
    for name in name_colum[1:]:
        fig, axs = plt.subplots(figsize=(15, 4))
        plt.title(name)
        table_data[name].plot.area(
            ax=axs,
            subplots=True,
            color=(random.random(), random.random(), random.random(), random.random())
        )
        axs.set_ylabel(name)
        fig.savefig(f"plot/{name}.jpg")

    return os.path.abspath('plot')


if __name__ == "__main__":
    table = draw_plots()
