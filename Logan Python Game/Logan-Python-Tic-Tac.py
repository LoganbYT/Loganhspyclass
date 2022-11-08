import random
import logging
from datetime import datetime
Board = {'1': "#", '2': "#", '3': "#", '4': "#", '5': "#", '6': "#", '7': "#", '8': "#", '9': "#"}
Player = random.choice(["o","x"])
PlaceTimes = 0
GameOver = False
Winner
def Switch():
    global Player
    if Player == "x":
        Player = "o"
    else:
        Player = "x"
def Print():
    print(Board["1"], Board["2"], Board["3"])
    print(Board["4"], Board["5"], Board["6"])
    print(Board["7"], Board["8"], Board["9"])
def Check():
    global Player
    global PlaceTimes
    for x in range(2):
        A = Board.get("1")
        B = Board.get("2")
        C = Board.get("3")
        D = Board.get("4")
        E = Board.get("5")
        F = Board.get("6")
        G = Board.get("7")
        H = Board.get("8")
        I = Board.get("9")
        if A == Player and B == Player and C == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
        if D == Player and E == Player and F == Player:
            PlaceTimes = 9
            Winner = Player
            print(f"Winner {Player}")
            break
        if G == Player and H == Player and I == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            break
        if A == Player and D == Player and G == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            break
        if B == Player and E == Player and H == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            break
        if C == Player and F == Player and I == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
        if A == Player and D == Player and G == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
        if B == Player and E == Player and H == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
        if C == Player and F == Player and I == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
        if A == Player and E == Player and I == Player:
            PlaceTimes = 9
            Winner = Player
            print(f"Winner {Player}")
            
            break
        if G == Player and E == Player and C == Player:
            PlaceTimes = 9
            print(f"Winner {Player}")
            Winner = Player
            break
Print()
while PlaceTimes != 9:
    print(f'Enter a number 1-9 on the board player ({Player})')
    PlayerInput = input('Enter: ')
    if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1","2","3","4","5","6","7","8","9"]:
        Board[PlayerInput] = Player
        PlaceTimes += 1
        print(PlaceTimes)
        Print()
        Check()
        Switch()            
    else:
        while True:
            print(f'Enter a number 1-9 on the board player ({Player})')
            PlayerInput = input('Enter: ')
            if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1","2","3","4","5","6","7","8","9"]:
                Board[PlayerInput] = Player
                PlaceTimes += 1
                print(PlaceTimes)
                Print()
                Check()
                Switch()
                break
print(f"Congratulations Winner, Run the script again to play again!")

open("Winners.txt", "a+") as f:
date = datetime.now().strftime("%Y-%m-%d %H:%:M")
f.write(f"\n")
f.write(f"{date} Winner {Winner}")
f.close()

    

    
