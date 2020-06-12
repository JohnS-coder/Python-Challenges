sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
count = 0
for i in sudoku:
    if count == 0 or count%3 == 0:
        print(" - - - - - - - - - - - - - - - ")
    a = ""
    while len(i) != 0:
        for j in i[:3]:
            a = a+str(j)
        i = i[3:]
    print(" "+"  ".join(a[:3])," |","  ".join(a[3:6]), " |","  ".join(a[6:]))
    count += 1
print(" - - - - - - - - - - - - - - - ")