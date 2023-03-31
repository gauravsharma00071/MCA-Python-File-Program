list = []
n = int(input("Enter number of elements should in a list: "))
for x in range(0,n):
    elements = int(input("enter the value of element." + str(x+1) + ":"))
    list.append(elements)
print(list)

n1 = int(input("enter the element to insert: "))
list.insert(0,n1)

print(list)

re = int(input("enter the element from list which you want to delete.: "))
list.pop(re)
print(list)