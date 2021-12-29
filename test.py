import pandas as pd

data = pd.read_csv('data.csv')

for d in data.values:
    # print(data.values[1][1])
    print(d[2])


# for d in data.values:
#     # read column by index
#     print(d[2])
#     break
