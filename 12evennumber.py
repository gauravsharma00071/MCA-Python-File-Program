start = int(input("Enter the value from where we want to start our list: "))
end = int(input("Enter last value where we want to stop:  "))

for x in range(start, end+1):
    if x % 2 == 0:
        print(x, end= " ")
