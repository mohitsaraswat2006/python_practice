# STORES VALUES IN KEY:VALUE PAIRS INSIDE CURLY BRAKET{}.
info = {
    "key" : "value",
    "name" : " mohit saraswat",
    "learning " : "python",
    "age" : 24,
    "is adult" : True,
    "marks" : 95.3,
    "subjects" : ["python","c", "javacsript", "html"],
    "marks" : ("maths","hindi","english","science") 
}
print(info)
print(type(info))

# to print individual values.
print(info["marks"])
print(info["name"])

info["ram"] = "hanuman"
info["surname"] = "saraswat"

null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)

# NESTED DICTIONARIES.

student = {
    "name" : 6,
    "subjects" : {
        "phy" : 78,
        "maths" : 45,
        "hindi" : 98
    }
}
print("student")

# methods in dictionary.
print(student.keys())
print(list(student.keys()))
print(len(student))

# to print values.
print(student.values())

# returns all items.
print(student.items())
print(list(student.items()))

# to return key.
print(student.get("name"))

# to update dict.
student.update({"city":"delhi"})
print(student)
