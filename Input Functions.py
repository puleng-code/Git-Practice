"""age = input("Enter your age: ")
new_age = float(age) + 50
print(new_age)"""

def age_func(age):
    new_age = float(age) + 50
    return age

age2 = input("Enter your age: ")
print(age_func(age2))