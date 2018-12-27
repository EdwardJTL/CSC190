from chessLib import *
import chess1
import ezchess_old as chess2
import ezchess as chess3
from time import *
#from chessPlayer_tree import *

def getPlayerMove(board, player):
   if player==10:
      player_string="White"
   elif player==20:
      player_string="Black"

   while True:
      try:
         x=True
         pos=raw_input(player_string+" please pick a piece: ")
         x=ord(pos[0])-97
         if x<0:
            x=ord(pos[0])-65
         piece=x+(int(pos[1])-1)*8
         valid=0
         for i in GetPlayerPositions(board,player):
            if piece==i:
               valid=1
         if valid==1:
            if GetPieceLegalMoves(board,piece)!=[]:
               break
         print "Invalid Piece"
      except:
         print "Invalid Piece"
   print GetPieceLegalMoves(board,piece)
   if board[piece]%10==0:
      piece_string="P"
   if board[piece]%10==1:
      piece_string="H"
   if board[piece]%10==2:
      piece_string="B"
   if board[piece]%10==3:
      piece_string="R"
   if board[piece]%10==4:
      piece_string="Q"
   if board[piece]%10==5:
      piece_st
      ring="K"

   while True:
      try:
         pos=raw_input(player_string+"["+piece_string+"] please pick a move: ")
         x=ord(pos[0])-97
         if x<0:
            x=ord(pos[0])-65
         move=x+(int(pos[1])-1)*8
         valid=0
         for i in GetPieceLegalMoves(board,piece):
            if move==i:
               valid=1
         if valid==1:
            break
         print "Invalid Move"
      except:
         print "Invalid Move"
   Move(board,piece,move)
   return True

def getRandomMove(board,player):
   from random import randint
   pieces=[]
   for i in GetPlayerPositions(board,player):
      if GetPieceLegalMoves(board,i)!=[]:
         pieces+=[i]
   piece=pieces[randint(0,len(pieces)-1)]
   moves=GetPieceLegalMoves(board,piece)
   Move(board,piece,moves[randint(0,len(moves)-1)])
   return True

def getSmartMove(board,player):
   thing=chessPlayer(board,player)
   move=thing[1]
   print thing[2]
   #print thing[1]
   #print thing[3]
   Move(board,move[0],move[1])
   return True

def getSmartMove1(board,player):
   thing=chess1.chessPlayer(board,player)
   move=thing[1]
   print thing[2]
   #print thing[1]
   #print thing[3]
   Move(board,move[0],move[1])
   return True

def getSmartMove2(board,player):
   thing=chess2.chessPlayer(board,player)
   move=thing[1]
   print thing[2]
   #print thing[1]
   #print thing[3]
   Move(board,move[0],move[1])
   return True

def getSmartMove3(board,player):
   thing=chess3.chessPlayer(board,player)
   move=thing[1]
   print thing[2]
   #print thing[1]
   #print thing[3]
   Move(board,move[0],move[1])
   return True

def game(humans):
   Max=0
   board=Board()
   player=1
   PrintBoard(board)
   while CheckMate(board,10)==CheckMate(board,20)==False:
      if humans[player]==1:
         getPlayerMove(board,player*10)
      elif humans[player]==2:
         start=time()
         getSmartMove(board,player*10)
         end=time()
         Max=max(Max,end-start)
         #print end-start
      elif humans[player]==3:
         start=time()
         getSmartMove1(board,player*10)
         end=time()
         Max=max(Max,end-start)
         print end-start
      elif humans[player]==4:
         start=time()
         getSmartMove2(board,player*10)
         end=time()
         Max=max(Max,end-start)
         print end-start
      elif humans[player]==5:
         start=time()
         getSmartMove3(board,player*10)
         end=time()
         Max=max(Max,end-start)
         print end-start
      else:
         getRandomMove(board,player*10)
      PrintBoard(board)
      player=player%2+1
      sleep(humans[0])
   if CheckMate(board,20):
      print "White Wins"
      print "Max Time: ",Max
      return 10
   if CheckMate(board,10):
      print "Black Wins"
      print "Max Time: ",Max
      return 20

thing=[0,0,0]
stuff=raw_input()
x=0
acc=''
for i in stuff:
   if i==',':
      thing[x]=float(acc)
      acc=''
      x+=1
   else:
      acc+=i
thing[x]=float(acc)
game(thing)
   


            
