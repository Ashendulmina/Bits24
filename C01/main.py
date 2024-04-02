import math

print("Super Duper LCM Calculator 2.0 ... with no error handling")
n = int(input("Enter the number of positive numbers: "))
numbers = list(
    map(int,
        input("Enter the numbers separated by spaces: ").split()))

lcm = numbers[0]

for i in range(1, n):
  current_number = numbers[i]
  gcd = math.gcd(lcm, current_number)
  lcm = lcm * current_number // gcd

print("LCM:", lcm)
