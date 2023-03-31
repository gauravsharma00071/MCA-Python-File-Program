a = []
n = int(input("Enter number of elements in list: "))
for x in range(0,n):
    elements = int(input("enter elements: " + str(x+1) + ":"))
    a.append(elements)

temp = a[0]
a[0] = a[n-1]
a[n-1] = a[0]
print("New list is: " ,a)