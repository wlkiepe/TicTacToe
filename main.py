# This is my second attempt at the project, I deleted the first one because I had a cumbersome amount of code
# The original draft had hundreds of lines of code, most of which I realized were redundant, after brainstorming with
# friend I realized I could remove most of that code by creating my own class MyButton

# Import the tools I will need
from tkinter import *
from Classes import MyButton

# Set up my window for my GUI, finding some colors that I think will look good
background = '#84D2C5'
window = Tk()
window.title("Tic Tac Toe")
window.wm_minsize(width=600, height=600)
window.config(bg=background)

# Create a canvas and create lines on that canvas to make the board
canvas = Canvas(width=500, height=400, highlightthickness=0, bg=background)
title = Label(text="Tic Tac Toe", highlightthickness=0, bg=background, font=('Arial', 32, "bold"))

canvas.create_line(200, 50, 200, 600)
canvas.create_line(360, 50, 360, 600)
canvas.create_line(50, 170, 800, 170)
canvas.create_line(50, 300, 800, 300)

# Create 9 MyButtons on the board to use for playing the game.
button1 = MyButton(150, 150)
button1.place()

button2 = MyButton(290, 150)
button2.place()

button3 = MyButton(450, 150)
button3.place()

button4 = MyButton(150, 270)
button4.place()

button5 = MyButton(290, 270)
button5.place()

button6 = MyButton(450, 270)
button6.place()

button7 = MyButton(150, 400)
button7.place()

button8 = MyButton(290, 400)
button8.place()

button9 = MyButton(450, 400)
button9.place()

# I have a habit of doing .place() at the end of the code. I am not sure if that is standard practice or not, but it
# helps me find it easier if I need to change the placement of anything as I edit code
canvas.place(x=40, y=40)
title.place(x=200, y=0)

window.mainloop()

# Possible future goal for this project:
# Automate the game so that the user could play a single player game against the computer.
# Steps to take - create a prompt asking the user if they are playing single player or multiplayer, if single player
# prompt the user if they want to be X's or O's. Then create a program that will allow the computer to select buttons.
# Ideally the computer would have some strategy to it, but I may make it choose random buttons at first.
