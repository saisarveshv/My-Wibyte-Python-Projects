import time
print ("This is a collection of games that I have created.")
time.sleep(1)
print("Given below are the various options.")
time.sleep(1)
point=input("1.Find the missing operator-type a\n2.Find the missing number-type b\n3.A conversation/quiz-type c\n4.Naruto jutsu battle(NEW)-type d-")
print("Pick your option")
time.sleep(1)
if point.lower()=='a':
    import random   
    print("Choose your difficulty")
    op_list = ['+', '-', '*']
#different difficulties based on number of operators/NOT BASED ON BODMAS
    difficulty=input("easy,medium,hard,impossible-")
    if difficulty=='easy':
        num1 = int(input('Please tell me a number\n'))
        num2 = int(input('Please tell me another number\n'))
        op = random.randint(0, 2)
        op_list = ['+', '-', '*']
        if op == 0:
            rhs = num1 + num2
        if op == 1:
            rhs = num1 - num2
        if op == 2:
            rhs = num1 * num2
        print('Can you tell me the missing operator\n')
        qn = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'
        answer = input(qn)
        if answer == op_list[op]:
            print('Well Done')
        else: 
            print('pathetic')
    if difficulty=='medium':
        num1 = int(input('Please tell me a number\n'))
        num2 = int(input('Please tell me another number\n'))
        print()
        num3 = random.randint(1, 100)
        print(num3)
        op1 = random.randint(0, 1)
        op2 = random.randint(0, 1)
        if op1 == 0:
            rhs = num1 + num2
        if op1 == 1:
            rhs = num1 - num2
        if op2 == 0:
            rhs = rhs + num3
        if op2 == 1:
            rhs = rhs - num3
        print('Can you tell me the missing operator\n')
        qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) + '\n'
        answer = input(qn)
        if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
            print('Well Done')
        else: 
            print('pathetic')
    if difficulty=='hard':
        op_list=['+','-','*']
        num1=int(input("enter a number"))
        num2=int(input("enter another number"))
        num3=int(input("enter another number"))
        num4=int(input("enter another number"))
        op1=random.randint(0,2)
        op2=random.randint(0,2)
        op3=random.randint(0,2)
        rhs=0
        if op1==0:
            rhs=num1+num2
        if op1==1:
            rhs=num1-num2
        if op1==2:
            rhs=num1*num2
        if op2==0:
            mhs=rhs+num3
        if op2==1:
            mhs=rhs-num3
        if op2==2:
            mhs=rhs*num3
        if op3==0:
            phs=mhs+num4
        if op3==1:
            phs=mhs-num4
        if op3==2:
            phs=mhs*num4
        print("Can you tell me the missing operators")
        qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) +'__'+str(num4)+'=' + str(phs) + '\n'
        count=0
        for i in range(3):
            answer=input(qn)
            if answer[0]==op_list[op1] and answer[1]==op_list[op2] and answer[2]==op_list[op3]:
                print ("well done")
                count=1
                break
            else:
                print ("try again")
        if count==0:
            print("Try it again, next time. The answer was")
        #guess the number
        if difficulty=='impossible':
            num1=int(input('pick a 5 and above digit number'))
        if num1/10000<0:
            print("pick another digit number")
            print("I myself will pick one")
        num1=random.randint(10000,99999)
        num2=random.randint(1,9999)
        rhs=num1/num2
        qn=str(num1)+'/'+'______'+'='+str(rhs)
        answer=input(qn)
        if answer==num2:
            print("your a genius")
            print("you deserve a gift")
            print("IIIIIIIIIII    TTTTTTTTTTTT      A           CCCCCCCCCCCCC    H              H       IIIIIIIIIIIIII")
            print("     I               T          A A         C                 H              H              I")
            print("     I               T         A   A       C                  H              H              I")
            print("     I               T        A     A     C                   H              H              I ")
            print("     I               T       A       A    C                   HHHHHHHHHHHHHHHH              I")
            print("     I               T      AAAAAAAAA A   C                   H              H              I")   
            print("     I               T     A           A   C                  H              H              I")    
            print("     I               T    A             A   C                 H              H              I")
            print("IIIIIIIIIII          T   A               A   CCCCCCCCCCCCCC   H              H       IIIIIIIIIIIIIII")
        else:
            print("You are normal") 
