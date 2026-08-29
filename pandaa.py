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
