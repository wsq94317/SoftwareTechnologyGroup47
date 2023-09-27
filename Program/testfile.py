import pandas as pd
import sqlite3
database = sqlite3.connect("database/airbnbdata.db")
res0 = database.execute("SELECT name FROM sqlite_master WHERE type='table';")
res = database.execute("SELECT * FROM Surburb")
res1 = database.execute("SELECT * FROM House")
res2 = database.execute("SELECT * FROM Calendar")
res3 = database.execute("SELECT * FROM Reviews")
for item in res:
    print(item)
for item in res0:
    print(item)
for item in res1:
    print(item)

for item in res2:
    print(item)

for item in res3:
    print(item)