import shape


print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter choice: ")

if choice == "1":
    r = float(input("Radius: "))
    print("Area =", shape.circle_area(r))

elif choice == "2":
    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Area =", shape.rectangle_area(l, w))

elif choice == "3":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area =", shape.triangle_area(b, h))

else:
    print("Wrong choice")