num = int(input("Enter number: "))
div = int(input("enter divisor"))

if num % (2 * div) == 0:
    print(f"{2* div} divides {num}")
elif num % div == 0:
    print(f"{div} divides {num}")
else:
    print("doesnt divide")
