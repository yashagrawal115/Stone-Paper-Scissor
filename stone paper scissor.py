# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:16:48 2019

@author: YASHA
"""



''' STONE PAPER SCISSOR GAME'''
''' My objective is to have player or gamer(CPU) should have atleast 3 points  
anyone of them to terminate the game, if player wins its +1 to player and if gamer wins -1 to player,
eg: in 7 games they played 4 non concecutive wins 3 lose, points will be -1'''
import random
print("Let's Play the game")
Element_list = ('STONE', 'PAPER', 'SCISSOR')
point = 0 
No_of_game = 0
Game_over = False
while not Game_over:
    if point <3 and point > -3: 
        user_input = input("Enter your part:")
        gamer_input = random.choice(Element_list)
        print("Gamer_input:" , gamer_input)
        if user_input == gamer_input:
            No_of_game += 1
            print("Its a Tie. \nNo one win and poNits are: %d \nNo_of_game %d" %(point,No_of_game))
        elif (user_input == 'PAPER' and gamer_input == 'STONE') or (user_input == 'STONE' and gamer_input == 'SCISSOR') or (user_input == 'SCISSOR' and gamer_input == 'PAPER'):
            point += 1
            No_of_game += 1
            print("You win ....Player!!! \nYour points are : %d \nNo_of_game %d" %(point,No_of_game))
        else:
            No_of_game += 1
            point -=1
            print("You lose ...Player!!! \nYour points are : %d \nNo_of_game %d" %(point,No_of_game))
    # I am looking for the solution below line, I am confused how to apply elif condition in while loop.
    elif (point == 3):
        print("Congratulation you win the game, your point is : %d and you took No_of_game : %d" %(point, No_of_game))
        #end of For loop 
        Game_over = True
        ''' ANY WRONG INPUT OR NO INPUT IS CONSIDERED AS LOSS'''
    elif (point == -3):
        print("SORRY..!! You lose the game, your point is : %d and you took No_of_game : %d" %(point, No_of_game))
        Game_over = True
    else:
        break
            
    
#from tkinter import *
#window=Tk()
#btn=Button(window, text="This is Button widget", fg='blue')
#btn.place(x=80, y=100)
#lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
#lbl.place(x=60, y=50)
#txtfld=Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=80, y=150)
#btnn = Button(window, text= "Learning started", fg = 'green')
#btnn.place(x=90, y= 88)
#window.title('Hello Python')
#window.geometry("300x500+10+10")
#window.mainloop()

    
    
    










