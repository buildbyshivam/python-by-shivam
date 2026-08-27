# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha"],
#     "Age": [20, 21, 19, 22],
#     "Marks": [78, 91, 65, 88]
# }

# df = pd.DataFrame(data)

# # print(df)
# print(df.head)
# print(df.tail)
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Vikas"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [78, 91, 65, 88, 72],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df.shape)
print(df.Marks)
print(df["Marks"] > 80)
print(df["Marks"].mean())
print(df.describe())