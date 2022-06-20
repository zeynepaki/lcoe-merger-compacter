import pandas as pd

df = pd.DataFrame({'A': range(1, 6),

                   'B': range(10, 0, -2),

                   'C': range(10, 5, -1)})
ten = 10
ft = df.query('B == @ten')
print(df)

for index, row in df.iterrows():
    print(df.iat[index, 2])

print(ft)
