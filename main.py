print('''

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████──────────██████─██████████████────██████████████████─██████████████─██████──────────██████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████────████████████░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██────────────────────████░░████─██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────
─██░░██─────────██░░██████░░██─██░░██──██░░██──██░░██─██░░██████████──────────████░░████───██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████████─
─██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██────────████░░████─────██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████░░██─██░░██──██████──██░░██─██░░██████████──────████░░████───────██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██────────────████░░████─────────██░░██──██░░██─██░░██──██░░██████░░██─██░░██─────────
─██░░██████░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██████████────██░░░░████████████─██░░██████░░██─██░░██──██░░░░░░░░░░██─██░░██████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░██──────────██░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─██████──────────██████─██████████████────██████████████████─██████████████─██████──────────██████─██████████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
''')
print("Welcome to the GameZone")
print("We have two games for you!!!!")
print('''
1)Team 11
2)TicTacToe
3)Exit''')
gn=int(input("Enter serial number of the game you want to play:"))

while gn not in range(1,4):
    gn=int(input("Please enter serial number from 1 to 3"))

while gn!=3:
    if gn==1:
        import random
        class Team:
            def __init__(self):
                self.lop=[]
                print("Select six Batsmen for your team")
                for i in range(6):
                    print("Enter name of batsman "+str(i+1)+":", end="")
                    x=Batsman()
                    self.lop.append(x)

                print("")
                print("Select three Bowlers for your team")
                for i in range(3):
                    print("Enter name of bowler "+str(i+1)+":", end="")
                    x=Bowler()
                    self.lop.append(x)
                print("")
                print("Select two Allrounders for your team")
                for i in range(2):
                    print("Enter name of allrounder "+str(i+1)+":", end="")
                    x=Allrounder()
                    self.lop.append(x)
                print("")

        class Batsman:

            def __init__(self):
                name=input()
                self.name=name
                self.runs=0
                self.sixes=0

            def runsScored(self):
                self.runs=int((random.randint(0,70)))
                return self.runs

            def sixesHit(self):
                self.sixes=int((random.randint(0,10)))
                return self.sixes

        class Bowler:

            def __init__(self):
                name=input()
                self.name=name
                self.wickets=0
                self.economy=0

            def wicketsTaken(self):
                self.wickets=int((random.randint(0,6)))
                return self.wickets

            def spelleconomy(self):
                self.economy=10*(random.random())
                return self.economy

        class Allrounder:

            def __init__(self):
                name=input()
                self.name=name
                self.runs=0
                self.sixes=0
                self.wickets=0
                self.economy=0

            def runsScored(self):
                self.runs=int((random.randint(0,50)))
                return self.runs

            def sixesHit(self):
                self.sixes=int((random.randint(0,10)))
                return (self.sixes)

            def wicketsTaken(self):
                self.wickets=int((random.randint(0,4)))
                return self.wickets

            def spelleconomy(self):
                self.economy=10*(random.random())
                return self.economy

        d={}
        #KKR
        d["KKR"]="Shubman Gill, Matthew Wade (WK), Sai Sudharsan, Hardik Pandya (C), David Miller, Rahul Tewatia, Abhinav Manohar, Rashid Khan, Lockie Ferguson, Mohammed Shami, Darshan Nalkande"
        #srh
        d["SRH"]="Abhishek Sharma, Kane Williamson (C), Rahul Tripathi, Aiden Markram, Nicholas Pooran, Shashank Singh, Washington Sundar, Bhuvneshwar Kumar, Marco Jansen, T Natarajan, Umran Malik/Kartik Tyagi"
        #rajasthan
        d["RR"]='Jos Buttler, Devdutt Padikkal, Sanju Samson (c & wk), Rassie van der Dussen, Shimron Hetmyer, Riyan Parag, Kuldeep Sen, Ravichandran Ashwin, Trent Boult, Prasidh Krishna, Yuzvendra Chahal'
        #lsg
        d["LSG"]='KL Rahul (c), Quinton de Kock (wk), Marcus Stoinis, Deepak Hooda, Ayush Badoni, Krunal Pandya, Jason Holder, Krishnappa Gowtham, Dushmantha Chameera, Ravi Bishnoi, Avesh Khan'

        lotm=["KKR","SRH","RR","LSG"]
        i1=random.randint(0,3)
        i2=random.randint(0,3)
        while i2==i1:
            i2=random.randint(0,3)
        pltm=[lotm[i1], lotm[i2]]

        class User:

            def __init__(self):
                name=input("Enter your name:")
                print("")
                self.name = name
                self.fpts=0
                
            def teamselect(self):
                global d
                global pltm

                print("Today is the match between "+pltm[0]+" and "+pltm[1])
                print("")
                print("The team for "+pltm[0])
                print("")
                print(d[pltm[0]])
                print("")
                print("The team for "+pltm[1])
                print("")
                print(d[pltm[1]])
                print("")
                print("Now it is time to select your 11 from these 22 players, choose wisely !!")
                print("")
                self.userteam=Team()
                
                l=[i.name for i in self.userteam.lop]
                print("Here is the team that you selected")
                for i in l:
                    print(i, end=" ")
                print("")

            def aftermatch(self):
                x=self.userteam.lop
                xlist=[i.name for i in x]
                
                for i in range(6):
                    x[i].runsScored()
                    x[i].sixesHit()
                for i in range(3):
                    x[i+6].wicketsTaken()
                    x[i+6].spelleconomy()
                for i in range(2):
                    x[i+9].runsScored()
                    x[i+9].sixesHit()
                    x[i+9].wicketsTaken()
                    x[i+9].spelleconomy()
            
            def finalpoints(self):
                
                x=self.userteam.lop
                finalpoints=0
                for i in range(6):
                    if x[i].runs in range(0,10):
                        finalpoints+=1
                    elif x[i].runs in range(10,30):
                        finalpoints+=2
                    elif x[i].runs in range(30,70):
                        finalpoints+=3
                    elif x[i].runs in range(70,100):
                        finalpoints+=4
                    else:
                        finalpoints+=5
                    
                    if x[i].sixes in range(0,1):
                        finalpoints+=1
                    elif x[i].sixes in range(1,3):
                        finalpoints+=2
                    elif x[i].sixes in range(3,7):
                        finalpoints+=3
                    else:
                        finalpoints+=4
                
                for i in range(3):
                    if x[i+6].wickets in range(0,1):
                        finalpoints+=1
                    elif x[i+6].wickets in range(1,2):
                        finalpoints+=2
                    elif x[i+6].wickets in range(2,3):
                        finalpoints+=3
                    elif x[i+6].wickets in range(3,5):
                        finalpoints+=4
                    else:
                        finalpoints+=5
                    if x[i+6].economy in range(15,99):
                        finalpoints+=1
                    elif x[i+6].economy in range(8,15):
                        finalpoints+=2
                    elif x[i+6].economy in range(5,8):
                        finalpoints+=3
                    elif x[i+6].economy in range(1,5):
                        finalpoints+=4
                    else:
                        finalpoints+=5
                        
                for i in range(2):
                    if x[i+9].runs in range(0,10):
                        finalpoints+=1
                    elif x[i+9].runs in range(10,30):
                        finalpoints+=2
                    elif x[i+9].runs in range(30,70):
                        finalpoints+=3
                    elif x[i+9].runs in range(70,100):
                        finalpoints+=4
                    else:
                        finalpoints+=5
                    if x[i].sixes in range(0,1):
                        finalpoints+=1
                    elif x[i].sixes in range(1,3):
                        finalpoints+=2
                    elif x[i].sixes in range(3,7):
                        finalpoints+=3
                    else:
                        finalpoints+=4
                    
                    if x[i+9].wickets in range(0,1):
                        finalpoints+=1
                    elif x[i+9].wickets in range(1,2):
                        finalpoints+=2
                    elif x[i+9].wickets in range(2,3):
                        finalpoints+=3
                    elif x[i+9].wickets in range(3,5):
                        finalpoints+=4
                    else:
                        finalpoints+=5

                self.fpts=finalpoints    
                return finalpoints

            def bestPicks(self):
                x=self.userteam.lop

                btsmnlst=x[:6]
                bwlrlst=x[6:9]
                alrndrlst=x[9:]

                mxrun=0
                for i in btsmnlst:
                    if i.runs>mxrun:
                        mxrun=i.runs
                        btsmn=i.name

                print("Best Batsman is "+btsmn+" with "+str(mxrun)+" runs.")
                print("")

                mxwckt=0
                for i in bwlrlst:
                    if i.wickets>mxwckt:
                        mxwckt=i.wickets
                        bwlr=i.name

                print("Best Bowler is "+bwlr+" with "+str(mxwckt)+" wickets.")
                print("")

                mxrnw=0
                hrun=0
                hwckts=0
                for i in alrndrlst:
                    if i.runs+20*(i.wickets)>mxrnw:
                        alrndr=i.name
                        hrun=i.runs
                        hwckts=i.wickets

                print("Best Allrounder is "+alrndr+" with "+str(hwckts)+" wickets and "+str(hrun)+" runs.")
                

        print('''                   
                                ██████                  
                            ██████████                
        ████                  ██████████                
        ██████                ██████████                
        ██████                ██████    ████          
            ██████                      ██████          
            ██████                  ████████          
                ██████              ████████            
                ██████          ████████              
                    ████      ████████                  
                        ██████████                      
                        ██                ████        
                            ██            ████████      
                                ████    ████████      
                                ██████  ████████      
                                ██████  ████████      
            ██████            ████████    ██████      
            ██  ██  ██          ██████      ██████      
            ██  ██  ██        ██████        ████████    
            ██  ██  ██        ██████          ██████    
            ██  ██  ██        ████              ████    
            ██  ██  ██        ████              ██████  
            ██  ██  ██        ██                  ████  
            ██  ██  ██      ████                  ████  
            ██  ██  ██      ████                    ████
            ██  ██  ██      ██                        ██
            ██  ██  ██      ██                        ██
        ''')
        print('''
                    ╭━━━━┳━━━┳━━━┳━╮╭━╮╱╭╮╱╭╮
                    ┃╭╮╭╮┃╭━━┫╭━╮┃┃╰╯┃┃╭╯┃╭╯┃
                    ╰╯┃┃╰┫╰━━┫┃╱┃┃╭╮╭╮┃╰╮┃╰╮┃
                    ╱╱┃┃╱┃╭━━┫╰━╯┃┃┃┃┃┃╱┃┃╱┃┃
                    ╱╱┃┃╱┃╰━━┫╭━╮┃┃┃┃┃┃╭╯╰┳╯╰╮
                    ╱╱╰╯╱╰━━━┻╯╱╰┻╯╰╯╰╯╰━━┻━━╯
        ''')

        print("-"*62)
        print("|                     WELCOME TO TEAM 11                     |")
        print("-"*62)
        print("")
        print("Welcome user")
        a=User()
        a.teamselect()
        a.aftermatch()
        print("")
        print("The match has started, enjoy !!")
        print("")
        print("So the match has ended and your final points are "+str(a.finalpoints()))
        print("")
        print("And here is a glimpse of your best picks")
        print("")
        a.bestPicks()
        print("Hope you enjoyed")

    elif gn==2:
        import random
        class board:
            def __init__(self):
                self.row1=["-","-","-"]
                self.row2=["-","-","-"]
                self.row3=["-","-","-"]

            def printboard(self):
                print(*self.row1)
                print(*self.row2)
                print(*self.row3)

            def move(self,n,s):
                if n in range(1,4):
                    self.row1[n-1]=s

                elif n in range(4,7):
                    self.row2[n-4]=s

                elif n in range(7,10):
                    self.row3[n-7]=s

                print("")
                self.printboard()

            def wino(self):
                a=bool(self.row1==["o","o","o"] or self.row2==["o","o","o"] or self.row3==["o","o","o"])
                b=bool(self.row1[0]==self.row2[0]==self.row3[0]=="o" or self.row1[1]==self.row2[1]==self.row3[1]=="o" or self.row1[2]==self.row2[2]==self.row3[2]=="o")
                c=bool(self.row1[0]==self.row2[1]==self.row3[2]=="o" or self.row1[2]==self.row2[1]==self.row3[0]=="o")

                return (a or b or c)

            def winx(self):
                a=bool(self.row1==["x","x","x"] or self.row2==["x","x","x"] or self.row3==["x","x","x"])
                b=bool(self.row1[0]==self.row2[0]==self.row3[0]=="x" or self.row1[1]==self.row2[1]==self.row3[1]=="x" or self.row1[2]==self.row2[2]==self.row3[2]=="x")
                c=bool(self.row1[0]==self.row2[1]==self.row3[2]=="x" or self.row1[2]==self.row2[1]==self.row3[0]=="x")
                
                return (a or b or c)

            def newgame(self):
                self.row1=["-","-","-"]
                self.row2=["-","-","-"]
                self.row3=["-","-","-"]


        class Player:
            def __init__(self,name,tot):
                self.name=name
                self.tot=tot
                self.score=0

            def won(self):
                self.score+=1

        print('''

        ████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
        ╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
        ░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
        ░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
        ░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
        ░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝
        ''')
        print("")
        print("Welcome to tic tac toe")
        print("Here is the board")
        print("")
        b=board()
        b.printboard()
        print("")
        nop=int(input("Enter number of players:"))
        while nop not in range(1,3):
            nop=int(input("Players can be 1 or 2"))
        
        if nop==2:
            print("")
            l=["x","o"]

            lop=[]
            name=input("Enter name of player 1:")
            tot=input("What would you select o or x ? Enter:")
            while tot not in l:
                tot=input("Enter only o or x:")
            l.remove(tot)
            p1=Player(name,tot)
            lop.append(p1)

            name=input("Enter name of player 2:")
            print("Player 2 you have to take "+l[0])
            tot=l[0]
            p2=Player(name,tot)
            lop.append(p2)

            flop=[]
            for i in lop:
                if i.tot=="x":
                    flop.append(i)
                    lop.remove(i)
            flop.append(lop[0])

            print("")
            print("All set, lets go!!!")
            print("")
            b.printboard()
            print("")
            cplcs=[]
            flag=True
            for i in range(1,10):
                if i%2!=0:
                    print(flop[0].name+" enter integer corresponding where you want place x :", end="")
                    n=int(input())
                    while n in cplcs:
                        n=int(input("Enter value which is not already covered:"))

                    while n not in range(1,10):
                        n=int(input("Please enter value from 1 to 9 :"))

                    cplcs.append(n)
                    s="x"
                    b.move(n,s)
                    print("")
                    if b.winx()==True:
                        print("Congrats!!! "+flop[0].name+" you won")
                        flop[0].won()
                        flag=False
                        break
                
                else:
                    print(flop[1].name+" enter integer corresponding where you want place o :", end="")
                    n=int(input())
                    while n in cplcs:
                        n=int(input("Enter value which is not already covered:"))

                    while n not in range(1,10):
                        n=int(input("Please enter value from 1 to 9 :"))

                    cplcs.append(n)
                    s="o"
                    b.move(n,s)
                    print("")
                    if b.wino()==True:
                        print("Congrats!!! "+flop[1].name+" you won")
                        flop[1].won()
                        flag=False
                        break
            if flag==True:
                print("The game was a Draw")
            print("")
            print("Do you guys wish to play a new game ?")
            ng=input("Enter Y/N :")
            print("")

            while ng!="N":
                b.newgame()
                print("Here is the fresh board")
                b.printboard()
                cplcs.clear()
                flag=True
                for i in range(1,10):
                    if i%2!=0:
                        print(flop[0].name+" enter integer corresponding where you want place x :", end="")
                        n=int(input())
                        while n in cplcs:
                            n=int(input("Enter value which is not already covered:"))

                        while n not in range(1,10):
                            n=int(input("Please enter value from 1 to 9 :"))

                        cplcs.append(n)
                        s="x"
                        b.move(n,s)
                        print("")
                        if b.winx()==True:
                            print("Congrats!!! "+flop[0].name+" you won")
                            flop[0].won()
                            flag=False
                            break
                    
                    else:
                        print(flop[1].name+" enter integer corresponding where you want place o :", end="")
                        n=int(input())
                        while n in cplcs:
                            n=int(input("Enter value which is not already covered:"))

                        while n not in range(1,10):
                            n=int(input("Please enter value from 1 to 9 :"))

                        cplcs.append(n)
                        s="o"
                        b.move(n,s)
                        print("")
                        if b.wino()==True:
                            print("Congrats!!! "+flop[1].name+" you won")
                            flop[1].won()
                            flag=False
                            break
                if flag==True:
                    print("The game was a Draw")
                print("")
                print("Do you guys wish to play a new game ?")
                ng=input("Enter Y/N :")


            print("Hope you guys enjoyed")
            print("Here are the scores")
            for i in flop:
                print(i.name+" scored "+str(i.score)+" points ")

        elif nop==1:
            print("")
            l=["x","o"]
            lop=[]
            name=input("Enter name of player 1:")
            print("You will play with x")
            tot=l[0]
            p1=Player(name,tot)
            lop.append(p1)

            name="AI"
            print("AI will take "+l[1])
            tot=l[1]
            p2=Player(name,tot)
            lop.append(p2)


            print("")
            print("All set, lets go!!!")
            b.printboard()
            cplcs=[]
            flag=True
            for i in range(1,10):
                if i%2!=0:
                    print(lop[0].name+" enter integer corresponding where you want place x :", end="")
                    n=int(input())
                    while n in cplcs:
                        n=int(input("Enter value which is not already covered:"))

                    while n not in range(1,10):
                        n=int(input("Please enter value from 1 to 9 :"))

                    cplcs.append(n)
                    s="x"
                    b.move(n,s)
                    print("")
                    if b.winx()==True:
                        print("Congrats!!! "+lop[0].name+" you won")
                        lop[0].won()
                        flag=False
                        break
                
                else:
                    print("AI's turn")
                    n=int((random.randint(1,9)))
                    while n in cplcs:
                        n=int((random.randint(1,9)))

                    cplcs.append(n)
                    s="o"
                    b.move(n,s)
                    print("")
                    if b.wino()==True:
                        print(lop[1].name+" won")
                        lop[1].won()
                        flag=False
                        break

            if flag==True:
                    print("The game was a draw")
            print("")
            print("Do you wish to play a new game ?")
            ng=input("Enter Y/N :")
            print("")

            while ng!="N":
                b.newgame()
                print("Here is the fresh board")
                b.printboard()
                cplcs.clear()
                flag=True
                for i in range(1,10):
                    if i%2!=0:
                        print(lop[0].name+" enter integer corresponding where you want place x :", end="")
                        n=int(input())
                        while n in cplcs:
                            n=int(input("Enter value which is not already covered:"))

                        while n not in range(1,10):
                            n=int(input("Please enter value from 1 to 9 :"))

                        cplcs.append(n)
                        s="x"
                        b.move(n,s)
                        print("")
                        if b.winx()==True:
                            print("Congrats!!! "+lop[0].name+" you won")
                            lop[0].won()
                            flag=False
                            break
                    
                    else:
                        print("AI's turn")
                        n=int((random.randint(1,9)))
                        while n in cplcs:
                            n=int((random.randint(1,9)))

                        cplcs.append(n)
                        s="o"
                        b.move(n,s)
                        print("")
                        if b.wino()==True:
                            print(lop[1].name+" won")
                            lop[1].won()
                            flag=False
                            break

                if flag==True:
                    print("The game was a draw")
                print("")
                print("Do you guys wish to play a new game ?")
                ng=input("Enter Y/N :")


            print("Hope you enjoyed")
            print("Here are the scores")
            for i in lop:
                print(i.name+" scored "+str(i.score)+" points ")


    print("")
    print("Want to play again ??")
    print("In case you forgot the games we offer", end="")
    print('''
    1)Team 11
    2)TicTacToe
    3)Exit''')
    gn=int(input("Enter serial number of the game you want to play:"))

    while gn not in range(1,4):
        gn=int(input("Please enter serial number from 1 to 3"))

print("")
print("Bye :-)") 


