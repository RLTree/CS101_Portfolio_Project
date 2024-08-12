import random

class Instructions:

  def __init__(self):
    return
  
  def __repr__(self):
    return """
    #######    #######    #######      #######     #####     #######      #######    #######    ####### 
       #          #       #               #       #     #    #               #       #     #    #    
       #          #       #               #       #     #    #               #       #     #    #    
       #          #       #               #       #######    #               #       #     #    ####
       #          #       #               #       #     #    #               #       #     #    #    
       #          #       #               #       #     #    #               #       #     #    #    
       #       #######    #######         #       #     #    #######         #       #######    #######
    ---------------------------------------------------------------------------------------------------
    Welcome to Tic-Tac-Toe!
    ---------------------------------------------------------------------------------------------------
    Instructions:
    This is a Python Terminal game based on the classic "Tic-Tac-Toe". You can play this game against 
    another player (PvP). When prompted, choose your names, whether you would like to be "X" or "O", 
    and who will go first. 
    
    Players take turns filling in the squares on the standard 3 x 3 grid until either one player wins by
    filling 3 squares in a row, or all 9 squares are filled. If all 9 squares are filled, but neither 
    player has 3 squares in a row, the game ends in a draw.

    Enjoy the game!     
    """

class Players:

  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.setup_symbols()
  
  def __repr__(self):
    return f"Logic for setting up Player #1 and their symbols for the game."
  
  def setup_symbols(self):
    try:
      self.player1_symbol = str(input(f"{self.player1}, will you be 'X' or 'O'?\n\n").strip() or "X")
      while self.player1_symbol != "X" and self.player1_symbol != "O":
        self.player1_symbol = str(input("Sorry! Other symbol options are not currently supported. Please choose either 'X' or 'O'.\n\n").strip() or "X")
    except EOFError:
      self.player1_symbol = "X"

    if self.player1_symbol == "X":
      self.player2_symbol = "O"
    else:
      self.player2_symbol = "X"


class TicTacToe:

  def __init__(self, players, board):
    self.players = players
    self.board = board
    self.starter = self.decide_starting_player()

    if self.starter == "Player 1":
      while True:
        self.player_1_move()

        for combo in winning_combinations:
          
          if all(move in board.player1_moves for move in combo):
            board.display_board()
            return print(f"Congratulations, {players.player1}! You won!\n\n")
      
        self.player_2_move()

        for combo in winning_combinations:

          if all(move in board.player2_moves for move in combo):
            board.display_board()
            return print(f"Congratulations, {players.player2}! You won!\n\n")
  
    else:
      while True:

        self.player_2_move()
      
        for combo in winning_combinations:

          if all(move in board.player2_moves for move in combo):
            board.display_board()
            return print(f"Congratulations, {players.player2}! You won!\n\n") 
        
        self.player_1_move()

        for combo in winning_combinations:

          if all(move in board.player1_moves for move in combo):
            board.display_board()
            return print(f"Congratulations, {players.player1}! You won!\n\n")
            
          


  def __repr__(self):
    return "Game Logic for Tic Tac Toe."
  
  def decide_starting_player(self):
    try:
      starter = str(input("Who will start the game? Player 1 or Player 2?\n\n").strip() or 'Player 1')
      while starter != 'Player 1' and starter != 'Player 2':
        starter = str(input("The game currently doesn't accept answers outside of Player 1 or Player 2. Will Player 1 or Player 2 start?\n\n").strip() or 'Player 1')
    except EOFError:
      starter = 'Player 1'
    
    return starter

  def player_1_move(self):
    board.display_board()
    try:
      p1_choice = int(input(f"{players.player1}, make your move.\n") or 1)
      while p1_choice not in range(1, 10) or p1_choice in board.player2_moves or p1_choice in board.player1_moves:
        board.display_board()
        p1_choice = int(input("\nYour move is not a valid move. Select an available square (1-9).\n") or 1)
    except EOFError:
      p1_choice = 1
    
    board.player1_moves.append(p1_choice)
    board.player1_moves.sort()

  def player_2_move(self):
    board.display_board()
    try:
      p2_choice = int(input(f"\n{players.player2}, make your move.\n") or 1)
      while p2_choice not in range(1,10) or p2_choice in board.player1_moves or p2_choice in board.player2_moves:
        board.display_board()
        p2_choice = int(input("\nYour move is not a valid move. Select an available square (1-9).\n") or 1)
    except EOFError:
        p2_choice = 1
      
    board.player2_moves.append(p2_choice)
    board.player2_moves.sort()

  
class Board:

  def __init__(self, players):
    self.board = [
      1, 2, 3,
      4, 5, 6, 
      7, 8, 9
      ]
    self.visual_board = ("""
     1 | 2 | 3 
    -----------
     4 | 5 | 6 
    -----------
     7 | 8 | 9 
     """)
  
  def display_board(self, player1_moves = [], player2_moves = []):
    
    self.player1_moves = player1_moves
    self.player2_moves = player2_moves

    for i, move in enumerate(self.board):
      if move in self.player1_moves:
        self.board[i] = players.player1_symbol
        self.visual_board = self.visual_board.replace(str(move), players.player1_symbol)
    
    for i, move in enumerate(self.board):
      if move in self.player2_moves:
        self.board[i] = players.player2_symbol
        self.visual_board = self.visual_board.replace(str(move), players.player2_symbol) 

    print(self.visual_board)


winning_combinations = (
[1,4,7],
[1,5,9],
[1,2,3],
[2,5,8],
[3,5,7],
[3,6,9],
[4,5,6],
[7,8,9]
)


instructions = Instructions()
print(instructions)

try:
  player1 = str(input("\n\nHello, Player 1! What should I call you?\n\n").strip() or "Player 1")
  player2 = str(input("\n\nHello, Player 2! What should I call you?\n\n").strip() or "Player 2")
except EOFError:
  player1 = "Player 1"
  player2 = "Player 2"

players = Players(player1, player2)
board = Board(players)
game = TicTacToe(players, board)