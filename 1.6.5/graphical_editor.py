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
            m = l.split(" ")
            color = arr[int(m[2]) - 1][int(m[1]) - 1]
            print(color)
            if int(m[2]) > 1:
                if arr[int(m[2]) - 2][int(m[1]) - 1] == color:
                    arr[int(m[2])-2][int(m[1]) - 1] = m[3][:-1]
            print(arr)