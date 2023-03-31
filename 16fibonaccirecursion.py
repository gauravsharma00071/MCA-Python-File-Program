def fib(n):
    if n <=1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
nterms = int(input("enter numbers of terms: "))
if nterms <= 0:
    print("enter a positive integer")
else:
    print("Fibonacci series using recursion is: ")
    for i in range(nterms):
            print(fib(i))