while True:
    import math
    x1=0
    x2=0
    x1,2=0
    print ("ax*ax+bx+c=0")
    print ("D=b*b-4ac")
    a=float(input("Enter number a:"))
    b=float(input("Enter number b:"))
    c=float(input("Enter number c:"))
    if (b**2 - 4*a*c > 0):
        print ("It has 2 roots")
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        print("x1="+str(x1))
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
        print("x2="+str(x2))
    elif (b**2 - 4*a*c == 0):
        print ("It has 1 roots")
        x1,2 = -b / (2*a)
        print("x1,2="+str(x1,2))
    else:
        print ("no skill")


