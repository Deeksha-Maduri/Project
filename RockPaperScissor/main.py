from tkinter import *
import random as r
from PIL import ImageTk,Image
# Create the main window
root=Tk()
root.title("Rock Paper Scissors")
# Create and pack the title label
Label(root,text="ROCK PAPER SCISSORS",font=("times roman","16","bold")).pack()
# Load and display the main image
rock_paper_scissors=ImageTk.PhotoImage(Image.open('/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/logo.JPG'))
l=Label(image=rock_paper_scissors)
l.pack()
# Load other image assets
rock=ImageTk.PhotoImage(Image.open("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/rock.jpg"))
paper=ImageTk.PhotoImage(Image.open("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/paper.jpg"))
scissors=ImageTk.PhotoImage(Image.open("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/scissor.jpg"))
rock_tie=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/rock-rock.jpg")))
rock_paper=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/rock-paper.jpg")))
rock_scissors=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/rock-scissor.jpg")))
paper_tie=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/paper-paper.jpg")))
paper_rock=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/paper-rock.jpg")))
paper_scissors=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/paper-scissor.jpg")))
scissors_tie=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/scissor-scissor.jpg")))
scissors_rock=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/scissor-rock.jpg")))
scissors_paper=ImageTk.PhotoImage(Image.open(("/Users/deekshamaduri/Documents/Projects/RockPaperScissor/RPS/scissor-paper.jpg")))
def game():
    e=["ROCK","PAPER","SCISSORS"]

    # Sub-function for when user chooses ROCK
    def z():
        m=r.choice(e)
        if m=="ROCK":
            x = LabelFrame(root, text="")
            x.pack()
            f=Label(x,image=rock_tie)
            f.grid(row=0,column=0)
            Label(x, text=f" ROCK Vs {m}",font=("times roman", "14", "bold")).grid(row=1)
            Label(x,text=f"DRAW MATCH",font=("times roman","10","bold")).grid(row=2)
        elif m=="SCISSORS":
            x = LabelFrame(root, text="")
            x.pack()
            g=Label(x,image=rock_scissors)
            g.grid(row=0,column=0)
            Label(x, text=f" ROCK Vs {m}",font=("times roman", "14", "bold")).grid(row=1)
            Label(x,text=f"YOU WON THE MATCH ",font=("times roman","10","bold")).grid(row=2)
        else:
            x=LabelFrame(root,text="")
            x.pack()
            h=Label(x,image=rock_paper)
            h.grid(row=0,column=0)
            Label(x, text=f" ROCK Vs  {m}",font=("times roman", "14", "bold")).grid(row=1)
            Label(x,text=f"YOU LOST THE MATCH ",font=("times roman","10","bold")).grid(row=2)

    # Sub-function for when user chooses SCISSORS
    def y():
        # Define the main game function
        m=r.choice(e)
        if m=="SCISSORS":
            f=Label(image=scissors_tie)
            f.pack()
            Label(root, text=f" SCISSORS  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root,text=f"DRAW MATCH ",font=("times roman","10","bold")).pack()
        elif m=="PAPER":
            g=Label(image=scissors_paper)
            g.pack()
            Label(root, text=f" SCISSORS  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root,text=f"YOU WON THE MATCH",font=("times roman","10","bold")).pack()
        else:
            h=Label(image=scissors_rock)
            h.pack()
            Label(root, text=f" SCISSORS  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root,text=f"YOU LOST THE MATCH",font=("times roman","10","bold")).pack()
    # Sub-function for when user chooses PAPER
    def x():
        m = r.choice(e)
        if m == "PAPER":
            f=Label(image=paper_tie)
            f.pack()
            Label(root, text=f" PAPER  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root, text=f"DRAW MATCH",font=("times roman","10","bold")).pack()
        elif m == "ROCK":
            g=Label(image=paper_rock)
            g.pack()
            Label(root, text=f" PAPER  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root, text=f"YOU WON THE MATCH",font=("times roman","10","bold")).pack()
        else:
            h=Label(image=paper_scissors)
            h.pack()
            Label(root, text=f" PAPER  Vs  {m}",font=("times roman", "14", "bold")).pack()
            Label(root, text=f"YOU LOST THE MATCH",font=("times roman","10","bold")).pack()
    c=LabelFrame(root,text="")
    c.pack()
    Button(c,image=rock,command=z).grid(row=0,column=0)
    Label(c,text="").grid(row=0,column=1)
    Label(c, text="").grid(row=0, column=2)
    Label(c, text="").grid(row=0, column=3)
    Label(c, text="").grid(row=0, column=4)
    Button(c, image=scissors,command=y).grid(row=0,column=5)
    Label(c, text="").grid(row=0, column=6)
    Label(c, text="").grid(row=0, column=7)
    Label(c, text="").grid(row=0, column=8)
    Label(c, text="").grid(row=0, column=9)
    Button(c, image=paper,command=x).grid(row=0,column=10)
# Create the "click here" button to start the game
Button(root,text="click here",font=("times roman","8","bold"),command=game).pack()
# Start the main event loop
root.mainloop()
