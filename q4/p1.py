import sys
from board import Board
def load_data():
    fileanme = sys.argv[1]
    with open(fileanme, 'r') as f:
        lines = [x for x in f.readlines() if x!='\n']
        moves = [int(x) for x in lines[0].strip('\n').split(',')]
        del lines[0]
        boards =[]
        for i in range(0,len(lines),5):
            rows = lines[i:i+5]
            board = []
            for row in rows:
                row = [(int(x),False) for x in row.strip('\n').split(' ') if x!='']
                board.append(row)
            boards.append(Board(arrs=board))
    return moves,boards

moves,boards = load_data()
bingo = False
bingo_board = 0
for move in moves:
    for idx,board in enumerate(boards):
        board.select(move)
        if board.check_bingo():
            bingo = True
            bingo_board = idx
            break
    if bingo:
        break
boards[bingo_board].get_score()