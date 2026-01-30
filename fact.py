def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("ENter the your number = "));
print("Factorial of", num, "is:", factorial(num))
