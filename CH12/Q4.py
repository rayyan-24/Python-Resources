try:
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    print(a/b)
except ZeroDivisionError as e:
    print(f"{a}/{b} gives infinity {e}")