list = []
n = int(input("Enter number of elements should in a list: "))
for x in range(0,n):
    elements = int(input("enter the value of element." + str(x+1) + ":"))
    list.append(elements)
print(list)

list.reverse()
print("Reverse of the list is:",list)
