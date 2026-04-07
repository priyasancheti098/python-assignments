filename = input("Enter the filename to open:")

try:

    file = open(filename, 'r')
    content = file.read()
    print("\nFile Opened Successfully.File content:\n")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")    

except PermissionError:
    print("Error: You do not have permission to access this file. Please check the file permissions and try again.")