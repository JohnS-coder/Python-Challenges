b = 0
c = [1,1]
for a in range(1,55):
  if b < 55 :
    b = c[a] + c[a-1]
    c.append(b)
print(f"fibonacci--> {c}")