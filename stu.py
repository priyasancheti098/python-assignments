import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Roll No", "Branch", "Marks"])
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        print(f"\nEnter details of student {i+1}:")
        name = input("Name: ")
        roll = input("Roll No: ")
        branch = input("Branch: ")
        marks = input("Marks: ")
        
        # writing data into CSV
        writer.writerow([name, roll, branch, marks])

print("\nData successfully written to students.csv")