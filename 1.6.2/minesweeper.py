n, m = input().split(" ")
field = []
for i in range(int(n)):
    l = []
    for x in input():
        if x == "*":
            l.append("*")
        else:
            l.append("0")
    field.append(l)
for row in field:
    print(''.join(row))
rowIndex = 0
for row in field:
    colIndex = 0
    for element in row:
        try:
            element = int(element)
        except:
            pass
    for element in row:
        if element == "*":
            if 0 <= rowIndex-1:
                # print(field, rowIndex, colIndex)
                # print(field[rowIndex-1][colIndex])
                field[rowIndex-1][colIndex] = int(field[rowIndex-1][colIndex]) + 1
            if 0 <= rowIndex + 1 < len(field):
                field[rowIndex+1][colIndex] = int(field[rowIndex+1][colIndex]) + 1
            try:
                if 0 <= colIndex - 1:
                    field[rowIndex][colIndex-1] = int(field[rowIndex][colIndex-1]) + 1
                else:
                    pass
            except:
                pass
            try:
                if 0 <= colIndex + 1 < len(row):
                    field[rowIndex][colIndex+1] += 1
                else:
                    pass
            except:
                pass
        colIndex += 1
    rowIndex += 1
    i = 0

print(field)

def MineSweeper2(m,n,field):
    for i in range(m):
        for j in range(n):
            if field[i][j] == "*":
                if i - 1 < 0:
                    pass
                else:
                    field[i-1][j] += 1
                if i + 1 < m:
                    field[i+1][j] += 1
                if j - 1 >= 0:
                    field[i][j-1] += 1
                if j + 1 < n:
                    field[i][j+1] += 1
    return field

print(MineSweeper2(3,2,[[0, 0], [0, "*"], ["*", 0]]))