
x=int(input('Enter The Number-->'))

def factorial(n):
    if n<0:
        return 'undefined' 

    elif n< 2:
        return 1
    else :
    
        return n*factorial(n-1)
    
result=factorial(x)
print("Factorial of", x,"is:",result)
