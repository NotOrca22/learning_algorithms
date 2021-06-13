board = []
with open("/Users/hailongwang/git/chris/learning_algorithms/1.6.7/input.txt") as f:
    for i in range(8):
        line = f.readline()
        board.append(list(line)[:8])
    whiteInCheck = False
    blackInCheck = False
    rank = 0
    file = 0
    for row in board:
        file = 0
        for piece in row:
            if piece != ".":
                if piece == "P":
                    if file > 0:
                        if board[rank-1][file-1] == "k":
                            blackInCheck = True
                            break
                    if file < 7:
                        if board[rank-1][file+1] == "k":
                            blackInCheck = True
                            break
                elif piece == "p":
                    if file > 0:
                        if board[rank+1][file-1] == "K":
                            whiteInCheck = True
                            break
                    if file < 7:
                        if board[rank+1][file+1] == "K":
                            whiteInCheck = True
                            break
                elif piece == "B":
                    directions = [(-1,-1), (1,1), (-1,1), (1,-1)]
                    for direction in directions:
                        if direction == (-1,-1):
                            f = file
                            r = rank
                            while f > 0 and r > 0:
                                f -= 1
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1,1):
                            f = file
                            r = rank
                            while f < 7 and r < 7:
                                f += 1
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1,1):
                            f = file
                            r = rank
                            while f > 0 and r < 7:
                                f -= 1
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        else:
                            f = file
                            r = rank
                            while f < 7 and r > 0:
                                f += 1
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                elif piece == "b":
                    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
                    for direction in directions:
                        if direction == (-1, -1):
                            f = file
                            r = rank
                            while f > 0 and r > 0:
                                f -= 1
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 1):
                            f = file
                            r = rank
                            while f < 7 and r < 7:
                                f += 1
                                r += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 1):
                            f = file
                            r = rank
                            while f > 0 and r < 7:
                                f -= 1
                                r += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        else:
                            f = file
                            r = rank
                            while f < 7 and r > 0:
                                f += 1
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                elif piece == "R":
                    directions = [(1,0), (-1,0), (0,1), (0,-1)]
                    for direction in directions:
                        if direction == (1,0):
                            r = rank
                            f = file
                            while r < 7:
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 0):
                            r = rank
                            f = file
                            while r > 0:
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (0, 1):
                            r = rank
                            f = file
                            while f < 7:
                                f += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 0):
                            r = rank
                            f = file
                            while f > 0:
                                f -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                elif piece == "r":
                    directions = [(1,0), (-1,0), (0,1), (0,-1)]
                    for direction in directions:
                        if direction == (1,0):
                            r = rank
                            f = file
                            while r < 7:
                                r += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 0):
                            r = rank
                            f = file
                            while r > 0:
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (0, 1):
                            r = rank
                            f = file
                            while f < 7:
                                f += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (0, -1):
                            r = rank
                            f = file
                            while f > 0:
                                f -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                elif piece == "Q":
                    directions = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1)]
                    for direction in directions:
                        if direction == (1,0):
                            r = rank
                            f = file
                            while r < 7:
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 0):
                            r = rank
                            f = file
                            while r > 0:
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (0, 1):
                            r = rank
                            f = file
                            while f < 7:
                                f += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 0):
                            r = rank
                            f = file
                            while f > 0:
                                f -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        if direction == (-1, -1):
                            f = file
                            r = rank
                            while f > 0 and r > 0:
                                f -= 1
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 1):
                            f = file
                            r = rank
                            while f < 7 and r < 7:
                                f += 1
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 1):
                            f = file
                            r = rank
                            while f > 0 and r < 7:
                                f -= 1
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        else:
                            f = file
                            r = rank
                            while f < 7 and r > 0:
                                f += 1
                                r -= 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                elif piece == "q":
                    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
                    for direction in directions:
                        if direction == (1, 0):
                            r = rank
                            f = file
                            while r < 7:
                                r += 1
                                if board[r][f] == "k":
                                    blackInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 0):
                            r = rank
                            f = file
                            while r > 0:
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (0, 1):
                            r = rank
                            f = file
                            while f < 7:
                                f += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 0):
                            r = rank
                            f = file
                            while f > 0:
                                f -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        if direction == (-1, -1):
                            f = file
                            r = rank
                            while f > 0 and r > 0:
                                f -= 1
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (1, 1):
                            f = file
                            r = rank
                            while f < 7 and r < 7:
                                f += 1
                                r += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        elif direction == (-1, 1):
                            f = file
                            r = rank
                            while f > 0 and r < 7:
                                f -= 1
                                r += 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break
                        else:
                            f = file
                            r = rank
                            while f < 7 and r > 0:
                                f += 1
                                r -= 1
                                if board[r][f] == "K":
                                    whiteInCheck = True
                                    break
                                elif board[r][f] != ".":
                                    break

            file += 1
        rank += 1

    if whiteInCheck:
        print("white king is in check.")
    elif blackInCheck:
        print("black king is in check.")
    else:
        print("no king is in check.")