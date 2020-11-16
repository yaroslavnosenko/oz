import pandas as pd
import datetime

lines = tuple(open('data.csv', 'r'))
rows = map(lambda line: line.split(','), lines)
rows = map(lambda row: row[-15:], rows) # get 15 cols from the end
rows = map(lambda row: row[:len(row)-4], rows) # remove last 4 empty rows
rows = [[r.strip() for r in q] for q in rows] # strip each item
names = rows[0]
data = rows[1:]
df = pd.DataFrame(data, columns=[names])

err_indexes = []
for idx, row in df.iterrows():
    try:
        deadline = row.values[3]
        datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
    except:
        err_indexes.append(idx)
df = df.drop(df.index[[err_indexes]])
df.to_csv('data_prep.csv', index=False)
