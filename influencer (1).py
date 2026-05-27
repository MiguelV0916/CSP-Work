#Miguel Velasquez
#init
import pandas as pd
#funcs
data = pd.read_csv("influencer.csv")


month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subs = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filter = []

def humble(high):
    for i in range(len(month)):
        if views[i] < high:
            filter.append([i])
    print(filter)
    filter.clear()
humble(2000)

def gold(high):
    for i in range(len(month)):
        if subs[i] > high:
            filter.append([i])
    print(filter)
    filter.clear()
gold(50000)

def scandle(cash):
    for i in range(len(month)):
        if revenue[i] == cash:
            filter.append([i])
    print(filter)
    filter.clear()

scandle(0)
