from random import randint
from termcolor import colored

win_sets = [{1,2,3},{4,5,6},{7,8,9},{2,5,8},{3,6,9},{1,4,7}]
all_cond = []
def isempty(n):
    if n in board:
        return False
    return True

def printboard():
    j=0
    for i in range(1,10):
        if j==3:
            print("\n")
            j=0
        if i in coordinate_info.keys():
            if coordinate_info[i] == "x":
                print(colored("[x]","cyan"),end=" ")
            else:
                print(colored("[o]","red"),end=" ")
        else:
            print(f"{[i]}", end=" ")
        j += 1
    print()
    print("\n")
def is_winner(coordinate_info,n):
    set_choices = set([i for i in coordinate_info.keys() if coordinate_info[i]==n])
    for win_set in win_sets:
        if win_set.issubset(set_choices):
            printboard()
            if n=="x":
                print("player wins!") 
            else:
                print("computer wins!")
            return True
def computer_choice():
    o_choice = 0
    global coordinate_info
    set_choices = set([i for i in coordinate_info.keys() if coordinate_info[i]=="x"])
    set_o_choices = set([i for i in coordinate_info.keys() if coordinate_info[i]=="o"])
    list_precednce = [sets for sets in win_sets if len(set_choices&sets)!= 0]
    ol = 1
    for i in win_sets:
        if len(i - set_o_choices)==1:
            v = int(*[i for i in set(i - set_o_choices)])
            if not isempty(v):
                ol = 0
                o_choice=v
                break
    if ol:             
        for i in win_sets:
            if len(i - set_choices) == 1 :
                v = int(*[i for i in set(i - set_choices)])
                if not isempty(v):
                    o_choice=v
                    ol = 0
                    break
    if ol:        
        for i in win_sets:
            if len(i - set_choices) == 2 and len((i - set_choices)&set_o_choices)!=0: 
                v = [i for i in set(i - set_o_choices)][1]
                if not isempty(v):
                    o_choice=v
                    ol =0
                    break
    if ol:        
        for i in win_sets:               
            if len(i - set_choices) == 2 :
                v = [i for i in set(i - set_o_choices)][0]
                if not isempty(v):
                    o_choice=v
    # all_condition = [set([i]) for i in set_choices] + all_cond

    if o_choice==0:
        o_choice = randint(1,9)
        while isempty(o_choice):
            o_choice = randint(1,9)
    coordinate_info[o_choice] = "o"
    return o_choice
play = 1  
while play:
    player,computer = "x", "o"
    print("player : x\ncomputer : o" )    
    board = [1,2,3,4,5,6,7,8,9]
    coordinate_info = {}   
    while len(board) != 1:
        x_choice = int(input("please make your move :"))
        while isempty(x_choice):
            x_choice = int(input("please make your move :"))
        coordinate_info[x_choice] = "x"
        if is_winner(coordinate_info,"x"):    
            break
        board.remove(x_choice)
        o_choice = computer_choice()
        if is_winner(coordinate_info,"o"):
            break
        board.remove(o_choice)
        printboard()
        print()
    print()
    answer = input("continue?   (y/n):").lower()
    if answer == "n":
        play = 0 