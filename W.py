
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()


file=open("data.txt","w")
file.write("Welcome to File Handling in Python")
file.close()


file=open("data.txt","a")
file.write("\nThis line is appended to the file")
file.close()








