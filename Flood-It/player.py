import random
import math
##from priorityq import PQ

class Player():

    def __init__(self):
        pass


# random move
class PlayerRandom(Player):

    def __init__(self):
        super().__init__()

    def findMove(self, board):
        children = board.children()

        return random.choice(children)[1]



# greedy algorithm
class PlayerNaive(Player):
    def __init__(self):
        super().__init__()

    def findMove(self, board):
        children = list(sorted(board.children(), key=lambda x: x[0].score()))
        
        return children[0][1]



# n-step ahead
class PlayerStep(Player):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth

    def findMove(self, board):
        return self.findMoveHelper(board, self.depth)[1]

    def findMoveHelper(self, board, depth):

        if board.isOver():
            return (board.scoree(), -1)
        elif depth == 0:
            return (board.scoree(), -1)

        best = -math.inf
        move = ""
        for child in board.children():
            temp = self.findMoveHelper(child[0], depth-1)[0]
            if temp > best:
                best = temp
                move = child[1]

        return (best, move)


# BFS
class PlayerBFS(Player):
    def __init__(self, board):
        super().__init__()
        self.open = [(board, "")]
        self.board = board

    def findMove(self):

        x = 0
        while len(self.open) > 0:
            print(x)
            x+=1

            b, move = self.open[0]

            if b.isOver():
                print(move)
                return move

            children = b.children()
            for child, m in children:
                self.open.append((child, move+m))

            del self.open[0]


# Dynamic Programming that saves states and cuts branches that have seen before
class PlayerDP(Player):
    def __init__(self, board):
        super().__init__()
        self.closedSet = []
        self.open = [(board, "")]
        self.board = board

    def findMove(self):

        x = 0
        while len(self.open) > 0:
            print(x)
            x+=1

            b, move = self.open[0]

            if b.isOver():
                print(move)
                return move
                
            if b.GROUPS in self.closedSet:
                del self.open[0]
                print("Cut")
                continue

            children = b.children()
            for child, m in children:
                self.open.append((child, move+m))

            self.closedSet.append(b.GROUPS)
            del self.open[0]




if __name__ == '__main__':
    from board import Board
    import copy
    while True:
        try:
            N = int(input("Size of the Board: (8 is recommended for testing)"))
            M = int(input("Number of colors: (4 is recomended for testing)"))
            a = input("Select search algorithm type: (RAND, GREED, DEPTH, BFS, DP)")
            if a.upper() in "RANDGREEDDEPTHBFSDP":
                if a.upper() == "DEPTH":
                    d = int(input("Search Depth: (3 is recommended)"))
                break
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")
                    
    i = 0
    b = Board(size=N, color=M)
    b.print()
    if a.upper() == "RAND":
        p = PlayerRandom()
        while not b.isOver():
            i+=1
            print(i)
            m = p.findMove(b)
            print(m)
            b.move(m)
            b.print()
    elif a.upper() == "GREED":
        p = PlayerNaive()
        while not b.isOver():
            i+=1
            print(i)
            m = p.findMove(b)
            print(m)
            b.move(m)
            b.print()
    elif a.upper() == "DEPTH":
        p = PlayerStep(d)
        while not b.isOver():
            i+=1
            print(i)
            m = p.findMove(b)
            print(m)
            b.move(m)
            b.print()
    elif a.upper() == "BFS":
        p = PlayerBFS(b)
        for c in p.findMove():
            i+=1
            print(i)
            b.move(c)
            b.print()
    elif a.upper() == "DP":
        p = PlayerDP(b)
        for c in p.findMove():
            i+=1
            print(i)
            b.move(c)
            b.print()
    else:
        print("ERROR")