if point.lower()=='b':
    import random
    n=random.randint(1,100)

    print('I have chosen a number from 1 to 100')
    attempts=0
    done=False
    while not done:
        guess=int(input('Guess a number'))
        attempts=attempts+1
        if guess>n:
            print('My number is smaller than that')
        if guess<n:
            print ("My number is greater than that")
        if guess==n:
            print('you got the number correct')
            print('it took you',attempts,'attempts to get it right')
            done=True
    print()
    print()
    done=False
    print('Nows your chance to choose a number')
    print("click when you are ready")
    input()
    guess=0
    attempts=0
    guess_step=10;
    prev_answer='1'

    while not done:
        answer=input('Is it'+str(guess)+'?(y=yes,s=smallerthan that,l=larger than that)\n')
        attempts=attempts+1
        if attempts > 1: 
            if answer != prev_answer:
                guess_step = guess_step - 1
        
        prev_answer = answer
    
        if answer.lower() == 's':
            guess = guess - guess_step
        
        if answer.lower() == 'l':
            guess = guess + guess_step
        
        if answer.lower() == 'y':
            print('Bingo, I got it.')
            print('I took ', attempts, 'attempts to guess it.')
            done = True
        
    print()
    print()

    print('I think I can do it smarter ... ')
    print('Let me try binary search ... ')

    done = False
    low = 0
    high = 100
    guess_step = 0
    attempts = 0

    while not done:
        guess = round((low + high)/2)
        answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
        attempts = attempts + 1 

        if answer.lower() == 's':
            high = guess
        
        if answer.lower() == 'l':
            low = guess
        
        if answer.lower() == 'y':
            print('Bingo, I got it.')
            print('I took ', attempts, 'attempts to guess it.')
            done = True
        
    print()
    print()
    print("Do you want to play a special game-")
    n=input("yes or no")
    if n=='yes':
        naruto=input("Type a naruto character name.Type random if you want a random character-")
        if naruto=='random':
            ni=["Itachi",'Sasuke','Naruto','Sakura','Obito','Madara']
            nii=random.randint(1,len(ni))
            if nii==0:
                naruto='Itachi'
            if nii==1:
                naruto='Sasuke'
            if nii==2:
                naruto='Naruto'
            if nii==3:
                naruto='Sakura'
            if nii==4:
                naruto="Obito"
            if nii==5:
                naruto='Madara'
            nio=['Itachi','Madara','Obito','Sasuke','Naruto','Tsunade','Pain','Kisame','Sakura','Minato','Jiraiya','Orochimaru','Hidan','Kakuzu','Kisame','Deidara','Sasori']
            guues=0
            attempts=0
            q=input("does he belong to a special clan(y=yes,n=no)")
            if q=='y':
                mylist=nio[0:8]
                del nio 
                attempts=attempts+1
                mylist=['Itachi','Madara','Obito','Sasuke','Naruto','Tsunade','Pain','Kisame']
                qu=input("Is the person an Uchiha")
                if qu=='y':
                    mylist1=mylist[0:4]
                    del mylist
                    attempts=attempts+1
                    mylist1=['Madara','Sasuke','Itachi','Obito']
                    que=input('Did that person get the EMS?')
                    if que=='y':
                        mylist2=mylist1[0:2]
                        del mylist1
                        attempts=attempts+1
                        mylist2=['Madara','Sasuke']
                        ques=input('Is that person goated(Sasuke is not a goat')
                        if ques=='y':
                            print('That person is Madara')
                        else:
                            print('That person is Sasuke')
                
                    elif que=='n':
                        mylist2=mylist1[2:4]
                        del mylist1
                        attempts=attempts+1
                        mylist2=['Itachi','Obito']
                        ques=input('Does he have susanoo')
                        if ques=='y':
                            print('That person is Itachi')
                        else:
                            print('That person is Obito')
                elif qu=='n':
                    mylist1=mylist[4:8]
                    del mylist
                    attempts=attempts+1
                    mylist1=['Naruto','Pain','Tsunade','Kisame']
                    que=input('Is that person a uzumaki?')
                    if que=='y':
                        mylist2=mylist1[0:2]
                        del mylist1
                        attempts=attempts+1
                        mylist2=['Naruto','Pain']
                        ques=input('Is that person a jinchuriki?')
                        if ques=='y':
                            print('That person is Naruto')
                        else:
                            print('That person is Pain')
                    elif que=='n':
                        mylist2=mylist1[2:4]
                        del mylist1
                        attempts=attempts+1
                        mylist2=['Tsunade','Kisame']
                        ques=input('Is that person a hokage?')
                        if ques=='y':
                            print('That person is Tsunade')
                        else:
                            print('That person is Kisame')
            elif q=='n':
                mylist=nio[8:16]
                del nio

                mylist=['Sakura','Minato','Jiraiya','Orochimaru','Hidan','Deidara','Sasori']
                attempts=attempts+1
                qu=input('Is that person an akatsuki member?')
                if qu=='y':
                    mylist1=mylist[3:7]
                    del mylist
                    attempts=attempts+1
                    mylist1=['Orochimaru','Hidan','Deidara','Sasori']
                    que=input('Is that person a snake user?')
                    if que=='y':
                        print('That person is Orochimaru')
                    elif que=='n':
                        mylist1.pop(0)
                        attempts=attempts+1
                        mylist1=['Hidan','Deidara','Sasori']
                        ques=input('Does that person use a puppet?')
                        if ques=='y':
                            print('That person is Sasori')
                        else:
                            mylist1.pop(2)
                            mylist1=['Hidan','Deidara']
                            attempts=attempts+1
                            quest=input('Does that person use explosives?')
                            if quest=='y':
                                print('That person is Deidara')
                            else:
                                print('That person is Hidan')
            
                elif qu=='n':
                    mylist1=mylist[0:3]
                    del mylist
                    attempts=attempts+1
                    mylist1=['Sakura','Minato','Jiraiya']
                    que=input('Is that person a sensei?')
                    if que=='y':
                        mylist1.pop(0)
                        attempts=attempts+1
                        mylist1=['Minato','Jiraiya']
                        ques=input('Is that person the fourth hokage?')
                        if ques=='y':
                            print('That person is Minato')
                        else:
                            print('That person is Jiraiya')
                    elif que=='n':
                        print('That person is Sakura')
                        print('I guessed your character in',attempts,'attempts')
                    else:
                        po=input('I am confused, can you tell me the name of the character?')
                        print('Your character ',po,'is a great character, but is hard to guess, I will try to guess it next time')      
        poi=input('Did you have fun playing?')
        if poi=='yes':
            print('I am glad you had fun')
        elif poi=='no':        
            print('I am sorry you did not have fun, I will try to make it better next time')
            print('To make up for it____')
            print("IIIIIIIIIII    TTTTTTTTTTTT      A           CCCCCCCCCCCCC    H              H       IIIIIIIIIIIIII")
            print("     I               T          A A         C                 H              H              I")
            print("     I               T         A   A       C                  H              H              I")
            print("     I               T        A     A     C                   H              H              I ")
            print("     I               T       A       A    C                   HHHHHHHHHHHHHHHH              I")
            print("     I               T      AAAAAAAAA A   C                   H              H              I")   
            print("     I               T     A           A   C                  H              H              I")    
            print("     I               T    A             A   C                 H              H              I")
            print("IIIIIIIIIII          T   A               A   CCCCCCCCCCCCCC   H              H       IIIIIIIIIIIIIII")       
            print('Do you want to play again?')
            poiu=input('yes or no')
            if poiu=='yes':
                print("Click the run button")
            else: 
                print('You can play again some other time') 
