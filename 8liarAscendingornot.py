test_list = []
test_list = [int for item in input("Enter the list.").split()]
print(test_list)

flag = 0
i =1
while i < len(test_list):
    if (test_list[i] < test_list[i-1]):
        flag = 1
    i += 1

if(not flag):
    print("yes it is ascending order.")
else:
    print("not sorted")