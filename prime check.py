def check_prime(n):
    if n <= 1:
        return f"{n} is not prime."
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not prime."
    return f"{n} is prime."

num = int(input("Enter a number: "))
print(check_prime(num))
