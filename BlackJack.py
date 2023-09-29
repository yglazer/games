#Yocheved Glazer
#1/7/2023

import random#to draw card



#who won?
def winner(user):
    computer=comp()#do computers turns now

    if computer> 21 and user>21:
        print("No winner. Both player and user have a hand over 21.")
    elif computer>21 and user<21:
        print("User Won!")
    elif computer<21 and user>21:
        print("Computer Won!")
    elif computer>user:
        print("Computer Won!")
    elif user>computer:
        print("User Won!")
    elif user==computer:
        print("User and Computer tied! Please play again.")


#menu
def menu():
    print("MENU\n1.Freeze my hand\n2.I want to pick another card\n3.I quit")
    choice=int(input("Select the desired action by pressing the number and enter."))
    while choice  != 1 and choice !=2 and choice  !=3:
        print("Invalid option. Please try again.")#input validation
        choice=int(input("Select the desired action by pressing the number and enter."))
    return choice #return choice from menu

#draw a new card     for user and computer
def draw():
    value=0
    cardname=''
    suit=0
    cardnumber=random.randint(1,13)
    if cardnumber==1:
        value=1
        cardname='Ace'
    elif cardnumber==2:
        value=2
        cardname='Two'
    elif cardnumber==3:
        value=3
        cardname='Three'
    elif cardnumber==4:
        value=4
        cardname='Four'
    elif cardnumber==5:
        value=5
        cardname='Five'
    elif cardnumber==6:
        value=6
        cardname='Six'
    elif cardnumber==7:
        value=7
        cardname='Seven'
    elif cardnumber==8:
        value=8
        cardname='Eight'
    elif cardnumber==9:
        value=9
        cardname='Nine'
    elif cardnumber==10:
        value=10
        cardname='Ten'
    elif cardnumber==11:
        value=10
        cardname='Jack'
    elif cardnumber==12:
        value=10
        cardname='Queen'
    else:
        value=10
        cardname='King'

    
    #suit
    cardsuit=random.randint(1,4)
    if cardsuit==1:
        suit='Hearts'
    elif cardsuit==2:
        suit='Clubs'
    elif cardsuit==3:
        suit="Spades"
    else:
        suit='Diamonds'

    fullcardname=cardname+' of '+suit
    
    print("The card drawn is a",fullcardname)
   
    return value


def comp():
    print("Computer's Turn")
    print('===============')
    value=draw()
    while value<15:
        value+=draw()
    
    print(value,'Computers hand')
    return value
    
def main():
    #Explanation of the game
    print('This is a card game. The object of the game is to get as close to 21 without going over.')
    again='y'

    while again.lower()=='y':
        input('Press enter to draw a card')#first card
        value=draw()
        print('Your hand value is',value)
        choice=menu()
        while choice ==2:#additional cards
        
            value+=draw()
            print('Your hand value is',value)
            choice=menu()
        if choice==1:
            winner(value)
            again=input('Do you want to play again?(y/n)')
        else:
            print('bye!')
        
        
        
main()
    
    
        
    
        
        
