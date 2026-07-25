student = {"name":"shivam","age":18,"city":"jaipur"}
print(student)
print(student["name"])
student["job"] = "no"
student["age"] = 19
print(student)
student.pop("city")
print(student)
for key,value in student.items():
    print(key,":",value)