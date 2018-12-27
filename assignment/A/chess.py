import ezchess
from random import randint
import time

init_board = [13, 11, 12, 15, 14, 12, 11, 13, 10, 10, 10, 10, 10, 10, 10, 10]
for i in range(16,48,1):
    init_board = init_board + [0]
init_board = init_board + [20, 20, 20, 20, 20, 20, 20, 20, 23, 21, 22, 25, 24, 22, 21, 23]
board = init_board

while True:
    ezchess.printBoard(board)
    # pieces = ezchess.GetPlayerPositions(board, 10)
    # moves = []
    # for i in pieces:
    #     l = ezchess.GetPieceLegalMoves(board, i)
    #     if isinstance(l, list):
    #         for j in l:
    #             moves += [[i, j]]
    # mov = moves[randint(0, len(moves)-1)]
    # ezchess.move(board, mov[0], mov[1])
    # if board[position] // 10 == 1:
    position = input('White: choose a piece:')
    target = input('White: where do you want to move it?')
    if target in ezchess.GetPieceLegalMoves(board, position):
        ezchess.move(board, position, target)
    else:
        print ('Illegal Move. Please try again.')
    # else:
    #     print ('That is not yours. Please try again')
    ezchess.printBoard(board)
    start = time.time()
    generated_move = ezchess.chessPlayer(board, 20)
    print generated_move
    end = time.time()
    print "total time"
    print end - start
    if generated_move[0]:
        position = generated_move[1][0]
        target = generated_move[1][1]
    ezchess.move(board, position, target)


