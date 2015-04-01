import random
def number_to_name(number):
    game ={0 :'rock' ,1 :'spork',2 :'paper',3 :'lizaed',4 :'scissors'}   
    return game[number]
def rpsls(player_choice):
    pla = player_choice
    com = random.choice([0,1,2,3,4])
    if pla != 0 and pla != 1 and pla != 2 and pla != 3 and pla != 4 :
        print "Wrong input! \n"
    elif pla == com :
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nDraw!\n"
    elif pla == 0 and ( com == 3 or com == 4):
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Wins!\n"
    elif pla == 1 and ( com == 1 or com == 4):
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Wins!\n"                                                                                      
    elif pla == 2 and ( com == 1 or com == 0):
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Wins!\n" 
    elif pla == 3 and ( com == 1 or com == 2):
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Wins!\n"
    elif pla == 4 and ( com == 2 or com == 3):
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Wins!\n"
    else:
        print "Player chooses "+ number_to_name(pla) + "\nComputer chooses "+ number_to_name(com)+"\nPlayer Loses!\n"
while True:
    player = (int)(raw_input('Please enter the number : \n0 - rock \n1 - Spock \n2 - paper \n3 - lizard \n4 - scissors \n5 -  exit \n') ) 
    if player == 5 :
        break
    else :
        rpsls(player)
