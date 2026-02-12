# PRINT LENTH OF A LIST.

cities = ["mathura","agra","delhi","mumbai","aligarh"]
heroes = ["hritik","tiger","ayushman","salman","jacky","shahrukh"]

def lenth(list) :
    list = len(list)
    return list

print(lenth(cities))
print(lenth(heroes))




# TO PRINT THE ELEMENTS OF LIST IN A SINGLE LINE.

def print_list(list) :
    for item in list :
        print(item, end=" ")


print_list(heroes)
print_list(cities)