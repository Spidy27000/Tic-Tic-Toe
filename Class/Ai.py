class Ai:
    def __init__(self,board,player):
        self.board = board
        self.player = player
    
    def minmax(self, board ,depth, alpha, beta, isMaximaxing):
        if board.state() != None:
            return board.state()

        if isMaximaxing:
            score = -float("inf")
            moves = board.get_valid_moves()
            for move in moves:
                copyboard = board.copy()
                copyboard.make_move(move,"X")
                score = max(score, minmax(copyboard, depth + 1, alpha, beta, False))
                alpha = max(score, alpha)
                if alpha >= beta:
                    break
                copyboard.make_move(move," ")
            return score
        else:
            score = float("inf")
            moves = board.get_valid_moves()
            for move in moves:
                copyboard = board.copy()
                copyboard.make_move(move,"O")
                score = min(score, minmax(copyboard, depth + 1, alpha, beta, True))
                beta = min(score, beta)
                if alpha >= beta:
                    break
                copyboard.make_move(move," ")
            return score


    def get_best_move(self):
        moves = self.board.get_valid_moves()
        bestMove = 22
        if self.player =="O":
            bestScore = float("inf")
            for move in moves:
                copyboard = board.copy()
                copyboard.make_move(move,"O")
                score = minmax(copyboard, 0, -float("inf"), float("inf"), True)
                if int(score) < bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = -float("inf")
            for move in moves:
                copyboard = board.copy()
                copyboard.make_move(move,"O")
                score = minmax(copyboard, 0, -float("inf"), float("inf"), False)
                if int(score) > bestScore:
                    bestScore = score
                    bestMove = move

        return bestMove
