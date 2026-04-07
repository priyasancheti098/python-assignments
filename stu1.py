# open file in write mode
file = open("output.txt", "w")

# number of lines user wants to enter
n = int(input("Enter number of lines: "))

print("Enter the lines:")

for i in range(n):
    line = input()
    file.write(line + "\n")   # write each line with newline

file.close()

print("Data successfully written to file.")