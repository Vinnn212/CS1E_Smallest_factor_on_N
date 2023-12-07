def smallest_factor(n):
  if n <= 1:
    return None
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return i
  return None

n = int(input("Enter a number: "))
smallest_factor = smallest_factor(n)

if smallest_factor is None:
  print(n, "is prime")

else:
  print(f"The smallest factor for", n, "is", smallest_factor)
