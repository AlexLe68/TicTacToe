import random
from re import X
import time

game = True
#function for printing grid
def grid(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print("   1     2     3 ")
    print("a ",a1," | ",a2," | ",a3)
    print(" -----------------")
    print("b ",b1," | ",b2," | ",b3)
    print(" -----------------")
    print("c ",c1," | ",c2," | ",c3)
    
#function to randomize computer's position
def randomize():
    global pos,a
    a = random.randint(1,9)
    if a == 1:
        pos = 'a1'
    elif a == 2:
        pos = 'a2'
    elif a == 3:
        pos = 'a3'
    elif a == 4:
        pos = 'b1'
    elif a == 5:
        pos = 'b2'
    elif a == 6:
        pos = 'b3'
    elif a == 7:
        pos = 'c1'
    elif a == 8:
        pos = 'c2'
    elif a == 9:
        pos = 'c3'
#function for each move
def move(i,user_or_computer):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,pos,b
    if user_or_computer == 'computer':
        randomize()
    while True:
        if pos == "a1" and (a1 !=xo and a1 != ox):
            a1 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "a2" and (a2 !=xo and a2 != ox):
            a2 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "a3" and (a3 !=xo and a3 != ox):
            a3 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "b1" and (b1 !=xo and b1 != ox):
            b1 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "b2" and (b2 !=xo and b2 != ox):
            b2 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "b3" and (b3 !=xo and b3 != ox):
            b3 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "c1" and (c1 !=xo and c1 != ox):
            c1 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "c2" and (c2 !=xo and c2 != ox):
            c2 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        elif pos == "c3" and (c3 !=xo and c3 != ox):
            c3 = i
            grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
            b = True
            break
        else:
            if user_or_computer == 'user':
                pos = input("That position is occupied ")
                b=False
            else: 
                randomize()
                b=False
            
#function to check if victory
def if_win():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,win
    if (a1 == a2 == a3 == xo) or (a1 == b1 == c1 == xo) or (a1 == b2 == c3 == xo) or (a2 == b2 == c2 == xo) or (a3 == b3 == c3 == xo) or (a3 == b2 == c1 == xo) or (b1 == b2 == b3 == xo) or (c1 == c2 == c3 == xo):
        print("You win! ")
        win = True
        return 0
    elif (a1 == a2 == a3 == ox) or (a1 == b1 == c1 == ox) or (a1 == b2 == c3 == ox) or (a2 == b2 == c2 == ox) or (a3 == b3 == c3 == ox) or (a3 == b2 == c1 == ox) or (b1 == b2 == b3 == ox) or (c1 == c2 == c3 == ox):
        print("I win! ")
        win = True
        return 0
    else:
        win = False

#function to check if it is tied
def if_tie():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,win
    if win == False and (a1 == xo or a1 == ox) and (a2 == xo or a2 == ox) and (a3 == xo or a3 == ox) and (b1 == xo or b1 == ox) and (b2 == xo or b2 == ox) and (b3 == xo or b3 == ox) and (c1 == xo or c1 == ox) and (c2 == xo or c2 == ox) and (c3 == xo or c3 == ox):
        print("It is a tie. ")
        win = True
#function to play when it is user's turn
def user_turn():
    global pos,win
    pos = ' '
    while pos != 'a1' and pos != 'a2' and pos != 'a3' and pos != 'b1' and pos != 'b2' and pos != 'b3' and pos != 'c1' and pos != 'c2' and pos != 'c3':
        pos = input("Choose a position (example: a1, b2, c3...) ")
    move(xo,'user') 
    if_win()
    if_tie()
    if win==True:
        return 0

#function to play when it is computer's turn
def computer_turn():
    global pos,win
    move(ox,'computer')
    while b == False:
        move(ox,'computer')
    if_win()
    if_tie()
    if win ==True:
        return 0

#GAME
while game == True:
    xo =' '
    a1=a2=a3=b1=b2=b3=c1=c2=c3=' '
    pos = ' '
    b = win = False
    a=0
    yn =''
    grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)
    while xo.upper() != 'X' and xo.upper() != 'O':
        xo = input("Choose X or O ").upper()
    if xo.upper() == 'X':
        ox = 'O'
    else:
        ox = 'X'
    print('So you are',xo)
    time.sleep(1)
    if xo =='X':
        print("You go first since you are X")
        time.sleep(2)
    else:
        print("I go first since I am X")
        time.sleep(2)
    while win==False:
        if xo == 'X':
            user_turn()
            if win == True:
                time.sleep(1)
                break
            time.sleep(2)
            computer_turn()
        else:
            computer_turn()
            if win == True:
                time.sleep(1)
                break
            user_turn()
            time.sleep(2)
    while yn != 'yes' and yn != 'no' and yn != 'ye' and yn != 'nah' and yn != 'sure' and yn != 'nope':
        yn=input("Do you want to play again? ").lower()
        if yn == 'yes' or yn == 'ye' or yn == 'sure':
            game = True
        else:
            game = False
            print("Thanks for playing. ")