def checkallligneandcolones(board ,size):
    """_summary_
    return False if no ligne win else player
    Returns:
        Player: pion / name
        or 
        Boolean: False
    """
    for y in range(size):
        a = []
        b = []
        for x in range(size):
            if board[y][x] != None:
                if len(a) > 0:
                    if a[0] == board[y][x]:
                           a.append(board[y][x])
                else:
                    a.append(board[y][x])
                        
            if board[x][y] != None:
                if len(a) > 0:
                    if a[0] == board[y][x]:
                        b.append(board[x][y])
                else:
                    b.append(board[x][y])
                        
        if len(a) == size:
            return a[0]
        if len(b) == size:
            return b[0]
    return False
size = 10

board = [[None for i in range(size)]for i in range(size)]
print(checkallligneandcolones(board, size))
