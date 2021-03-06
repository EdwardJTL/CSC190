
def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")

   return r

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def GetPlayerPositions(board,player):
   W = 10
   B = 20
   if (player!=W) and (player!=B):
      return []
   else:
      x0=zip(board,range(0,64,1))
      x1=filter(lambda x : ((x[0]-player) < W) and ((x[0]-player) >= 0), x0)
      return map(lambda x:x[1],x1)


print printBoard(range(0,64,1))
board=genBoard()
print "raw board is: (index=0 ... index=63):"
print board
print "\nwhich will look like the following:"
print printBoard(genBoard())
print ""
print " Note 1: lower right hand square is WHITE"
print " Note 2: two upper rows are for BLACK PIECES"
print " Note 3: two lower rows are for WHITE PIECES"


print "White occupies:"
print GetPlayerPositions(board,10)
print "Black occupies:"
print GetPlayerPositions(board,20)

def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False

def GetBishopMoves(pos):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum=[]
   ul = pos
   ll = pos
   ur = pos
   lr = pos
   for i in range(0,nr,1):
      ur += 7
      lr -= 9
      if IsOnBoard(lr):
         accum += [lr]
      if IsOnBoard(ur):
         accum += [ur]

   for i in range(0,nl,1):
      ul += 9
      ll -= 7
      if IsOnBoard(ul):
         accum += [ul]
      if IsOnBoard(ll):
         accum += [ll]
   return accum

def GetRookMoves(pos):
   nl = pos % 8
   nr = 7 - (pos % 8)
   nd = pos / 8
   nu = 7 - (pos / 8)
   #print nl,nr,nd,nu
   accum=[]
   l=r=u=d=pos
   for i in range(0,nl,1):
      l -= 1
      if IsOnBoard(l):
         accum += [l]

   for i in range(0,nr,1):
      r += 1
      if IsOnBoard(r):
         accum += [r]

   for i in range(0,nd,1):
      d -= 8
      if IsOnBoard(d):
         accum += [d]

   for i in range(0,nu,1):
      u += 8
      if IsOnBoard(u):
         accum += [u]

   return accum

def GetQueenMoves(pos):
   return GetRookMoves(pos) + GetBishopMoves(pos)

#print GetBishopMoves(50)
#print GetRookMoves(34)
print GetQueenMoves(34)