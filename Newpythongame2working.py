import random

Board = {'1': "0", '2': "0", '3': "0", '4': "0", '5': "0", '6': "0", '7': "0", '8': "0", '9': "0"}

def Print():
    print(Board["1"], Board["2"], Board["3"])
    print(Board["4"], Board["5"], Board["6"])
    print(Board["7"], Board["8"], Board["9"])

PlaceTimes = 0
while PlaceTimes != 9:
    PlayerInput = input("enter num 1-9 (o):")
    if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        Board[PlayerInput] = "x"
        Print()
    else:
        while Board.get(PlayerInput) == "x" or Board.get(PlayerInput) == "o" or PlayerInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            PlayerInput = input("enter num 1-9(o):")
            if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                Board[PlayerInput] = "x"
                PlaceTimes + 1
                Print()
                break
            break

    PlayerInput = input("enter num 1-9 (o):")
    if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        Board[PlayerInput] = "o"
        Print()
    else:
        while Board.get(PlayerInput) == "x" or Board.get(PlayerInput) == "o" or PlayerInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            PlayerInput = input("enter num 1-9(o):")
            if Board.get(PlayerInput)!= "x" and Board.get(PlayerInput) != "o" and PlayerInput in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                Board[PlayerInput] = "o"
                PlaceTimes + 1
                Print()
                break
            break

    

    
