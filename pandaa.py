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

# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Vikas"],
#     "Age": [20, 21, 19, 22, 20],
#     "Marks": [78, 91, 65, 88, 72],
#     "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"]
# }

# df = pd.DataFrame(data)
# print(df.shape)
# print(df.Marks)
# print(df["Marks"] > 80)
# print(df["Marks"].mean())
# print(df.describe())

# // learn the loc and iloc 
# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Vikas", "Priya"],
#     "Age": [20, 21, 19, 22, 20, 21],
#     "Marks": [78, 91, 65, 88, 72, 95],
#     "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Delhi"]
# }

# df = pd.DataFrame(data)
# print(df[["Name","Marks"]])
# print(df.columns)
# print(df.loc[1])
# print(df[(df["Marks"] > 80 )& (df["Age"]>20)])
# print(df.sort_values("Marks"))
# print(df.loc[df["City"]=="Delhi"])

#small student analyser
# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Vikas", "Priya"],
#     "Age": [20, 21, 19, 22, 20, 21],
#     "Marks": [78, 91, 65, 88, 72, 95],
#     "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Delhi"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df["Marks"]>80)
# print(df["Marks"].max())
# print(df.sort_values("Marks",ascending = False)
# def check_result(marks):
#     if marks >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# df["Result"] = df["Marks"].apply(check_result)

# print(df)

import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Riya"],
    "Age": [20, 21, None, 19, 21],
    "Marks": [78, 91, None, 88, 91],
    "City": ["Delhi", "Jaipur", "Delhi", None, "Jaipur"]
}

df = pd.DataFrame(data)

# print(df)
# print(df.isnull())
# print(df.isna())
# remove the null contains rows
# df.isnull()
# df = df.dropna()
# print(df)
# fill the value of the null by the mean

# df.isnull()
# Mean =df["Marks"].mean()
# df["Marks"]= df["Marks"].fillna(Mean)
# print(df)
# to print the duplicate value
# df.duplicated()
# print(df.drop_duplicates())
print(df["Name"].dtype)
print(df["Age"].dtype)
print(df["Marks"].dtype)
