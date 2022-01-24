# Interest loop

APR = eval(input("Enter the APR"))
principal = eval(input("Enter the principal account balance"))

for element in range(10):
    principal = principal * (1 + APR)

print(principal)