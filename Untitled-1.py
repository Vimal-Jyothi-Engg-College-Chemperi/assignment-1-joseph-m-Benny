
n = int(input("Enter an integer: "))

sign = -1 if n < 0 else 1
n = abs(n)

rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

rev *= sign
print("Reversed integer:", rev)
