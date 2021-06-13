def fill(x,y,array, color):
    x, y = int(x), int(y)
    originalColor = array[y-1][x-1]
    cellsToChange = [[y-1, x-1, False]]
    for cell in cellsToChange:
        if not cell[2]:
            y1 = cell[0] - 1
            x1 = cell[1]
            if y1 >= 0:
                if array[y1][x1] == originalColor and [y1, x1, False] not in cellsToChange and [y1,x1, True] not in cellsToChange:
                    cellsToChange.append([y1, x1, False])
            y2 = cell[0] + 1
            x2 = cell[1]
            if y2 <= len(arr) + 1: #check element under the original element
                if array[y2][x2] == originalColor and [y2, x2, False] not in cellsToChange and [y2,x2, True] not in cellsToChange:
                    cellsToChange.append([y2, x2, False])
            y3 = cell[0]
            x3 = cell[1] - 1
            if x3 >= 0: # check element to the left of the original element
                if array[y3][x3] == originalColor and [y3, x3, False] not in cellsToChange and [y3,x3, True] not in cellsToChange:
                    cellsToChange.append([y3, x3, False])
            y4 = cell[0]
            x4 = cell[1] + 1
            if x4 < len(arr[0]): # check element to the right of the original element
                if array[y4][x4] == originalColor and [y4,x4,False] not in cellsToChange and [y4,x4,True] not in cellsToChange:
                    cellsToChange.append([y4,x4,False])
                cell[2] = True # this cell has been fully checked
    for cell in cellsToChange:
        array[cell[0]][cell[1]] = color
    return array
with open("/Users/hailongwang/git/chris/learning_algorithms/1.6.5/input.txt") as f:
    l = ""
    arr = []
    while l != "X":
        l = f.readline()
        print(l)
        if l.startswith("I"):
            m = l.split(" ")
            for i in range(int(m[2])):
                s = []
                for i in range(int(m[1])):
                    s.append("O")
                arr.append(s)

            print(arr)
        elif l.startswith("L"):
            m = l.split(" ")
            arr[int(m[2]) - 1][int(m[1]) - 1] = m[3][:-1]
            print(arr)
        elif l.startswith("V"):
            m = l.split(" ")
            for i in range(int(m[2]),int(m[3]) + 1):
                print(i)
                arr[i][int(m[1]) - 1] = m[4][:-1]
            print(arr)
        elif l.startswith("H"):
            m = l.split(" ")
            for i in range(int(m[2]), int(m[3]) + 1):
                print(i)
                arr[int(m[1]) - 1][i] = m[4][:-1]
            print(arr)
        elif l.startswith("C"):
            arr2 = []
            for i in range(len(arr)):
                s = []
                for i in range(len(arr[i])):
                    s.append("O")
                arr2.append(s)
            arr = arr2
            print(arr)
        elif l.startswith("K"):
            m = l.split(" ")
            print(m)
            for i in range(int(m[2]), int(m[4]) + 1):
                for j in range(int(m[1]), int(m[3]) + 1):
                    print(i,j)
                    arr[i-1][j-1] = m[5][:-1]
            print(arr)
        elif l.startswith("F"):
                # toChange = []
            m = l.split(" ")
                # color = arr[int(m[2]) - 1][int(m[1]) - 1]
                # toChange.append([int(m[2]) - 1,int(m[1]) - 1, 0])
                # print(color == arr[int(m[2])-2][int(m[1]) - 1])
                # if int(m[2]) > 1:
                #     if arr[int(m[2]) - 2][int(m[1]) - 1] == color:
                #         toChange.append([int(m[2])-2,int(m[1]) - 1, 0])
                # if int(m[2]) < len(arr) + 1:
                #     if arr[int(m[2])][int(m[1]) - 1] == color:
                #         toChange.append([int(m[2]),int(m[1]) - 1,0])
                # if int(m[1]) < len(arr[0]) + 1:
                #     toChange.append([int(m[2]) - 1, int(m[1]), 0])
                # if int(m[1]) - 1 > 0:
                #     toChange.append([int(m[2]) - 1,int(m[1]) - 2, 0])
                # for element in toChange[1:]:
                #     if element[0] > 0 and arr[element[1]][element[0] - 1] == color and element[2] == 0:
                #         print(element)
                #         print(arr[element[1]][element[0] - 1])
                #         print(element == [1,3,0] or element == [1,3,1])
                #         print(element)
                #         print(arr[3][0])
                #         toChange.append([element[1],element[0]-1, 0])
                #     if element[0] < len(arr[0]) + 1 and arr[element[1]][element[0] + 1] == color and element[2] == 0:
                #         toChange.append([element[1],element[0]+ 1, 0])
                #     if element[1] < len(arr) + 1 and arr[element[1] + 1][element[0]] == color and element[2] == 0:
                #         toChange.append([element[1] + 1, element[0], 0])
                #     if element[1] > 0 and arr[element[1] - 1][element[0]] == color and element[2] == 0:
                #         print(element)
                #         toChange.append([element[1] - 1, element[0], 0])
                #         element[2] = 1
                # print(toChange)
                # for i in toChange:
                #     print(i)
                #     arr[i[1]][i[0]] = m[3][:-1]
            arr = fill(m[1], m[2], arr, m[3][:-1])
            print(arr)
        for row in arr:
            print("".join(row))
