import numpy as np

data_type = [("name", "S15") , ("age", int), ("height", float)]

student_details = [("John", 17, 67.90), ("Mia", 16, 62.53), ("Sam",16,63.23), ("Xander",18, 69.90)]
students = np.array(student_details, dtype=data_type)

print("original array:-")
print(students)

print("sort by height :-")
print(np.sort(students, order= "height"))

print("sort by age :-")
print(np.sort(students, order = "age"))

print("sort by name :-")
print(np.sort(students, order = "name"))