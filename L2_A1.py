name = "Penguin" #String(str) Datatype
age = 17 #Integer(int) Datatype
is_student = True #Boolean(bool) Datatype
weight = 7.12 #Float Datatype

print("Name :", name)
print("Datatype of name is :", type(name))
print("Age :", age)
print("Datatype of age is :", type(age))
print("is_student :", is_student)
print("Datatype of is_student is :", type(is_student))
print("Weight :", weight)
print("Datatype of weight is:", type(weight))

print("\n After Type Casting...")
age = str(age)
print(age)
print("Datatype of age is :", type(age))
weight = int(weight)
print(weight)
print("Datatype of weight is:", type(weight))