if point.lower()=='c':
    import time
    print("This is a conversation game")
    response=input("Do you want to play ?Type y or n\n")
    if response.lower()=='y':
    
        print("You will have 3 options to choose from")
        choice=input.lower("Choose A,B or C\n")
        if choice=='A':
            print("I will give you another conversation")


            print()
            print("I am Itachi Uchiha")
            time.sleep(1)
            print("I am a ninja from the village hidden in the leaves")
            time.sleep(1)
            print("I have come to choose a new ninja for the akatsuki")
            time.sleep(1)
            print("You look like the ideal candidate, but I am ging to have to test you first")
            time.sleep(1)
            print("What is my goal?Destroy the hidden leaf or capture all the tailed beasts")
            ans=input("Your answer\n")
            if ans.lower()=='capture all the tailed beasts':
                print("You are correct")
                print("But that is not MY goal")
                time.sleep(1)
                print("What is the most powerful clan in the ninja world?")
                asw=input("Your answer\n")
                if asw.lower()=='uchiha':
                    print("I will forgive")
                    time.sleep(1)
                    print("I will ask  you one final question. What is my most prized jutsu?")
                    answ=input("Your answer\n")
                    if answ.lower()=='susanoo':
                        print("You are correct, you have passed the test")
                    elif answ.lower()=='None':
                        print("AMATERASU")
                    else:
                        print("You are wrong", "AMATERASU")
                else:
                    print("You are wrong", "AMATERASU")
            elif ans.lower()=='protect sasuke':
                print("How do you know my goal? You are defenitely a spy.","SUSANOO")
            else:
                print("You are wrong, But I will give you another chance")
                time.sleep(1)
            print("What is the most powerful clan in the ninja world?")
            asw=input("Your answer\n")
            if asw.lower()=='uchiha':
                print("I will forgive")
                time.sleep(1)
                print("I will ask  you one final question. What is my most prized jutsu?")
                answ=input("Your answer\n")
                if answ.lower()=='susanoo':
                    print("You are correct, you have passed the test")
                elif answ.lower()=='None':
                    print("AMATERASU")
                else:
                    print("You are wrong", "AMATERASU")
            else:
                print("You are wrong", "AMATERASU")
    if choice=='B':
        print("I will give you another conversation")
        time.sleep(1)
        print('I am the famous quiz master, Professor Grumpy')
        time.sleep(1)
        print("This is the famous quiz show, 'Who wants to be a millionaire'")
        time.sleep(1)
        print("You have to answer 3 questions correctly to win the grand prize of $1,000,000")
        time.sleep(1)
        print('But the questions asked here are going to be very hard, so you have to be very careful')


        print()
        print("Question 1: What is the capital of France?")
        ans=input("Your answer\n")
        if ans.lower()=='paris':
            print('You are correct, but the difficulty only increases from here')
            time.sleep(1)
            print('Question 2:What is the name of the movie which has one the most Oscars/')
            ans=input("Your answer\n")
            if ans.lower()=='ben-hur'or ans.lower()=='titanic' or ans.lower()=='the lord of the rings: the return of the king':
                print('You are correct, but the difficulty only increases from here')
                time.sleep(1)
                print('Question 3:What is the name of the second person to walk on the moon?')
                ans=input("Your answer\n")
                if ans.lower()=='buzz aldrin':
                    print('You are correct, you have won $1,000,000')
                else:
                    print('You are wrong, you have lost the game')
            else:
                print('There were three movies. How could you not the guess the correct answer? You have lost the game')
        else:
            print('You are wrong, how do you not know the capital of France? You have lost the game')
    if choice=='C':
        print('Now I will give you a fun yet challenging coversation')
        time.sleep(1)
        print('I am the Ghost of the Uchiha, Madara Uchiha')
        time.sleep(1)
        print('I have come to test your knowledge of the Uchiha clan, and if you pass, I will give you a special gift')
        time.sleep(1)
        print("But if you fail, you will end up like the other Uchihas")


        print()
        print("Question 1: What is the name of the founder of the Uchiha clan?")
        ans=input()
        if ans.lower()=='indra':
            print('You are correct, but the difficulty only increases from here')
            time.sleep(1)
            print("Question 2: What is the name of the Uchiha clan's Kekkai Genkai?")
            ans=input()
            if ans.lower()=='sharingan':
                print('You are correct, but the difficulty only increases from here')
                time.sleep(1)
                print("Question 3: What is the name of the Uchiha clan's most powerful jutsu?")
                ans=input()
                if ans.lower()=='susanoo':
                    print('You are correct')
                    time.sleep(1)
                    print("NOW, the final question:Name the three Uchiha clan members who have awakened the Mangekyo Sharingan")
                    ans=input()
                    tito=ans.find('Itachi'or 'Sasuke' or 'Madara' or 'Obito' or 'Shisui' or 'Izuna')
                    if tito==True and tito>=3:
                        print('You are correct, you have passed the test and will be rewarded with a special gift, MY AMATERASU')
                        time.sleep(1)
                        print('Just kidding, as a reward, you can live')
                    else:
                        print('You are wrong, you have failed the test and will end up like the other Uchihas')
                else:
                    print('You are wrong, you have failed the test and will end up like the other Uchihas')
            else:
                print('You are wrong, you have failed the test and will end up like the other Uchihas')
