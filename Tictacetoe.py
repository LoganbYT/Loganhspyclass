import random
import keyboard

GameOver = False
CorrectTac = 0
TacOrTic = 1
Turn = random.uniform(0,1)
CountToTry = 0
PlayerInput = 0
Board = {'1':0, '2':0,'3':0, '4':0, '5':0,'6':0,'7':0,'8':0,'9':0}
CharacterCheck = "x"
Winner = "x"
ActualCheck = 0

print("enter P to start")
while GameOver == False:
    if keyboard.is_pressed("p"):
        if Turn == 1:       
            Board[input("enter your choice as a number:")][1] == "x"
            Check()
            if CorrectTac == 3:
                Turn = 2
        if Turn == 1:       
            Board[input("enter your choice as a number:")][1] == "o"
            Check()
            if CorrectTac == 3:
                Turn = 1


    def Check():
        while ActualCheck != 2:
            while CountToTry >= 4:
                if Board[A] & Board[B] & Board[C] == CharacterCheck:
                    A+3
                    B+3
                    C+3 
                    CorrectTac+1  
                    CountToTry+1 
            else:
                A=1
                B=4
                C=7 
            while CountToTry >= 7:
                if Board[A] & Board[B] & Board[C] == CharacterCheck:
                    A+1
                    B+1
                    C+1
                    CorrectTac+1
                    CountToTry+1
                else:
                    A=1
                    B=5
                    C=9
                    if CountToTry >= 8:
                        if Board[A] & Board[B] & Board[C] == CharacterCheck:
                        GameOver = True
                    else:
                        A=3
                        B=5
                        C=7
                    if CountToTry >= 9:
                        if Board[A] & Board[B] & Board[C] == CharacterCheck:
                            GameOver = True
                            CountToTrys += 1
                        else:
                            ActualCheck + 1
                            CharacterCheck = "o"
                            CountToTry = 0 

                            


                            



        
    
        
    

        

              
                


    


    

    
