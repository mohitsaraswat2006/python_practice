# with open("practice.txt","r") as f:
#     # f.write("hi everyone\nwe are learning File I\O\n")
#     # f.write("using java.\nI like programming in  java.")
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)  # gives python at the place of java only in terminal.

# with open("practice.txt","w") as f :
#     f.write(new_data)  # it saves the chnages or python at the place of java in file.


# to check the word "learning" exists in the text file or not.
word = "learning"
with open("practice.txt","r") as f:
    data =f.read()
    if(data.find(word) != -1):
        print("found")
    else :
        print("not found")