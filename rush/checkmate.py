def validBoard(board: str) -> bool:
    if not board or not isinstance(board, str):
        return False

    board = board.strip("\n")
    lines = board.split("\n")

    if len(lines) == 0:
        return False

    size = len(lines[0])

    if len(lines) != size:
        return False

    for line in lines:
        if len(line) != size:
            return False

    king_count = sum(line.count("K") for line in lines)
    if king_count != 1:
        return False

    return True

def normalizeBoard(board):
    alp = "KPRBQ"
    return [[ch if ch in alp else "." for ch in row] for row in board]

def check_pawn(board, row, col, king_row, king_col):
    if row - 1 == king_row and col - 1 == king_col:
        return True
    if row - 1 == king_row and col + 1 == king_col:
        return True

    return False

def check_rook(board, row, col, king_row, king_col):
    if col == king_col:
        step = 1 if king_row > row else -1
        r = row + step
        while r != king_row:
            if board[r][col] != ".":
                return False
            r += step
        return True

    if row == king_row:
        step = 1 if king_col > col else -1
        c = col + step
        while c != king_col:
            if board[row][c] != ".":
                return False
            c += step
        return True
    
    return False

def check_bishop(board, row, col, king_row, king_col):
    if abs(row - king_row) == abs(col - king_col):
        row_step = 1 if king_row > row else -1
        col_step = 1 if king_col > col else -1

        r = row + row_step
        c = col + col_step

        while r != king_row and c != king_col:
            if board[r][c] != ".":
                return False
            r += row_step
            c += col_step

        return True

    return False

def check_queen(board, row, col, king_row, king_col):
    if check_rook(board, row, col, king_row, king_col) or \
       check_bishop(board, row, col, king_row, king_col):
        return True

    return False

def checkmate(board_str):
    if not validBoard(board_str):
        print("Fail")
        return

    lines = board_str.strip("\n").split("\n")
    board = normalizeBoard(lines)

    size = len(board)

    king_row = -1
    king_col = -1

    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                king_row = r
                king_col = c

    for r in range(size):
        for c in range(size):
            piece = board[r][c]

            if piece == "P":
                if check_pawn(board, r, c, king_row, king_col):
                    print("Success")
                    return

            if piece == "R":
                if check_rook(board, r, c, king_row, king_col):
                    print("Success")
                    return
                
            if piece == "B":
                if check_bishop(board, r, c, king_row, king_col):
                    print("Success")
                    return

            if piece == "Q":
                if check_queen(board, r, c, king_row, king_col):
                    print("Success")
                    return

    print("Fail")