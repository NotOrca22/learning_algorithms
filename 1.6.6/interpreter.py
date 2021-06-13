with open("/Users/hailongwang/git/chris/learning_algorithms/1.6.6/input.txt") as f:
    registers = [0,0,0,0,0,0,0,0,0,0]
    i = f.readline()
    for i in range(int(i)):
        line = ""
        cmmdsUsed = 0
        registerSelected = 0
        while line != "100":
            line = f.readline()
            print(line)
            if line == "100" or line == 100:
                exit(54)
            if line.startswith("2"):
                registers[int(line[1])] = int(line[2])
                print(registers)
                cmmdsUsed += 1
            elif line.startswith("3"):
                registers[int(line[1])] += int(line[2])
                print(registers)
                cmmdsUsed += 1
            elif line.startswith("4"):
                registers[int(line[1])] *= int(line[2])
                print(registers)
                cmmdsUsed += 1
            elif line.startswith("5"):
                registers[int(line[1])] = int(line[2])
                cmmdsUsed += 1
            elif line.startswith("6"):
                registers[int(line[1])] += int(line[2])
                cmmdsUsed += 1
            elif line.startswith("7"):
                registers[int(line[1])] *= int(line[2])
                cmmdsUsed += 1
            elif line.startswith("8"):
                registers[int(line[1])] = int(line[2])
                cmmdsUsed += 1
            elif line.startswith("9"):
                registers[int(line[1])] = int(line[2])
                cmmdsUsed += 1
            else:
                print(line)
                cmmdsUsed += 1
                if len(line) >= 3:
                    if "0" not in str(registers[int(line[2])]):
                        registerSelected = int(line[1])
                else:
                    break
    print(cmmdsUsed)