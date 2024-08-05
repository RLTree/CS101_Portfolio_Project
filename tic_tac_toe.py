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
    the computer (PvE), or against another player (PvP). When prompted, choose "PvE" or "PvP", whether 
    you would like to be "X" or "O", and who will go first. 
    
    Players take turns filling in the squares on the standard 3 x 3 grid until either one player wins by
    filling 3 squares in a row, or all 9 squares are filled. If all 9 squares are filled, but neither 
    player has 3 squares in a row, the game ends in a draw.

    Enjoy the game!     
    """

class Player:

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return f"Logic for setting up Player #1 and their symbols for the game."
  
  def setup_Player(self):
    try:
      self.symbol = str(input("Will you be 'X' or 'O'?").strip() or "X")
      while self.symbol != "X" and self.symbol != "O":
        self.symbol = str(input("Sorry! Other symbol options are not currently supported. Please choose either 'X' or 'O'.").strip() or "X")
    except EOFError:
      self.symbol = "X"

class Computer:

  def __init__(self, difficulty_level):
    self.difficulty = difficulty_level
    self.symbol = 'O' if player.symbol == 'X' else 'X'
    
    if self.difficulty == "Easy" or self.difficulty == "1":
      self.setup_easy("TicTacTyro")
    elif self.difficulty == "Medium" or self.difficulty == "2":
      self.setup_medium("TicTacPro")
    elif self.difficulty == "Hard" or self.difficulty == "3":
      self.setup_hard("TacToeTerminator")
  
  def __repr__(self):
    return "Logic for setting up a computer if PvE mode is selected."
  
  def setup_easy(self, name):
    self.name = name
    pass

  def setup_medium(self, name):
    self.name = name
    pass

  def setup_hard(self, name):
    self.name = name
    pass

class Opponent:

  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol
  
  def __repr__(self):
    return "Logic for setting up Player #2 if PvP mode is selected."

class TicTacToe:

  def __init__(self, player, opponent):
    self.player = player
    self.opponent = opponent
    self.starter = self.decide_starting_player()

    if isinstance(self.opponent, Computer):
      self.start_game_PvE(self.player, self.opponent, self.starter)
    elif isinstance(self.opponent, Opponent):
      self.start_game_PvP(self.player, self.opponent, self.starter)
  
  def __repr__(self):
    return "Game Logic for Tic Tac Toe."
  
  def decide_starting_player(self):
    try:
      starter = str(input("Who will start the game? Player 1 or Player 2 ").strip() or 'Player 1')
      while starter != 'Player 1' and starter != 'Player 2':
        starter = str(input("The game currently doesn't answers outside of Player 1 or Player 2. If you are playing against a computer and would like it to start, select Player 2. Player 1 or Player 2? ").strip() or 'Player 1')
    except EOFError:
      starter = 'Player 1'
    
    return starter
  
  def start_game_PvE(self, player, opponent, starter):
    self.player = player
    self.opponent = opponent
    self.starter = starter

  def start_game_PvP(self, player, opponent, starter):
    self.player = player
    self.opponent = opponent
    self.starter = starter
  
class Board:

  def __init__(self):
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
  
  def display_Board(self, player1_moves, player2_moves):
    self.player1_moves = []
    self.player2_moves = []





instructions = Instructions()
print(instructions)