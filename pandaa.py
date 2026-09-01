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

# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Riya"],
#     "Age": [20, 21, None, 19, 21],
#     "Marks": [78, 91, None, 88, 91],
#     "City": ["Delhi", "Jaipur", "Delhi", None, "Jaipur"]
# }

# df = pd.DataFrame(data)

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
# print(df["Name"].dtype)
# print(df["Age"].dtype)
# print(df["Marks"].dtype)

# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Riya"],
#     "Age": [20, 21, None, 19, 21],
#     "Marks": [78, 91, None, 88, 91],
#     "City": ["Delhi", "Jaipur", "Delhi", None, "Jaipur"]
# }

# df = pd.DataFrame(data)
# print(df.shape)
# print(df.columns)
# # print(df.rows)
# print(df.dtypes)
# print(df.info)
# mean = df["Age"].mean()
# df["Age"] = df["Age"].fillna(mean)
# df["Age"] = df["Age"].astype(int)
# print(df["Age"].dtype)

# print(df["Marks"].mean())
# print(df["Marks"].max())
# print(df["Marks"].min())
# print(df["Marks"].sum())

# print((df["Marks"] > 80) & (df["Age"]>20))
# print(df[(df["Marks"] > 80 )& (df["Age"]>20)])
# sorting the values udsing pandas
# mean = df["Marks"].mean()
# df["Marks"] = df["Marks"].fillna(mean)
# print(df.sort_values("Marks"))
# print(df.sort_values("Marks",ascending = False))
# small student analyser
# Total Students:
# Average Marks:
# Highest Marks:
# Lowest Marks:

# Top Students:
# Name + Marks where Marks > 80

# Sorted Students:
# Highest → Lowest

# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya", "Rahul", "Neha", "Riya"],
#     "Age": [20, 21, None, 19, 21],
#     "Marks": [78, 91, None, 88, 91],
#     "City": ["Delhi", "Jaipur", "Delhi", None, "Jaipur"]
# }

# df = pd.DataFrame(data)
# print(df.shape[0])
# print(len(df))
# print(df["Marks"].mean())
# print(df["Marks"].max())
# print(df["Marks"].min())
# df["Marks"]= (df["Marks"]>80)
# print(df["Marks"], ["Name"])

# print(df.loc[df["Marks"] > 80, ["Name", "Marks"]])

import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Vikas", "Priya", "Arjun", "Kavya"],
    "Age": [20, 21, 19, 22, 20, 21, 22, 20],
    "Marks": [78, 91, 65, 88, 72, 95, 82, 76],
    "City": ["Delhi", "Jaipur", "Delhi", "Pune", "Mumbai", "Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

# print(df)
# print(df.groupby("City")["Marks"].mean())
# print(df.groupby("City")["Marks"].max())
# print(df.groupby("City")["Marks"].min())
# print(df.groupby("City")["Marks"].agg(["max" , "min" ,"mean"]))
print (df.groupby("City")["Marks"].count())
