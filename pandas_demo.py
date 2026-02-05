import pandas as pd 
# series = pd.Series([10,20,30,40,50])
# print(series)

# data = {
#     "Name" : ["Emp1","Emp2","Emp3","Emp4","Emp5","Emp6","Emp7"],
#     "Age": [20,22,24,26,28,30,32],
#     "Salary": ["1lakh","2lakh","2.5lakh","3lakh","3.5lakh","4lakh","4.5lakh"]
# }
# res = pd.DataFrame(data)
# print(res)
# print(res.head())
# print(res.tail())
# print(res.shape)
# print(res.columns)
# print(res.info())

res = pd.read_excel("students.xlsx")
print(res[(res["Marks"]>80) & (res["Age"]>21)])
print(res[res["Marks"]>80])
print(res)
print(res["Rollno"])
print(res[["Name","Marks"]])
print(res.loc[0])
print("-----------------")
print(res.iloc[0])

res = pd.read_excel("students.csv")
res["passed"] = res["Marks"] > 80
print(res)
res.drop(["passed", "Name"], axis=1, inplace=True)
print(res)
res.drop([1,3], inplace=True)
print(res)
print(len(res))



