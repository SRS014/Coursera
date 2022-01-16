largest = None
smallest = None
My_List = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num != int(num)

        except ValueError:
            print("Invalid input")
        else:
            num1 = int(num)
            My_List.append(num1)
            largest = max(My_List)
            smallest = min(My_List)
            
print("Maximum is", largest)
print("Minimum is", smallest)