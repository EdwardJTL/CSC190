#An empty board position has a value of 0. A
# board position that is occupied will have a value
# given by: Offset+Value
#
# White: Offset=10
# Black: Offset=20
#
# Piece: Value
# Pawn:   +0
# Knight: +1
# Bishop: +2
# Rook:   +3
# Queen:  +4
# King:   +5

# The white player pieces will occupy rows 0 and 1
#    initially (i.e., elements 0 through 15), while the black player
#    pieces will occupy rows 7 and 6 initially (i.e., elements 48 to 63).
import time


def GetPlayerPositions(board, player):
    if not isinstance(board, list):
        return -1
    if (len(board) != 64) or (player not in [10, 20]):
        return -1
    else:
        r_list = []
        for i in range(0, len(board), 1):
            if ((board[i] - player) >= 0) and ((board[i] - player) <= 5):
                r_list = r_list+[i]
    return r_list


def printBoard(board):
    if not isinstance(board, list):
        return False
    else:
        printb = []
        char = ''
        [row1, row2, row3, row4, row5, row6, row7, row8] = ['', '', '', '', '', '', '', '']
        for i in range(0, 64, 1):
            piece = board[i]
            if piece == 0:
                [x, y] = [i % 8, i // 8]
                sum = x % 2 + y % 2
                if sum % 2 == 1:
                    char = '#'
                else:
                    char = '_'
            else:
                if (piece % 10) == 0:
                    char = 'P'
                elif (piece % 10) == 1:
                    char = 'K'
                elif (piece % 10) == 2:
                    char = 'B'
                elif (piece % 10) == 3:
                    char = 'R'
                elif (piece % 10) == 4:
                    char = 'Q'
                elif (piece % 10) == 5:
                    char = 'G'
            if piece // 10 == 2:
                char = '\x1b[6;30;42m' + char + '\x1b[0m'
            printb = printb + [char]
            if i < 8:
                row1 += printb[i]
            elif i < 16:
                row2 += printb[i]
            elif i < 24:
                row3 += printb[i]
            elif i < 32:
                row4 += printb[i]
            elif i < 40:
                row5 += printb[i]
            elif i < 48:
                row6 += printb[i]
            elif i < 56:
                row7 += printb[i]
            elif i < 64:
                row8 += printb[i]
        for i in reversed([row1, row2, row3, row4, row5, row6, row7, row8]):
            print i
    return True


def GetPieceLegalMoves(board, position):
    if not isinstance(board, list):
        return -1
    if (len(board) != 64) or (position not in range(0, 64, 1)):
        return -1
    if board[position] == 0:
        return -1
    else:
        piece = board[position]
        identity = piece % 10
        enemy_list = []
        moves = []
        final_moves = []
        if piece >= 20:
            [player, enemy] = [20, 10]
        else:
            [player, enemy] = [10, 20]
        if piece == 0:
            return -1
        for i in range(0, 6, 1):
            enemy_list += [i+enemy]
        # <editor-fold desc="pon logic">
        if identity == 0:
            # White
            if (player == 10) and (position in range(8, 56, 1)):
                if board[position+8] == 0:
                    moves += [position+8]
                if position % 8 == 0:
                    if board[position+9] in enemy_list:
                        moves += [position+9]
                elif position % 8 == 7:
                    if board[position+7] in enemy_list:
                        moves += [position+7]
                else:
                    if board[position+7] in enemy_list:
                        moves += [position+7]
                    if board[position+9] in enemy_list:
                        moves += [position+9]
            # Black
            if (player == 20) and (position in range(8, 56, 1)):
                if board[position-8] == 0:
                    moves += [position-8]
                if position % 8 == 0:
                    if board[position-7] in enemy_list:
                        moves += [position-7]
                elif position % 8 == 7:
                    if board[position-9] in enemy_list:
                        moves += [position-9]
                else:
                    if board[position-7] in enemy_list:
                        moves += [position-7]
                    if board[position-9] in enemy_list:
                        moves += [position-9]
            # return moves
        # </editor-fold>
        # <editor-fold desc="Knight">
        elif identity == 1:
            [x, y] = [(position % 8), (position // 8)]
            target_x = [-2, -2, -1, -1, 1, 1, 2, 2]
            target_y = [1, -1, 2, -2, 2, -2, 1, -1]
            for i in range(0, 8, 1):
                if ((x+target_x[i]) in range(0, 8, 1)) and ((y+target_y[i]) in range(0, 8, 1)):
                    target = (y+target_y[i])*8+(x+target_x[i])
                    if (board[target] == 0) or (board[target] in enemy_list):
                        moves += [target]
            # return moves
        # </editor-fold>

        # <editor-fold desc="Bishop">
        elif identity == 2:
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # up right
            while True:
                x += 1
                y += 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # up Left
            while True:
                x -= 1
                y += 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # Down right
            while True:
                x += 1
                y -= 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # Down left
            while True:
                x -= 1
                y -= 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            # return moves
        # </editor-fold>
        # <editor-fold desc="Rook">
        elif identity == 3:
            target = [position, position, position, position]
            extender = [-1, 1, 8, -8]
            while True:
                upper = len(extender)
                if upper == 0:
                    break
                new_target = []
                new_extender = []
                for i in range(0, upper, 1):
                    [x_prev, y_prev] = [(target[i] % 8), (target[i] // 8)]
                    target[i] += extender[i]
                    [x_after, y_after] = [(target[i] % 8), (target[i] // 8)]
                    t1 = (x_prev == x_after) or (y_prev == y_after)
                    t2 = target[i] in range(0, 64, 1)
                    if t1 and t2:
                        if board[target[i]] == 0:
                            moves += [target[i]]
                            new_extender += [extender[i]]
                            new_target += [target[i]]
                        if board[target[i]] in enemy_list:
                            moves += [target[i]]
                target = new_target
                extender = new_extender
            # return moves
        # </editor-fold>
        # <editor-fold desc="Queen">
        elif identity == 4:
            temp_board_1 = board[:]
            temp_board_2 = board[:]
            temp_board_1[position] = board[position] - 1
            temp_board_2[position] = board[position] - 2
            moves_1 = GetPieceLegalMoves_pseudo(temp_board_1, position)
            moves_2 = GetPieceLegalMoves_pseudo(temp_board_2, position)
            moves = moves_1 + moves_2
            # return moves
        # </editor-fold>
        # <editor-fold desc="King">
        elif identity == 5:
            [x, y] = [(position % 8), (position // 8)]
            target_x = [-1, -1, -1, 0, 0, 1, 1, 1]
            target_y = [1, 0, -1, -1, 1, -1, 0, 1]
            for i in range(0, 8, 1):
                if ((x+target_x[i]) in range(0, 8, 1)) and ((y+target_y[i]) in range(0, 8, 1)):
                    target = (y+target_y[i])*8+(x+target_x[i])
                    if (board[target] == 0) or (board[target] in enemy_list):
                        moves += [target]
            # return moves
        # </editor-fold>
        for i in range(0, len(moves), 1):
            if not IsCheck(board, position, moves[i]):
                final_moves.append(moves[i])
        return final_moves


def IsCheck(board, position, target):
    temp_board = board[:]
    piece = temp_board[position]
    temp_board[position] = 0
    temp_board[target] = piece
    king_at = 5
    if piece >= 20:
        [player, enemy] = [20, 10]
    else:
        [player, enemy] = [10, 20]
    for i in range(0, 64, 1):
        if temp_board[i] == player+5:
            king_at = i
            break
    enemy_pieces = GetPlayerPositions(temp_board, enemy)
    for i in enemy_pieces:
        move_list = GetPieceLegalMoves_pseudo(temp_board, i)
        if king_at in move_list:
            return True
    return False


def CanCheck(board, position, target):
    temp_board = board[:]
    piece = temp_board[position]
    temp_board[position] = 0
    temp_board[target] = piece
    king_at = 5
    if piece >= 20:
        [player, enemy] = [20, 10]
    else:
        [player, enemy] = [10, 20]
    for i in range(0, 64, 1):
        if temp_board[i] == enemy + 5:
            king_at = i
            break
    moves = GetPieceLegalMoves_pseudo(temp_board, target)
    if isinstance(moves, list):
        if king_at in moves:
            return True
    return False


def CanCapture(board, position, target):
    piece = board[position]
    if piece >= 20:
        [player, enemy] = [20, 10]
    else:
        [enemy, player] = [20, 10]
    if board[target] == enemy + 5:
        return True
    else:
        return False


def GetPieceLegalMoves_pseudo(board, position):
    if not isinstance(board, list):
        return -1
    if (len(board) != 64) or (position not in range(0, 64, 1)):
        return -1
    if board[position] == 0:
        return -1
    else:
        piece = board[position]
        identity = piece % 10
        enemy_list = []
        moves = []
        if piece >= 20:
            [player, enemy] = [20, 10]
        elif piece >= 10:
            [player, enemy] = [10, 20]
        else:
            return moves
        for i in range(0, 6, 1):
            enemy_list += [i+enemy]
        # <editor-fold desc="pon logic">
        if identity == 0:
            # White
            if (player == 10) and (position in range(8, 56, 1)):
                if board[position+8] == 0:
                    moves += [position+8]
                if position % 8 == 0:
                    if board[position+9] in enemy_list:
                        moves += [position+9]
                elif position % 8 == 7:
                    if board[position+7] in enemy_list:
                        moves += [position+7]
                else:
                    if board[position+7] in enemy_list:
                        moves += [position+7]
                    if board[position+9] in enemy_list:
                        moves += [position+9]
            # Black
            if (player == 20) and (position in range(8, 56, 1)):
                if board[position-8] == 0:
                    moves += [position-8]
                if position % 8 == 0:
                    if board[position-7] in enemy_list:
                        moves += [position-7]
                elif position % 8 == 7:
                    if board[position-9] in enemy_list:
                        moves += [position-9]
                else:
                    if board[position-7] in enemy_list:
                        moves += [position-7]
                    if board[position-9] in enemy_list:
                        moves += [position-9]
            return moves
        # </editor-fold>
        # <editor-fold desc="Knight">
        elif identity == 1:
            [x, y] = [(position % 8), (position // 8)]
            target_x = [-2, -2, -1, -1, 1, 1, 2, 2]
            target_y = [1, -1, 2, -2, 2, -2, 1, -1]
            for i in range(0, 8, 1):
                if ((x+target_x[i]) in range(0, 8, 1)) and ((y+target_y[i]) in range(0, 8, 1)):
                    target = (y+target_y[i])*8+(x+target_x[i])
                    if (board[target] == 0) or (board[target] in enemy_list):
                        moves += [target]
            return moves
        # </editor-fold>

        # <editor-fold desc="Bishop">
        elif identity == 2:
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # up right
            while True:
                x += 1
                y += 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # up Left
            while True:
                x -= 1
                y += 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # Down right
            while True:
                x += 1
                y -= 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            target = position
            [x, y] = [(target % 8), (target // 8)]
            # Down left
            while True:
                x -= 1
                y -= 1
                if (x in range(0, 8, 1)) and (y in range(0, 8, 1)):
                    target = y * 8 + x
                    if board[target] == 0:
                        moves += [target]
                    elif board[target] in enemy_list:
                        moves += [target]
                        break
                    else:
                        break
                else:
                    break
            return moves
        # </editor-fold>
        # <editor-fold desc="Rook">
        elif identity == 3:
            target = [position, position, position, position]
            extender = [-1, 1, 8, -8]
            while True:
                upper = len(extender)
                if upper == 0:
                    break
                new_target = []
                new_extender = []
                for i in range(0, upper, 1):
                    [x_prev, y_prev] = [(target[i] % 8), (target[i] // 8)]
                    target[i] += extender[i]
                    [x_after, y_after] = [(target[i] % 8), (target[i] // 8)]
                    t1 = (x_prev == x_after) or (y_prev == y_after)
                    t2 = target[i] in range(0, 64, 1)
                    if t1 and t2:
                        if board[target[i]] == 0:
                            moves += [target[i]]
                            new_extender += [extender[i]]
                            new_target += [target[i]]
                        if board[target[i]] in enemy_list:
                            moves += [target[i]]
                target = new_target
                extender = new_extender
            return moves
        # </editor-fold>
        # <editor-fold desc="Queen">
        elif identity == 4:
            temp_board_1 = board[:]
            temp_board_2 = board[:]
            temp_board_1[position] = board[position] - 1
            temp_board_2[position] = board[position] - 2
            moves_1 = GetPieceLegalMoves_pseudo(temp_board_1, position)
            moves_2 = GetPieceLegalMoves_pseudo(temp_board_2, position)
            moves = moves_1 + moves_2
            return moves
        # </editor-fold>
        # <editor-fold desc="King">
        elif identity == 5:
            [x, y] = [(position % 8), (position // 8)]
            target_x = [-1, -1, -1, 0, 0, 1, 1, 1]
            target_y = [1, 0, -1, -1, 1, -1, 0, 1]
            for i in range(0, 8, 1):
                if ((x+target_x[i]) in range(0, 8, 1)) and ((y+target_y[i]) in range(0, 8, 1)):
                    target = (y+target_y[i])*8+(x+target_x[i])
                    if (board[target] == 0) or (board[target] in enemy_list):
                        moves += [target]
            return moves
        # </editor-fold>


def IsPositionUnderThreat(board, position, player):
    if not isinstance(board, list):
        return False
    if not isinstance(position, int):
        return False
    if not isinstance(player, int):
        return False
    else:
        if player == 20:
            enemy = 10
        elif player == 10:
            enemy = 20
        for i in range(0, 64, 1):
            if (board[i] - enemy) in range(0, 6, 1):
                move_list = GetPieceLegalMoves(board, i)
                if position in move_list:
                    return True
    return False


def move(board, position, target):
    piece = board[position]
    board[position] = 0
    board[target] = piece
    return True


def player_win(board, player):
    if player == 10:
        enemy = 20
    else:
        enemy = 10
    king_at = 0
    for i in range(0, 64, 1):
        if board[i] == enemy+5:
            king_at = i
            break
    king_moves = GetPieceLegalMoves(board, king_at)
    threat = IsPositionUnderThreat(board, king_at, enemy)
    if len(king_moves) == 0 and threat:
        return True
    else:
        return False


def position_value(board, position):
    value = 0
    piece_value = [100, 320, 330, 500, 900, 20000]
    board_value_select = []
    # position value is made from the view of the white side, top down, flip for black
    pawn_val = [0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10, 5, 5, 10, 25, 25, 10, 5, 5, 0, 0, 0, 20, 20, 0, 0, 0, 5, -5, -10, 0, 0, -10, -5, 5, 5, 10, 10, -20, -20, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    knight_val = [-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 0, 0, 0, -20, -40, -30, 0, 10, 15, 15, 10, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 10, 15, 15, 10, 5, -30, -40, -20, 0, 5, 5, 0, -20, -40, -50, -40, -30, -30, -30, -30, -40, -50]
    bishop_val = [-20, -10, -10, -10, -10, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 10, 10, 5, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 10, 10, 10, 10, 10, 10, -10, -10, 5, 0, 0, 0, 0, 5, -10, -20, -10, -10, -10, -10, -10, -10, -20]
    rook_val = [0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, 10, 10, 10, 10, 5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 5, 5, 0, 0, 0]
    queen_val = [-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 5, 5, 5, 0, -10, -5, 0, 5, 5, 5, 5, 0, -5, 0, 0, 5, 5, 5, 5, 0, -5, -10, 5, 5, 5, 5, 5, 0, -10, -10, 0, 5, 0, 0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20]
    king_val = [-30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -20, -30, -30, -40, -40, -30, -30, -20, -10, -20, -20, -20, -20, -20, -20, -10, 20, 20, 0, 0, 0, 0, 20, 20, 20, 30, 10, 0, 0, 10, 30, 20]
    king_val_end = [-50, -40, -30, -20, -20, -30, -40, -50, -30, -20, -10, 0, 0, -10, -20, -30, -30, -10, 20, 30, 30, 20, -10, -30, -30, -10, 30, 40, 40, 30, -10, -30, -30, -10, 30, 40, 40, 30, -10, -30, -30, -10, 20, 30, 30, 20, -10, -30, -30, -30, 0, 0, 0, 0, -30, -30, -50, -30, -30, -30, -30, -30, -30, -50]
    piece  = board[position]
    if piece == 0:
        return 0
    else:
        identity = piece % 10
        player = (piece // 10) * 10
        value += piece_value[identity]
        if identity == 0:
            board_value_select = pawn_val[:]
        elif identity == 1:
            board_value_select = knight_val[:]
        elif identity == 2:
            board_value_select = bishop_val[:]
        elif identity == 3:
            board_value_select = rook_val[:]
        elif identity == 4:
            board_value_select = queen_val[:]
        elif identity == 5:
            if len(GetPlayerPositions(board,player)) < 6:
                board_value_select = king_val_end[:]
            else:
                board_value_select = king_val[:]
        if player == 10:
            value += board_value_select[-position - 1]
            return value
        else:
            value = (-1) * value
            value -= board_value_select[position]
            return value


def board_value(board):
    white_list = GetPlayerPositions(board, 10)
    black_list = GetPlayerPositions(board, 20)
    value = 0
    for i in white_list:
        value += position_value(board, i)
    for i in black_list:
        value += position_value(board, i)
    # value = value + zone_attack_value(board, 10) - zone_attack_value(board, 20)
    return value


def gen_king_zone(board, player):
    king_at = 0
    for i in range(0, len(board), 1):
        if board[i] == player + 5:
            king_at = i
    [king_x, king_y] = [king_at % 8, king_at // 8]
    target_x = [-1, -1, -1, 0, 0, 1, 1, 1]
    target_y = [1, 0, -1, -1, 1, -1, 0, 1]
    zone = [king_at]
    for i in range(0, 8, 1):
        if ((king_x + target_x[i]) in range(0, 8, 1)) and ((king_y + target_y[i]) in range(0, 8, 1)):
            target = (king_y + target_y[i]) * 8 + (king_x + target_x[i])
            zone += [target]
    return zone


def zone_attack_value(board, player):
    pieces = GetPlayerPositions(board, player)
    multiplier = [10, 20, 20, 40, 80, 10]
    attacker_multiplier = [0, 0, 50, 75, 88, 94, 97, 99, 100, 101, 102]
    value = 0
    attacking_piece_count = 0
    if player == 10:
        enemy = 20
    else:
        enemy = 10
    enemy_zone = gen_king_zone(board, enemy)
    for i in pieces:
        piece = board[i]
        moves = GetPieceLegalMoves(board, i)
        square_count = 0
        if isinstance(moves, list):
            for j in moves:
                if j in enemy_zone:
                    square_count += 1
        if square_count != 0:
            attacking_piece_count += 1
        value += square_count * (multiplier[piece % 10])
    score = value * attacker_multiplier[attacking_piece_count] / 100
    return score


# step 1, get all possible moves of the player
# step 2, analyze opponent's response

# step 1
def gen_possible_moves(tree, player):
    board = tree.board
    pieces = GetPlayerPositions(board, player)
    exist_move = False
    for i in pieces:
        moves = GetPieceLegalMoves(board, i)
        if isinstance(moves, list):
            for j in moves:
                exist_move = True
                child = chess_tree(board, [i, j])
                tree.add_child(child)
    return exist_move
# step 1 complete :)


# step 2, analyze opponent's response for each move
def gen_opponent_response(move_tree, player):
    if player == 10:
        enemy = 20
    else:
        enemy = 10
    enemy_pieces = GetPlayerPositions(move_tree.board, enemy)
    extreme_board_value = 0
    exist_moves = False
    for i in enemy_pieces:
        moves_list = GetPieceLegalMoves(move_tree.board, i)
        if isinstance(moves_list, list):
            for j in moves_list:
                exist_moves = True
                child = chess_tree(move_tree.board, [i, j])
                board_val = child.val
                if CanCheck(child.board, i, j):
                    board_val += (player - 25) * 200
                if enemy == 20:
                    if board_val < extreme_board_value:
                        extreme_board_value = board_val
                        move_tree.subtrees = []
                        move_tree.add_child(child)
                else:
                    if board_val > extreme_board_value:
                        extreme_board_value = board_val
                        move_tree.subtrees = []
                        move_tree.add_child(child)
    return exist_moves


def gen_third_n_fourth_levels(move_tree, player):
    if move_tree.subtrees == []:
        return False
    counter_1 = move_tree.subtrees[0]
    r = gen_possible_moves(counter_1, player)
    extreme_value = 0
    if r is False:
        return False
    for second_move in counter_1.subtrees:
        r = gen_opponent_response(second_move, player)
    # Now we prune
        if player == 10:
            if second_move.val < extreme_value:
                counter_1.val = second_move.val
                move_tree.val = second_move.val
        else:
            if second_move.val > extreme_value:
                counter_1.val = second_move.val
                move_tree.val = second_move.val
    return True


def chessPlayer(board, player):
    start = time.time()
    if (not isinstance(board, list)) or (player not in [10, 20]):
        return [False, [], [], 0]
    else:
        root = chess_tree(board, [])
        move_choice = []
        candidate_moves = []
        gen_possible_moves(root, player)
        if len(root.subtrees) == 0:
            return [False, move_choice, candidate_moves, root]
        phase_1 = time.time()
        if phase_1 - start > 0.35:
            for i in root.subtrees:
                candidate_move = [i.pos_tar, i.val]
                candidate_moves += [candidate_move]
        else:
            for i in root.subtrees:
                r = gen_opponent_response(i, player)
                phase_2 = time.time()
                if phase_2 - start < 2:
                    r = gen_third_n_fourth_levels(i, player)
                if len(i.subtrees) != 0:
                    candidate_move = [i.pos_tar, i.subtrees[0].val]
                else:
                    candidate_move = [i.pos_tar, i.val]
                candidate_moves += [candidate_move]
        for i in candidate_moves:
            if CanCapture(board, i[0][0], i[0][1]):
                move_choice = i[0]
        if move_choice == []:
            current_best_val = candidate_moves[0][1]
            current_best_move = candidate_moves[0][0]
            if player == 10:
                for i in candidate_moves:
                    if i[1] > current_best_val:
                        current_best_val = i[1]
                        current_best_move = i[0]
            if player == 20:
                for i in candidate_moves:
                    if i[1] < current_best_val:
                        current_best_val = i[1]
                        current_best_move = i[0]
            move_choice = current_best_move
        return [True, move_choice, candidate_moves, root]


class queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, x):
        self.storage += [x]
        return True

    def dequeue(self):
        if len(self.storage) == 0:
            return [False, []]
        else:
            a = self.storage[0]
            if len(self.storage) > 1:
                self.storage = self.storage[1:]
            else:
                self.storage = []
            return [True, a]


class chess_tree:
    def __init__(self, board, move_list):
        self.subtrees = []
        self.pos_tar = move_list
        self.board = board[:]
        self.val = 0
        if len(move_list) == 2:
            move(self.board, move_list[0], move_list[1])
        self.val = board_value(self.board)/1.0

    def add_child(self, child):
        if not isinstance(child, chess_tree):
            return False
        else:
            self.subtrees += [child]
            return True

    def get_level_order_traversal(self):
        x = queue()
        x.enqueue(self)
        accum = []
        while True:
            y = x.dequeue()
            if y[0] is False:
                break
            else:
                item = [y[1].pos_tar, y[1].board]
                accum = accum + [item]
                for i in y[1].subtrees:
                    x.enqueue(i)
        return accum