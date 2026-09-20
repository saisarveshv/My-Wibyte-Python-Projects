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
  if naruto==random:
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
    nio=['Naruto','Itachi','Madara','Obito','Sakura','Sasuke','Minato','Tsunade','Jiraiya','Pain','Orochimaru','Hidan','Kakuzu','Kisame','Deidara','Sasori']
    guues=0
    attempts=0
    q=input("does he belong to a special clan(y=yes,n=no)")
    if q=='y':
      nio.pop(4)
      nio.pop(6)
      nio.pop(8)
      nio.pop(10)
      nio.pop(11)
      nio.pop(12)
      nio.pop(14)
      nio.pop(15)
      attempts=attempts+1
      nio=['Naruto','Itachi','Madara','Obito','Sasuke','Tsunade','Pain','Kisame']
      qu=input("Is the person an Uchiha")
      if qu=='y':
        nio.pop(0)
        nio.pop(5)
        nio.pop(6)
        nio.pop(7)
        attempts=attempts+1
        nio=['Itachi','Madara','Obito','Sasuke']
        que=input('Did that person get the EMS?')
        if que=='y':
          nio.pop(0)
          nio.pop(2)
          attempts=attempts+1
          nio=['Madara','Sasuke']
          ques=input('Is that person goated(Sasuke is not a goat')
          if ques=='y':
             print('That person is Madara')
          else:
            print('That person is Sasuke')
          
        elif que=='n':
          nio.pop(1)
          nio.pop(3)
          nio=['Itachi','Obito']
          attempts=attempts+1
          ques=input('Does he have susanoo')
          if ques=='y':
            print('That person is Itachi')
          else:
            print('That person is Obito')
      elif qu=='n':
        nio.pop(1)
        nio.pop(2)
        nio.pop(3)
        nio.pop(4)
        attempts=attempts+1
        nio=['Naruto','Tsunade','Pain','Kisame']
        que=input('Is that person a uzumaki?')
        if que=='y':
          nio.pop(1)
          nio.pop(4)
          attempts=attempts+1
          nio=['Naruto','Pain']
          ques=input('Is that person a jinchuriki?')
          if ques=='y':
            print('That person is Naruto')
          else:
            print('That person is Pain')
        elif que=='n':
          nio.pop(0)
          nio.pop(2)
          attempts=attempts+1
          nio=['Tsunade','Kisame']
          ques=input('Is that person a hokage?')
          if ques=='y':
            print('That person is Tsunade')
          else:
            print('That person is Kisame')
    elif q=='n':
      nio.pop(0)
      nio.pop(1)
      nio.pop(2)
      nio.pop(3)
      nio.pop(5)
      nio.pop(7)
      nio.pop(9)
      nio.pop(13)

      nio=['Sakura','Minato','Jiraiya','Orochimaru','Hidan','Deidara','Sasori']
      attempts=attempts+1
      qu=input('Is that person an akatsuki member?')
      if qu=='y':
        nio.pop(0)
        nio.pop(1)
        nio.pop(2)
        nio.pop(4)
        nio.pop(5)
        attempts=attempts+1
        nio=['Orochimaru','Hidan','Deidara','Sasori']
        que=input('Is that person a snake user?')
        if que=='y':
          print('That person is Orochimaru')
        elif que=='n':
          nio.pop(0)
          attempts=attempts+1
          nio=['Hidan','Deidara','Sasori']
          ques=input('Does that person use a puppet?')
          if ques=='y':
            print('That person is Sasori')
          else:
            nio=['Hidan','Deidara']
            attempts=attempts+1
            quest=input('Does that person use explosives?')
            if quest=='y':
              print('That person is Deidara')
            else:
              print('That person is Hidan')
      
      elif qu=='n':
        nio.pop(0)
        nio.pop(1)
        nio.pop(2)
        nio.pop(3)
        attempts=attempts+1
        nio=['Sakura','Minato','Jiraiya']
        que=input('Is that person a sensei?')
        if que=='y':
          nio.pop(0)
          attempts=attempts+1
          nio=['Minato','Jiraiya']
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