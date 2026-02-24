info = [
    ("Alice","Maths"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Maths"),
    ("Bob","Maths"),
    ("Alice","English"),
    ("Charlie","English"),
]
unique_courses = set()
for tup in info :
    # print(tup) #prints wholw tuple.
    # print(tup[0]) # prints only the names which are on 0th index.
    # print(tup[1]) # prints only the subjects which are stored on 1ts index.
    unique_courses.add(tup[1])
print(unique_courses)

#print those student who enrolled in emglish course.
for name , course in info :
    # print(name,course) 
    if(course == "English") :
        print(name)