import time
print('Hi I am the professors new assistant')
time.sleep(2)
print('So you want to meet the professor')
time.sleep(2)
print('First you have to pass my quiz')
time.sleep(2)
score=3
answer=input('Tell me what are action words called in english\n' )
if answer.lower()=='verbs':
    print('You are correct but this is only a warm up question')
    score=score-1

    time.sleep(2)
    answers=input('Give me a eight letter word with three vowels')
    if len(answer)==8:
        print('Your word has eight letters')
        count_a=answer.count('a')
        count_e=answer.count('e')
        count_i=answer.count('i')
        count_o=answer.count('o')
        count_u=answer.count('u')
        count_vowels=count_a+count_e+count_i+count_u+count_o
        if count_vowels<3:
            print('There are too many vowels you idiot')
            score=score+1
        elif count_vowels==3:
            print('You are surprisingly correct, but I think it was a fluke')
            score=score-1
        else:
            print('There are too less vowels you moron')
            score=score+1
    else:
        print("You can't even count the number of letters in your word. I am speechless")
        score=score+2
        
    print()
    time.sleep(2)
    sentence = input("ok, tell me a sentence ending in 'wise assistant' (no question please)\n")
    if sentence.endswith('wise assistant'):
        print("Haven't you learnt about punctuations?")
        
    elif sentence.endswith('wise assistant.'):
        len_first = sentence.find(' ')
        po=sentence.find('idiot'or' moron' or ' animal' or ' fool' or ' stupid'or ' dumb' or ' jerk' or ' loser' or ' moron' or ' nincompoop' or ' simpleton' or ' twit' or ' blockhead' or ' bonehead' or ' dimwit' or ' dunce' or ' ignoramus' or ' nitwit' or ' numbskull' or ' oaf' or ' pinhead' or ' saphead' or ' slowpoke' or ' thickhead')
        if len_first < 5:
            print("The first word in the sentence is too short.")
            score=score-1
        if po==True:
            print("You have used a derogatory word in your sentence. I am disappointed.")
            score=score+1
    else:
        print("I really think you will make the professor furious.")
        score=score+2
    if score==0:
        print("You have passed the quiz, you can meet the professor")
        time.sleep(1)
        print("I will now schedule your appointment with the professor")
        time.sleep
        print("Ok, pick your preferred appointment time for next Monday(A/B/C/D)")
        time.sleep
        print("A. 8 mins past midnight", "B. 16 mins before sunrise", sep='\t');
        time.sleep(1) 
        print("C. 24 mins before noon", "D. 48 mins after sunset", sep='\t');
        appointment = input('Select your slot (A/B/C/D)\n')
        
        if appointment == 'A':
            print("Careful, Prof may be sleepy.")
        elif appointment == 'B':
            print("Warning, Prof. may be jogging.")
        elif appointment == 'C':
            print("Beware, Prof. may be hungry.")
        else:
            print("Caution, Prof. may be tired.")
        
    elif score==1:
        print('There is a chance you can meet the professor, but I am not sure if he will be happy to see you.I will schedule your appointment with the professor later')
    else:
        print("You have failed the quiz, you cannot meet the professor")
        time.sleep(1)
        print("I will not schedule your appointment with the professor")
    
else:
    print("Which grade are you in, -1")
    time.sleep(1)
print('You cannot meet the professor if you cannot answer a simple question. Goodbye.')

print("Do you want to play a new game(yes or no)")
response=input()
if response.lower()=='yes':
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
if response=='no':
    print('Well your no fun')
    time.sleep(1)    
    print('Just cause your like me')
    time.sleep(1)
    print('I will now schedule your appointment with the professor')
    time.sleep(1)        
    print('You can leave now')
    time.sleep(1)