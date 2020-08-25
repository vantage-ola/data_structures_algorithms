def factorial(n):
    
    if n==0:
        return 1
    f= n*factorial(n-1)
    print(f)
    return (f)
    
factorial(4)