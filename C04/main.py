print("Super duper calculator 3.0 ... fibonacci sequence to calculate")
print("Im really bad at maths and i cant even do this")
print("I just learned what this was from wikipedia")
print("Welp")
print("")
print("")

n = int(input("Enter the term of the Fibonacci sequence to calculate: "))

prev = 0
curr = 1

#some sessy math

if n == 1:
  print("Nth term:", prev)
  print("Sum of terms:", prev)
else:
  for _ in range(n - 1):
    next_term = prev + curr
    prev, curr = curr, next_term

  print("Nth term:", curr)

  sum_of_terms = curr
  for _ in range(n - 2):
    next_term = prev + curr
    prev, curr = curr, next_term
    sum_of_terms += curr

  print("Sum of terms:", sum_of_terms)
