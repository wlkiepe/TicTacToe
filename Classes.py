from tkinter import *
from tkinter import messagebox

# Create a turn variable which will help keep track of if it is X's turn or 0's turn
turn = 0
# Create a dictionary to help keep track of who won. What is going to happen is as X's and O's are added to the board
# the scores in the appropriate row, column, or diagonal will change and the program will know if somebody wins if
# any of the scores reach either 3 (in which case X will win) or -3 (in which case O will win)
score = {
    'row1': 0,
    'row2': 0,
    'row3': 0,
    'col1': 0,
    'col2': 0,
    'col3': 0,
    'diag1': 0,
    'diag2': 0
}

# Create a class called MyButton that inherits the properties of TkInter's Button class, but will allow me to add
# specific features that I will need the buttons to be able to do.
class MyButton(Button):
    
# In my original code the first thing I struggled with was efficiently placing the buttons. Here I require an x and y
# coordinate to be input as a part of the init to tell the button where it will be placed
    def __init__(self, x, y):
        super().__init__()
        global turn
        self.xcor = x
        self.ycor = y
        self.button = Button(width=8, text='TicTacToe', command=self.press)
        self.label = Label(bg='#84D2C5', font=('Arial', 32, "bold"))
        self.turn = 1
# The buttons keep track of the score. Each value is put as na because I was getting a bug when I tried setting the
# values to numbers and this seemed to be the easiest fix
        self.score = {
            'row1': 'na',
            'row2': 'na',
            'row3': 'na',
            'col1': 'na',
            'col2': 'na',
            'col3': 'na',
            'diag1': 'na',
            'diag2': 'na'
        }

    def press(self):
        self.turn_tracker()
        # This if else portions seems wonky, but for some reason the buttons weren't keeping track of the turns 
        # properly and adding the if self.turn == turn portion fixed that bug. I have a hunch that I can get rid of 
        # some of these lines of codes, but I am happy with how the program runs, so I don't feel the need to do that
        if self.turn == turn:
            # The button will destroy itself, then check the turn and depending on whose turn it is will either replace
            # the button with an 'X' or an 'O' after checking whose turn it was and will update the score tracker 
            # appropriately
            self.button.destroy()
            if self.turn % 2 == 1:
                self.label.config(text='X', fg='#13005A')
                self.label.place(x=self.xcor + 15, y=self.ycor - 20)
                self.x_score()
            else:
                self.label.config(text='O', fg='red')
                self.label.place(x=self.xcor+15, y=self.ycor-20)
                self.o_score()
        else:
            self.turn = turn
            self.button.destroy()
            if self.turn % 2 == 1:
                self.label.config(text='X', fg='#13005A')
                self.label.place(x=self.xcor + 15, y=self.ycor - 20)
                self.x_score()
            else:
                self.label.config(text='O', fg='#820000')
                self.label.place(x=self.xcor + 15, y=self.ycor - 20)
                self.o_score()
            
    # Create a method to allow me to place the button where I want it to go on my canvas
    def place(self):
        self.button.place(x=self.xcor, y=self.ycor)
    
    # The turn tracker keeps track of the turn which is used to determine if 'X' is playing or 'O' is playing
    def turn_tracker(self):
        global turn
        if turn < 10:
            turn = turn + 1
            return turn
    
    # Create a method to update the score for 'X'. Based on the coordinate of the button, the method will know which
    # row, column, and diagonal the 'X' was placed, and will add a point to each of those values. It then checks to 
    # see if the game is over using the game_over method created later. 
    def x_score(self):
        global score
        # This first if statement makes sure that the self.score of the button is set to the score of the game so that 
        # it can accurately keep track and update the score.
        if self.score != score:
            self.score = score
            if self.xcor < 200:
                self.score['col1'] += 1
                if self.ycor < 200:
                    self.score['row1'] += 1
                    self.score['diag1'] += 1
                elif self.ycor < 400:
                    self.score['row2'] += 1
                else:
                    self.score['row3'] += 1
                    self.score['diag2'] += 1
                self.game_over()
            elif self.xcor < 400:
                self.score['col2'] += 1
                if self.ycor < 200:
                    self.score['row1'] += 1
                elif self.ycor < 400:
                    self.score['row2'] += 1
                    self.score['diag1'] += 1
                    self.score['diag2'] += 1
                else:
                    self.score['row3'] += 1
                self.game_over()
            else:
                self.score['col3'] += 1
                if self.ycor < 200:
                    self.score['row1'] += 1
                    self.score['diag2'] += 1
                elif self.ycor < 400:
                    self.score['row2'] += 1
                else:
                    self.score['row3'] += 1
                    self.score['diag1'] += 1
                self.game_over()
            
    #Create a method to update the score for 'O'. Identical to keeping track of the score for 'X',' but the program 
    #checks if 'O' has won by checking if any of the scores are -3, so this method subtracts 1 from the appropriate 
    #values in the dictionary. 
    def o_score(self):
        global score
        if self.score != score:
            self.score = score
            if self.xcor < 200:
                self.score['col1'] -= 1
                if self.ycor < 200:
                    self.score['row1'] -= 1
                    self.score['diag1'] -= 1
                elif self.ycor < 400:
                    self.score['row2'] -= 1
                else:
                    self.score['row3'] -= 1
                    self.score['diag2'] -= 1
                self.game_over()
            elif self.xcor < 400:
                self.score['col2'] -= 1
                if self.ycor < 200:
                    self.score['row1'] -= 1
                elif self.ycor < 400:
                    self.score['row2'] -= 1
                    self.score['diag1'] -= 1
                    self.score['diag2'] -= 1
                else:
                    self.score['row3'] -= 1
                self.game_over()
            else:
                self.score['col3'] -= 1
                if self.ycor < 200:
                    self.score['row1'] -= 1
                    self.score['diag2'] -= 1
                elif self.ycor < 400:
                    self.score['row2'] -= 1
                else:
                    self.score['row3'] -= 1
                    self.score['diag1'] -= 1
                self.game_over()
            
    #Create a method to check if the game is over
    def game_over(self):
        #First, if the turn is less than 9, check the values in the dictionaries. If any of them are 3, that means 'X'
        #has won. If any of the values are -3, that means 'O' has won, and this will create a pop up to congradulate
        #the winner. If all the scores are between -3 and 3, the game will continue uninterrupted.
        if turn < 9:
            if 3 in self.score.values():
                messagebox.showinfo(title="Game Over", message="Condragulations Player 1 You're a Winner Baby")
            if -3 in self.score.values():
                messagebox.showinfo(title="Game Over", message="Condragulations Player 2 You're a Winner Baby")
        #If the turn == 9 that means this is the last turn. The program will check one last time if there is a winner
        #If there is not, it will create a pop up informing the players that it is a tie.
        if turn == 9:
            if 3 in self.score.values():
                messagebox.showinfo(title="Game Over", message="Condragulations Player 1 You're a Winner Baby")
            #The elif statement is unnecessary because 'O' cannot win on turn 9, but it helped me test that the code
            #was functioning properly, so I chose to keep it in for if I want to make any changes to this project later
            elif -3 in self.score.values():
                messagebox.showinfo(title="Game Over", message="Condragulations Player 2 You're a Winner Baby")
            else:
                messagebox.showinfo(title="Game Over", message="Boo It's a Tie")
