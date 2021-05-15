line1 = ["-"]
def getLayers(size):
    print(type(size))
    size = int(size)
    return [["-", "", "-","-","","-","-","-","-","-"],
            ["|" + size * " " + "|", "|", (" " * size + "|"), (size * " " + "|"),"|" + size * " " + "|",("|"), ("|"), (size * " " + "|"), ("|" + size * " " + "|"),("|" + size * " " + "|" )],
            ["", "", "-","-","-","-","-","","-","-"],
            ["|" + size * " " + "|","|", "|", (size * " "  + "|")," " + "|","|", "|" + size * " " + "|",size * " " + "|", "|" + size * " " + "|",size * " " + "|"],
            ["-", "", "-","-","","-","-","","-","-"]]

def getFirstLayer(number, size):
    size = int(size)
    output = ""
    for digit in str(number):
        digit = int(digit)
        if digit == 0 or digit == 2 or digit == 3 or digit == 5 or digit == 6 or digit == 7 or digit == 8 or digit == 9:
            output += ' ' + "-" * size + " "
        elif digit == 1:
            output += " "
        else:
            output += " " * (size + 2)
        output += " "
    print(output)

def getSecondLayer(number, size):
    for i in range(size):
        output = ""
        for digit in str(number):
            digit = int(digit)
            if digit == 0 or digit == 4 or digit == 8 or digit == 9:
                output += "|" + " " * size + "|"
            elif digit == 5 or digit == 6:
                output += "|" + " " * (size + 1)
            elif digit == 1:
                output += "|"
            else:
                output += " " * (size + 1) + "|"
            output += " "
        print(output)

def getThirdLayer(number, size):
    output = ""
    for digit in str(number):
        digit = int(digit)
        if digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6 or digit == 8 or digit == 9:
            output += " " + "-" * size + " "
        elif digit == 1:
            output += " "
        elif digit == 7 or digit == 0:
            output += " " * (size + 2)
        else:
            output += " " * size
        output += " "
    print(output)

def getFourthLayer(number, size):
    for i in range(size):
        output = ""
        for digit in str(number):
            digit = int(digit)
            if digit == 0 or digit == 6 or digit == 8:
                output += "|" + " " * size + "|"
            elif digit == 1:
                output += "|"
            elif digit == 2:
                output += "|" + " " * (size + 1)
            else:
                output += " " * (size + 1) + "|"
            output += " "
        print(output)

def getFifthLayer(number, size):
    output = ""
    for digit in str(number):
        digit = int(digit)
        if digit == 0 or digit == 2 or digit == 3 or digit == 5 or digit == 6 or digit == 8 or digit == 9:
            output += " " + "-" * size + " "
        elif digit == 1:
            output += " "
        elif digit == 7 or digit == 4:
            output += " " * (size + 2)
        else:
            output += " " * size
        output += " "
    print(output)
def printZero(size):
    print("-" * size)
    for i in range(size):
        print("|" + " " * size + "|")
    print("-" * size)
def printOne(size):
    # print("\n")
    # print("|\n" * size)
    # print("|\n" * size)
    return "|\n" * size * 2
def printTwo(size):
    s = ""
    print("-"* size)
    # print((" " * size + "|") * (size-1))
    for i in range(size):
        print(" " * size + "|")
    print("-" * size)
    for i in range(size):
        print("|")
    print("-" * size)
    return "-" * size
def printThree(size):
    print("-"* size)
    # print((" " * size + "|") * (size-1))
    for i in range(size):
        print(" " * size + "|")
    print("-" * size)
    for i in range(size):
        print(" " * size + "|")
    print("-" * size)
def printFour(size):
    for i in range(size):
        print("|" + " " * size + "|")
    print(size * "-")
    for i in range(size):
        print(" " * size + "|", end="")
def printFive(size):
    print("-"* size)
    # print((" " * size + "|") * (size-1))
    for i in range(size):
        print("|")
    print("-" * size)
    for i in range(size):
        print(" " * size + "|")
    print("-" * size)
def printSix(size):
    print("-"* size)
    # print((" " * size + "|") * (size-1))
    for i in range(size):
        print("|")
    print("-" * size)
    for i in range(size):
        print("|" + " " * size + "|")
    print("-" * size)
def printSeven(size):
    print("-"*size)
    for i in range(size*2):
        print(" " * size + "|")
def printEight(size):
    print("-"*size)
    for i in range(size):
        print("|" + " " * size + "|")
    print("-"*size)
    for i in range(size):
        print("|" + " " * size + "|")
    print("-"*size)
def printNine(size):
    print("-"*size)
    for i in range(size):
        print("|" + " " * size + "|")
    print("-"*size)
    for i in range(size):
        print(" " * size + "|")
    print("-"*size)
def oneTwoThree(size):
    x = getLayers(size)
    print(size * (x[0][1]) + "\t" + size * (x[0][2]) + "\t\t" + size * (x[0][3]) + "\t" + size * (x[0][4]) + "\t\t\t" + size * (x[0][5]) + "\t\t" + size * x[0][6] + "\t\t" + size * x[0][7] + "\t\t" + size * x[0][8] + "\t\t" + size * x[0][9] +  "\t\t" + size * x[0][0] + "\n" +
          size * (x[1][1] + "\t" + x[1][2] + "\t" + x[1][3] + "\t" + x[1][4] + "\t" + x[1][5] + "\t\t" + x[1][6] + "\t\t" + x[1][7] + "\t" + x[1][8] + "\t" + x[1][9] + "\t" + x[1][0] + "\n") +
          size * (x[2][1]) + "\t" + size * (x[2][2]) + "\t\t" + size * (x[2][3]) + "\t\t " + size * x[2][4] + "\t" + size * x[2][5] + "\t\t" + size * x[2][6] + "\t\t" + size * x[2][7] + "\t\t" + size * x[2][8] + "\t\t" + size * x[0][9] +  "\t\t" + size * x[2][0] + "\n"+
          size*(x[3][1] + "\t" + x[3][2] + "\t\t" + x[3][3] + "\t" + size * " " + x[3][4] + "\t\t" + x[3][5] + "\t" + x[3][6] + "\t" + x[3][7] + "\t" + x[3][8] + "\t" + x[3][9] + "\t" + x[3][0] + "\n") +
          size * (x[4][1]) + "\t" + size * (x[4][2]) + "\t\t" + size * x[4][3] + "\t\t" + size * x[4][4] + "\t\t" + size * x[4][5] + "\t\t" + size * x[4][6] + "\t\t" + size * x[4][7] + "\t\t" + size * x[4][8] + "\t\t" + size * x[4][9] + "\t\t" + size * x[4][0] +"\n")
x = getLayers(2)
# print(x[0][6] + "\n" + x[1][6] + x[2][6]+ "\n" +x[3][6] + x[4][6])
with open("/Users/hailongwang/git/chris/learning_algorithms/1.6.4/input.txt") as f:
    l = ""
    while l != "0 0":
        l = f.readline()
        s,n = l.split(" ")
        if l == "0 0":
            exit(0)
        n = n[:-1]
        s, n = int(s), int(n)
        # printTwo(3)
        # oneTwoThree(3)
        getFirstLayer(n, s)
        getSecondLayer(n, s)
        getThirdLayer(n, s)
        getFourthLayer(n, s)
        getFifthLayer(n, s)