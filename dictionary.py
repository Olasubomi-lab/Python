# Creating a dictionary
# Method 1 
student = {
    "name":"Subomi",
    "age":16,
    "grade":"twelve"
}
print(student)

# Method 2

d3 = dict({
    "name":"Subomi",
    "age":16,
    "grade":"twelve"
})
print(d3)

# Keys cannot be repeated
student1 = {
    "name":"Subomi",
    "age":16,
    "grade":"twelve",
    "name":"Inka"
}
print(student1)

# Empty dictionary
d1 = {}
print(d1)

# Dictionary with mixed keys
d2 = {
    "name":"Grace",
    1:[1,2,3,4]
}
print(d2)

# Accessing the dictionary 
student3 = {
    "Name":"Greg",
    "Age":10,
    "Grade":5
}
print(student3["Age"])
print(student3["Name"])

# Updating a dictionary
student3["Name"] = "Sarah"
print(student3["Name"])

# Deleting a key
student4 = {
    "Name":"Greg",
    "Age":10,
    "Grade":5,
    "Year":5
}
del student4["Year"]
print(student4)

# Nested dictionary 
people = {
    1:{"Name":"Damian","Age":20},
    2:{"Name":"Sam","Age":13}
}

print(people)

# Accessing nested dictionary
print(people[1]["Name"])
print(people[2]["Age"])
