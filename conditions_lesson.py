#progrgam for find the age of user

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 17: #if we use only < or > it will be mistake (edge case)
    print("You are a teenager. ")
else:
    print("You are an adult")