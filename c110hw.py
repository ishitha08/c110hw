import statistics
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import random
import csv
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['Math_score'].tolist()

population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)

print('population mean -',population_mean)
print('population_std_deviation -',population_std_deviation)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['temp'],show_hist=False)
    fig.show()