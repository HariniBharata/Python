def fib(x):
    if x<=1 and x>=0:
        return x;
    else:
        return(fib(x-1)+fib(x-2));
n=int(input("enter range"))
if n<0:
    print("enter a positive number");
for i in range(n):
    print(fib(i))

    
    
