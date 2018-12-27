import ezchess
from ezchess import chess_tree

init_board = [13, 11, 12, 14, 15, 12, 11, 13, 10, 10, 10, 10, 10, 10, 10, 10]
for i in range(16,48,1):
    init_board = init_board + [0]
init_board = init_board + [20, 20, 20, 20, 20, 20, 20, 20, 23, 21, 22, 24, 25, 22, 21, 23]

ezchess.printBoard(init_board)

board = init_board[:]
#print ezchess.GetPieceLegalMoves(board,8)
#print ezchess.GetPieceLegalMoves(board,9)
#print ezchess.GetPieceLegalMoves(board,15)
#print ezchess.GetPieceLegalMoves(board,16)
#print ezchess.GetPieceLegalMoves(board,5)
print ezchess.move(board,11,19)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,2)
print ezchess.move(board,9,17)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,2)
#print ezchess.GetPieceLegalMoves(board,1)
print ezchess.move(board,17,41)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,41)
print ezchess.move(board,0,17)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,17)
#print ezchess.GetPieceLegalMoves(board,48)
#print ezchess.GetPieceLegalMoves(board,4)
print ezchess.move(board,3,20)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,4)
#print ezchess.GetPieceLegalMoves(board,20)
print ezchess.move(board,58,46)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,46)
print "CanCheck?"
print ezchess.CanCheck(board,61,25)
print ezchess.move(board,61,25)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,4)
#print ezchess.GetPieceLegalMoves(board,17)
print ezchess.IsPositionUnderThreat(board,25,20)
print ezchess.IsPositionUnderThreat(board,4,10)
print ezchess.position_value(board,15)
print ezchess.board_value(init_board)
print ezchess.board_value(board)
print ezchess.gen_king_zone(board,10)
ezchess.printBoard(board)
print ezchess.zone_attack_value(board, 20)
print ezchess.move(board,57,28)
ezchess.printBoard(board)
#print ezchess.GetPieceLegalMoves(board,28)
print ezchess.zone_attack_value(board, 20)
print ezchess.board_value(board)
print ezchess.GetPieceLegalMoves(board, 20)
print ezchess.GetPieceLegalMoves_pseudo(board, 20)


# print "Testing Trees."
# test_tree = ezchess.chess_tree(init_board, [])
# print test_tree.get_level_order_traversal()
# print test_tree.val
# board_2 = init_board[:]
# ezchess.gen_possible_moves(test_tree, 10)
# print test_tree.get_level_order_traversal()
# ezchess.gen_opponent_response(test_tree.subtrees[0], 10)
# print "testing opponent response."
# print test_tree.get_level_order_traversal()

# testing final :)
board_2 = init_board[:]
ezchess.printBoard(board_2)
# r = ezchess.chessPlayer(board_2, 10)
# print r
# print r[3].get_level_order_traversal()
print ezchess.position_value(board_2, 55)
print ezchess.position_value(board_2, 15)
print ezchess.board_value(board_2)

