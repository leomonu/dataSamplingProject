import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go


df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population mean",population_mean)
print("Standered Deviation",std_deviation)

fig = ff.create_distplot([data],["claps"],0,show_hist=False)
fig.show()

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["claps"],show_hist=False)
    # fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "MEAN"))
    fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value)
        
    mean = statistics.mean(dataset)
    return mean


def standerd_deviation():
    mean_list = []
    for i in range(1,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("Standerd Deviation Of Sampling Distribution :",std_deviation)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()
standerd_deviation()