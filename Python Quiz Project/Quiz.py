import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import random
from string import ascii_lowercase
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1500)
questions={}
h=['simran','vidushi','akshara','nisha']
p=['1105','2606','1505','1102']
s1=input('Enter the Host Name:')
s2=input('Enter the Password:')
quiz=pd.read_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Quiz.csv')
player=pd.read_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Players.csv')
if s1 in h :
    if s2 in p:
        while True:
            sco=0
            canswer=0
            wanswer=0
            print('\n')
            print('                                         KNOWLEDGE KNOCKOUT                                      ')
            print('                                           _____________                                         ')
            print('\n')
            print('                          Designed by Simran Prabhakar and Yash Rajora                           ')
            print('                           Under the guidance of Dr. Nripendra Dwivedi                           ')
            print('\n')
            print('\n')
            print('++=============================================================================================++')
            print('||                                     ___             _____                                   ||')
            print('||                         |\  /|  /\   | |\  |  |\  /||    |\  ||   |                         ||')
            print('||                         | \/ | /--\  | | \ |  | \/ ||----| \ ||   |                         ||')
            print('||                         |    |/    \_|_|  \|  |    ||____|  \||___|                         ||')
            print('||                                                                                             ||')
            print('++=============================================================================================++')
            print('||                                                                                             ||')
            print('||                           Select From The Following Options                                 ||')
            print('||                                                                                             ||')
            print('||                          (a)Play Game                                                       ||')
            print('||                          (b)Add Player Record                                               ||')
            print('||                          (c)Update the Player Record                                        ||')
            print('||                          (d)Search  the Player Record                                       ||')
            print('||                          (e)Delete Player Record                                            ||')
            print('||                          (f)Analise the Data                                                ||')
            print('||                          (g)Exit                                                            ||')
            print('++=============================================================================================++')
            o=input('Enter a Option:')
            if o=='a' or o=='A':
                o1=int(input("Enter The Id:"))
                print('\n')
                l1=player['ID'].tolist()
                if o1 not in l1:
                    print('Id not available!')
                    c=input('Press Enter to Continue')
                else:
                    print('Select From following Modes')
                    print('\n')
                    print('-Select Option-')
                    print('(a)Easy(10Q)')
                    print('(b)Medium(20Q)')
                    print('(c)Hard(35Q)')
                    print('(d)Brutal(50Q)')
                    print('(e)GOD MODE(80Q)')
                    o2=input('Enter a Option:')
                    print('\n')
                    if o2=='a' or o2=='A':
                        a=10
                        level='Easy'
                    elif o2=='b' or o2=='B':
                        a=20
                        level='Medium'
                    elif o2=='c' or o2=='C':
                        a=35
                        level='Hard'
                    elif o2=='d' or o2=='D':
                        a=50
                        level='Brutal'
                    elif o2=='e' or o2=='E':
                        a=80
                        level='GOD MODE'
                    else:
                        print('Ivalid Option')
                        break
                    quiz1=quiz.sample(n=a,axis='columns')
                    a=list(quiz1.columns.values)
                    q=len(a)
                    for i in range(q):
                        s=a[i]
                        l=quiz[s].to_list()    
                        questions[s]=l
                    for n,(question,alternatives) in enumerate(questions.items(),start=1):
                        
                        print(f"Question{n}:")
                        print('\n')
                        print(f"{question}?")
                        correct_answer=alternatives[0]
                        la=dict(zip(ascii_lowercase,random.sample(alternatives,k=4)))
                        for label,alternatives in la.items():
                            print(f" {label}){alternatives}")     
                        answerl=input("Choice?")
                        answer=la.get(answerl)
                        if answer==correct_answer:
                            sco+=20
                            canswer+=1
                            print("Good Job,Correct Answer")
                            c=input('Press Enter to Continue')
                            print('\n')
                            print('________________________________________________________________________')
                        else:
                            print("Sorry Wrong Answer")
                            sco-=5
                            wanswer+=1
                            c=input('Press Enter to Continue')
                            print('\n')
                            print('________________________________________________________________________')
                    print('\n')        
                    c=input('Press Enter to Continue or Y/y to Update the Score:')        
                    if c=='Y' or c=='y':
                        h=player.index[(player['ID']==o1)]
                        player.loc[h,'Score']=sco
                        player.loc[h,'Correct_answer']=canswer
                        player.loc[h,'Wrong_answer']=wanswer
                        player.loc[h,'Mode']=level
                        print(player)
                        player.to_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Players.csv',na_rep='NULL',index=False)
                        c=input('Press Enter to Continue')
                        
            elif o=='b' or o=='B':
                i=int(input('Enter the Id For Player:'))
                e=player['ID'].tolist()
                if i in e :
                    print('Id already Exists')
                    c=input('Press Enter to Continue')
                else:
                    name=input('Enter the Name of Player:')
                    gender=input('Enter the Gender of Player:')
                    age=input('Enter the Age of Player:')
                    area=input('Enter the Area of Player:')
                    ap=[i,name,gender,age,area,0,0,0,np.NaN]
                    le=len(player)
                    player.loc[le]=ap
                    print('Adding Data....')
                    print('\n')
                    print('Data Added Sucessfully!!')
                    print('\n')
                    print(player)
                    print('\n')
                    player.to_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Players.csv',na_rep='NULL',index=False)
                    c=input('Press Enter to Continue')
                    
            elif o=='c' or o=='C':
                c1=input('Enter the Column name:')
                r1=int(input('Enter the Id of Player:'))
                v=input('Enter the Value:')
                h=player.index[(player['ID']==r1)]
                player.loc[h,c1]=v
                print('Updating Data....')
                print('\n')
                print('Data Updated Sucessfully!!')
                print('\n')
                print(player)
                print('\n')
                player.to_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Players.csv',na_rep='NULL',index=False)
                c=input('Press Enter to Continue')
            
            elif o=='d' or o=='D':
                r3=int(input('Enter the ID of Player:'))
                print('Searching Data....')
                print('\n')
                print('Data Searched Sucessfully!!')
                print('\n')
                print(player.loc[player['ID']==r3])
                print('\n')
                c=input('Press Enter to Continue')
           
            elif o=='e' or o=='E':
                r5=int(input('Enter the ID of Player:'))
                print('Deleting Data....')
                print('\n')
                print('Data Deleted Sucessfully!!')
                player.drop(player.index[(player['ID']==r5)],axis=0,inplace=True)
                print('\n')
                print(player)
                print('\n')
                player.to_csv('C:\\Users\\Dell\\Documents\\Python Scripts\\Players.csv',index=False)
                c=input('Press Enter to Continue')
            
            elif o=='f' or o=='F':
                print('Select From The Following Option')
                print('(a)Show All Column Name')
                print('(b)Arrange in Order ')
                print('(c)Create Graph')
                o2=input('Enter a Option:')
                if o2=='a' or o2=='A':
                    print(player.columns)
                    print('\n')
                    c=input('Press Enter to Continue')

                elif o2=='b' or o2=='B':
                    j=input('Enter a Column by which you want order by:')
                    j1=input('Enter a Ascend(A,a)/Desend(D,d):')
                    if j1=='A' or  j1=='a':
                        print(player.sort_values([j],ascending=[True]))
                        print('\n')
                        c=input('Press Enter to Continue')


                    elif  j1=='D' or j1=='d':
                        print(player.sort_values([j],ascending=[False]))
                        print('\n')
                        c=input('Press Enter to Continue')


                    else:
                         print('Invalid option selected by the Host')
                         print('Please Try again!')
                         c=input('Press Enter to Continue')

                elif o2=='c' or o2=='C':
                    print('Line chart(l or L)')
                    print('Bar chart(b or B)')
                    o5=input('Enter the type of Graph:')
                    if o5=='l' or  o5=='L':
                        print('Line chart is Selected. ')
                        m1=input('Enter the Column for Graph(X):')
                        m2=input('Enter the Column for Graph(Y):')
                        t1=input('Enter the Label for X-Axis:')
                        t2=input('Enter the Label for Y-Axis:')
                        l1=player[m1].tolist()
                        l2=player[m2].tolist()
                        pl.plot(l1,l2)
                        pl.xlabel(t1)
                        pl.ylabel(t2)
                        pl.show()
                        c=input('Press Enter to Continue')

                    elif o5=='B' or  o5=='b':
                        print('Bar chart is Selected ')
                        m1=input('Enter the Column for Graph(X):')
                        m2=input('Enter the Column for Graph(y):')
                        t1=input('Enter the Label for X-Axis:')
                        t2=input('Enter the Label for Y-Axis:')
                        l1=player[m1].tolist()
                        l2=player[m2].tolist()
                        pl.bar(l1,l2)
                        pl.xlabel(t1)
                        pl.ylabel(t2)
                        pl.show()
                        c=input('Press Enter to Continue')

            elif o == 'g' or o=='G':
                 print('😊Thank you for Playing😊')
                 m=input('Press Enter Key to Quit')
                 break

            else:
                 print('Invalid option')
                 print('Please Try again!')
                 c=input('Press Enter to Continue')               
                              
    else:
        print('Invalid Password entered')
        print('Please Try again!')
        m=input('Press Enter Key to Quit')

else:
    print('Invalid Host ')
    print('Please Try again!')
    m=input('Press Enter Key to Quit')