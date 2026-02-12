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

def check_pawn():
    return ...

def check_rook():
    return ...

def check_bishop():
    return ...

def check_queen():
    return ...

def checkmate(board_str):
    if not validBoard(board_str):
        print("Fail")
        return

    lines = board_str.strip("\n").split("\n")
    board = normalizeBoard(lines)

    print(board)