### CODIO SOLUTION BEGIN
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)
print(factorial(3))
### CODIO SOLUTION END