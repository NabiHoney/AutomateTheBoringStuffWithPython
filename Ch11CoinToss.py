import random
import pyinputplus as pyip

toss = []
choice = []

def chyuz():
    hort = pyip.inputMenu(['heads', 'tails'], numbered=True)
    choice.append(hort)  
    print(choice)
    

def air():
    flip = random.randint(0, 1)
    if flip == 0:
        toss.append('heads')   
    else:
        toss.append('tails')
    print(toss)
    
def comp():
    if toss == choice:
        print('You guessed it!')
    else:
        print('Sorry, try again!')
    

chyuz()
air()
comp()
