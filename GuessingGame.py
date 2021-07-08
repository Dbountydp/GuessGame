#!/usr/bin/python3

import random

welcome = """
              |-------------------------------|
              |        Guesing Game           | 
              |-------------------------------|                  
    """
print(welcome)

player = int(input(" how many player you want to play: "))



def Guesing_Game(player):
    print(
        f"hello {player.title()} \nwelcome to the Game \nhere you have 3 chance \nbest of luck \n")
    chance = 3
    score = 0
    i = 0
    while i < chance:
        guess_ = int(input(" Guess you Number between 1 to 10 : "))
        print()
        num = random.randint(0, 10)
        i += 1
        if guess_ is num:
            print("\n<------yeah you guess right: ---->")
            score = score+1
            print(f"you got one more point now your score is {score}\n")

        else:
            print("\n<---- better luck next time----->")

            print(f"you lost your chance {i}\n")
    return score


def players(player):
    win = []
    playersNameLst = []
    for name in range(player):
        playerName = input(" hey what's your name: ")
        # appending player name in list so we can find winner in end
        playersNameLst.append(playerName)

        score = Guesing_Game(playerName)
        win.append(score)
    
    #find max score index
    if any(win)==False:
        print(" \n<------No one Win------>\n ")
    
    
    else:
        m = max(win)
        winIndex = win.index(m)
        return playersNameLst[winIndex]


winner = players(player)
if winner == None:
    pass
else:

    logo = f"""
                |--------------------------------------------|
                |        We got our winner {winner}          | 
                |--------------------------------------------|                  
        """
    print(logo)




        