if point.lower()=='d':
    import time
    import random  
    print("This is a Naruto jutsu battle game")
    time.sleep(1)
    scores=0
    oppscore=0
    choice=0
    print("You will be given a choice of 3 jutsus to choose from")
    time.sleep(1)
    print("The jutsus are:Rasengan-a,Chidori-b,water style: bomb jutsu-c")
    time.sleep(1)
    print("The opponent will also choose a jutsu")
    time.sleep(1)
    print("The winner will be decided based on the following rules:")
    time.sleep(1)
    print("Rasengan beats Chidori")
    time.sleep(1)
    print("Chidori beats Water style: bomb jutsu")
    time.sleep(1)
    print("Water style: bomb jutsu beats Rasengan")
    time.sleep(1)
    lol=input("Type your option of jutsu-a,b or c\n")
    time.sleep(1)
    choice=random.choice(['Rasengan','Chidori','Water style: bomb jutsu'])
    if lol=='a':
        print("You have chosen Rasengan")
        time.sleep(1)
        print("The opponent has chosen",choice)
        time.sleep(1)
        if choice=='Rasengan':
            print("It is a tie")
        elif choice=='Chidori':
            print("You win")
            scores=scores+1
        elif choice=='Water style: bomb jutsu':
            print("You lose")
            oppscore=oppscore+1
    elif lol=='b':
        print("You have chosen Chidori")
        time.sleep(1)
        print("The opponent has chosen",choice)
        time.sleep(1)
        if choice=='Rasengan':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Chidori':
            print("It is a tie")
        else:
            print("You win")
            scores=scores+1
    elif lol=='c':
        print("You have chosen Water style: bomb jutsu")
        time.sleep(1)
        print("The opponent has chosen",choice)
        time.sleep(1)
        if choice=='Rasengan':
            print("You win")
            scores=scores+1
        elif choice=='Chidori':
            print("You lose")
            oppscore=oppscore+1
        else:
            print("It is a tie")
    print("Round 2:You will be given a choice of three characters to choose from")
    time.sleep(1)
    print("The characters are:Naruto-a,Sasuke-b,Kakashi-c")
    time.sleep(1)
    print("The opponent will also choose a character")
    time.sleep(1)
    print("The winner will be decided based on the following rules:")
    time.sleep(1)
    print("Kakashi beats Naruto")
    time.sleep(1)
    print("Sasuke beats Kakashi")
    time.sleep(1)
    print("Naruto beats Sasuke")
    time.sleep(1)
    loli=input("Type your option of character-a,b or c\n")
    time.sleep(1)
    choice=random.choice(['Naruto','Sasuke','Kakashi'])
    if loli=='a':
        print("You have chosen Naruto")
        time.sleep(1)
        print("The opponent has chosen",choice)
        if choice=='Naruto':
            print("It is a tie")
        elif choice=='Sasuke':
            print("You lose")
            oppscore=oppscore+1
        else:
            print("You win")
            scores=scores+1
    elif loli=='b':
        print("You have chosen Sasuke")
        time.sleep(1)
        print("The opponent has chosen",choice)
        if choice=='Naruto':
            print("You win")
            scores=scores+1
        elif choice=='Sasuke':
            print("It is a tie")
        else:
            print("You lose")
            oppscore=oppscore+1
    elif loli=='c':
        print("You have chosen Kakashi")
        time.sleep(1)
        print("The opponent has chosen",choice)
        if choice=='Naruto':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Sasuke':
            print("You win")
            scores=scores+1
        else:
            print("It is a tie")
    print("Round 3:You will be given a choice of three characters and jutsu to choose from")
    time.sleep(1)
    print("You could also choose a trump player who will either beat any character or jutsu or will lose instantly to any character or jutsu")
    time.sleep(1)
    print("Your characters and jutsus are:Hashirama-a,Madara-b,Naruto-c;Wood style-1,Rinnegan-2,Rasen Shuriken-3:Trumpmaster-4")
    time.sleep(1)
    print("The opponent will also choose a character and jutsu")
    time.sleep(1)
    nop=input("Type your option of character and jutsu-a1,a2,a3,b1,b2,b3,c1,c2,c3,4\n")
    choicese=random.choice(['Hashirama and Wood style','Madara and Rinnegan','Naruto and Rasen Shuriken',])
    if nop=='a1':
        print("You have chosen Hashirama and Wood style")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("It is a tie")
        elif choice=='Madara and Rinnegan':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Naruto and Rasen Shuriken':
            print("You win")
            scores=scores+1
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='a2':
        print("You have chosen Hashirama and Rinnegan")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You win")
            scores=scores+1
        elif choice=='Madara and Rinnegan':
            print("It is a tie")
        elif choice=='Naruto and Rasen Shuriken':
            print("You lose")
            oppscore=oppscore+1
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='a3':
        print("You have chosen Hashirama and Rasen Shuriken")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Madara and Rinnegan':
            print("You win")
            scores=scores+1
        elif choice=='Naruto and Rasen Shuriken':
            print("It is a tie")
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='b1':
        print("You have chosen Madara and Wood style")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Madara and Rinnegan':
            print("It is a tie")
        elif choice=='Naruto and Rasen Shuriken':
            print("You win")
            scores=scores+1
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='b2':
        print("You have chosen Madara and Rinnegan")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You win")
            scores=scores+1
        elif choice=='Madara and Rinnegan':
            print("It is a tie")
        elif choice=='Naruto and Rasen Shuriken':
            print("You lose")
            oppscore=oppscore+1
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='b3':
        print("You have chosen Madara and Rasen Shuriken")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Madara and Rinnegan':
            print("You win")
            scores=scores+1
        elif choice=='Naruto and Rasen Shuriken':
            print("It is a tie")
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='c1':
        print("You have chosen Naruto and Wood style")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Madara and Rinnegan':
            print("You win")
            scores=scores+1
        elif choice=='Naruto and Rasen Shuriken':
            print("It is a tie")
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='c2':
        print("You have chosen Naruto and Rinnegan")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You win")
            scores=scores+1
        elif choice=='Madara and Rinnegan':
            print("It is a tie")
        elif choice=='Naruto and Rasen Shuriken':
            print("You lose")
            oppscore=oppscore+1
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='c3':
        print("You have chosen Naruto and Rasen Shuriken")
        time.sleep(1)
        print("The opponent has chosen",choicese)
        if choice=='Hashirama and Wood style':
            print("You lose")
            oppscore=oppscore+1
        elif choice=='Madara and Rinnegan':
            print("You win")
            scores=scores+1
        elif choice=='Naruto and Rasen Shuriken':
            print("It is a tie")
        else:
            print("You lose instantly")
            oppscore=oppscore+1
    if nop=='4':
        trump=random.choice(['Itachi','Ino','Kaguya','Shikamaru'])
        if trump=='Itachi':
            print("You have chosen Itachi, the trump player")
            time.sleep(1)
            print("The opponent has chosen",choicese)
            print("You win instantly")
            scores=scores+1
        elif trump=='Ino':
            print("You have chosen Ino, the trump player")
            time.sleep(1)
            print("The opponent has chosen",choicese)
            print("You lose instantly")
            oppscore=oppscore+1
        elif trump=='Kaguya':
            print("You have chosen Kaguya, the trump player")
            time.sleep(1)
            print("The opponent has chosen",choicese)
            print("You win instantly")
            scores=scores+1
        elif trump=='Shikamaru':
            print("You have chosen Shikamaru, the trump player")
            time.sleep(1)
            print("The opponent has chosen",choicese)
            print("You lose instantly")
            oppscore=oppscore+1
    print("The final score is: You-",scores,"Opponent-",oppscore)
    if scores>oppscore:
        print("You win")
    elif scores<oppscore:
        print("You lose")
    else:
        print("It is a tie")   
#end of program