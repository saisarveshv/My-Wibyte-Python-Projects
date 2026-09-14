import random
import colorama    
from colorama import Fore,Back,Style
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
        print(Fore.RED+   "IIIIIIIIIII    TTTTTTTTTTTT      A           CCCCCCCCCCCCC    H              H       IIIIIIIIIIIIII")
        print(Fore.BLACK+ "     I               T          A A         C                 H              H              I")
        print(Fore.BLUE+  "     I               T         A   A       C                  H              H              I")
        print(Fore.ORANGE+"     I               T        A     A     C                   H              H              I ")
        print(Fore.PURPLE+"     I               T       A       A    C                   HHHHHHHHHHHHHHHH              I")
        print(Fore.PINK+  "     I               T      AAAAAAAAA A   C                   H              H              I")   
        print(Fore.YELLOW+"     I               T     A           A   C                  H              H              I")    
        print(Fore.CYAN+  "     I               T    A             A   C                 H              H              I")
        print(Fore.BLACK+ "IIIIIIIIIII          T   A               A   CCCCCCCCCCCCCC   H              H       IIIIIIIIIIIIIII")
    else:
        print("You are normal")
#End of code