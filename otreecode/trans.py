import pandas as pd

file = pd.read_excel('trans1.xlsx')
print(file)

num = list(file['num'])
region = list(file['region'])
print(num, region)

output = list
for i in range(90):
    print(f"[{num[i]}, '{region[i]}'],")