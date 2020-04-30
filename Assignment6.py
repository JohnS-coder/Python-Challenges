num = int(input("Enter a number: "))
b = []
if num == 0 or num == 1:
  print(f"{num} is not prime")
else:
  for i in range(2,num):
    a = []
    for x in range(2,num):
      if i % x == 0 and x < i:
        a.append(x)
    if len(a) == 0:
      b.append(i)
  print(f"{b} prime numbers 1 to {num}")