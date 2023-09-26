import pandas as pd

df = pd.read_csv("../datasets/listings_dec18.csv")
count = 0
for ind, ele in df.iterrows():
    # print("ind______________________________")
    # print(ind)
    # print("ele____________")
    # print(ele)
    if ele['neighbourhood'].isnull() :
        count += 1
print(count)