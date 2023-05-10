import csv

import pandas as pd

# read csv from dataset1.csv

with open('dataset1.csv', 'r') as file:
    # pd dataframe from csv
    dataframe = pd.read_csv(file, delimiter=';', header=None)

print(dataframe)

newdf = pd.DataFrame()
for index, row in dataframe.iterrows():
    newrow = []
    for i in range(0, len(row)):
        data = row[i]
        # split by ,
        data = data.split(',')
        # if less than 3 parts, just append
        if len(data) < 3:
            newrow.append(data[0])
            continue
        if len(data) == 3:
            for part in data:
                newrow.append(part)
            continue
        # for each part of data
        inner_index = 0
        while inner_index < len(data):
            part = data[inner_index]
            # if last past, just append
            if inner_index + 1 == len(data):
                newrow.append(part)
                inner_index += 1
                continue
            if data[inner_index + 1] == '0':
                newrow.append(part)
                inner_index += 1
                continue

            # add this and next part together
            newrow.append(part + '.' + data[inner_index + 1])
            # skip next part
            inner_index += 2
    newdf = newdf.append(pd.Series(newrow), ignore_index=True)

print(newdf)
# to csv
newdf.to_csv('dataset1_fixed.csv', index=False, header=False)