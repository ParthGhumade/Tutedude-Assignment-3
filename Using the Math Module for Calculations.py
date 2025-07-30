import math 
n=int(input('Enter The Number-->'))

if n<0:
    print("Square Root : Not Defined")
    print("Logarithm   : Not Defined")
elif n==0:
    print("Square Root :",math.sqrt(n))
    print("Logarithm   : Not Defined")
else:
    
    print("Square Root :",math.sqrt(n))
    
    print("Logarithm   :",math.log(n))


print ("Sine        :",math.sin(n))

