list = []
n = int(input("Enter number of elements should in a list: "))
for x in range(0,n):
    elements = int(input("enter the value of element." + str(x+1) + ":"))
    list.append(elements)
print(list)
pos_count, neg_count = 0 ,0
num = 0
while(num< len(list)):
    if list[num] >= 0:
        pos_count += 1
    else:
        neg_count +=1
    num += 1
print("Poistive number of values are: ",pos_count)
print("Negative number of values are: ",neg_count)