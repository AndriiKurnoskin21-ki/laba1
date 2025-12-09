#ЗМІННІ ВСІХ ТИПІВ
age = 20                         # int
temperature = 36.6               # float
name = "Андрій"                  # str
is_student = True                # bool
grades = [90, 85, 100]           # list
coords = (10, 20)                # tuple
nums = {1, 2, 3}                 # set
user = {"name": "Андрій"}        # dict

# ВИВЕДЕННЯ ЗНАЧЕННЯ ТИПУ
print(f"age, {type(age)} : {age}")
print(f"temperature, {type(temperature)} : {temperature}")
print(f"name, {type(name)} : {name}")
print(f"is_student, {type(is_student)} : {is_student}")
print(f"grades, {type(grades)} : {grades}")
print(f"coords, {type(coords)} : {coords}")
print(f"nums, {type(nums)} : {nums}")
print(f"user, {type(user)} : {user}")

#ОСНОВНІ ОПЕРАТОРИ
a, b = 10, 3

print(a + b)   # додавання
print(a - b)   # віднімання
print(a * b)   # множення
print(a / b)   # ділення
print(a % b)   # остача
print(a ** b)  # степінь

print(a > b)   # порівняння
print(a == b)

print(True and False)  # логічні
print(True or False)
print(not True)

c = 5
c += 2       # присвоєння
print(c)

print("Добрий день " + name)  # конкатенація
