import time
import numpy as noo
import turtle
print("You have to different games to choose")
time.sleep(2)
choice=input("Choose a or b")
time.sleep(2)
if choice=='a':
    print("You are the chief selector of an ipl cricket team:DC")
    time.sleep(2)
    print("Your task is to create a good ipl team")
    time.sleep(2)
    print("You have to buy five  players;Namely a batter,an all-rounder, a bowler and two subs")
    time.sleep(2)
    print("For each, you have three choices, but you have to select them all within the budget of 100cr")
    time.sleep(2)
    print ('The players are as follows')
    time.sleep(2)
    batterlist=['Kl Rahul     ','Rishab Pant   ','Jaiswal       ','Ruturaj Gaikwad','Abhishek Sharma']
    time.sleep(2)
    price=[20,15,13,10,16]
    time.sleep(2)
    print('PLAYER(BATTER)','PRICE(IN CRORE)',sep='\t\t\t')
    for kk in range(len(batterlist)):
        print(str(kk+1)+'. '+batterlist[kk],price[kk],sep='\t\t')

    a=0
    b=0
    shopping_complete=0

    while shopping_complete==0:
        order=int(input('Enter 1 to 5 to select a player.'))


        if order<=5:
            print('You have selected player',batterlist[order-1])
            a=batterlist[order-1]
            b=price[order-1]
            shopping_complete=shopping_complete+1
        else:
            print('invalid input')

    print("Next you have the choose your all-rounder")   
    time.sleep(2)    
    all_round=['H Pandya     ','Ravindra Jadeja'  ,'Axar Patel      ','Sunil Narine    ','Shivam Dube     ']
    time.sleep(2)
    prices=[20,18,13,16,8]
    time.sleep(2)
    print('PLAYER(ALL-ROUNDER)','PRICE(IN CRORE)',sep='\t\t\t')
    for ll in range(len(all_round)):
        print(str(ll+1)+'. '+all_round[ll],prices[ll],sep='\t\t\t')

    
    shoping=0
    c=0
    d=0
    while shoping==0:
        orde=int(input("enter 1 to 5 to select a player"))
        if orde<=5:
            print('You have chosen',all_round[orde-1])
            c=all_round[orde-1]
            d=prices[orde-1]
            shoping=shoping+1
        else:
            print('Invalid player')


    print('Next you have to buy a bowler')
    time.sleep(2)
    bowler=['Bumrah        ','Siraj        ', 'Kuldeep Yadav ','Starc          ','Harshit Rana  ']
    time.sleep(2)
    pricess=[20,18,13,16,8]
    print('PLAYER(BOWLER)','PRICE(IN CRORE)',sep='\t\t\t')
    for bb in range(len(bowler)):
        print(str(bb+1)+'. '+bowler[bb],pricess[bb],sep='\t\t')
    
    
    shopingg=0
    e=0
    f=0
    while shopingg==0:
        orders=int(input("enter 1 to 5 to select a player"))
        if orders<=5:
            print('You have chosen',bowler[orders-1])
            e=bowler[orders-1]
            f=pricess[orders-1]
            shopingg=shopingg+1
        else:
            print('Invalid player')


    print("now you have to choose your two substitutes")
    time.sleep(2)
    print("You will have a choice of ten players to choose from")
    subs=['Sanju Samson   ','Dev Padikkal','Tilak Varma   ','Sai Sudharshan','Romario Shepherd','Corbin Bosch   ','Khaleel Ahmed','Bhuvneshwar Kumar','Varun Chakravarty','Mohammad Shami']
    time.sleep(2)
    pricesy=[15,11,17,9,2,1,4,10,5,8]
    print('PLAYER NAME(SUB)','PRICE(IN CRORES)',sep='\t\t\t')
    for ss in range(len(subs)):
        print(str(ss+1)+'. '+subs[ss],pricesy[ss],sep='\t\t\t')

    shopsy=0
    g=[]
    h=[]
    while shopsy==0:

        ordersss=int(input("choose two players and enter number between 1 to 10,11 to finish"))
        if ordersss<=10:
            print("You have chosen",subs[ordersss-1])
            g.append(subs[ordersss-1])
            h.append(pricesy[ordersss-1])
        elif ordersss==11:
            print('You have finished your purchases')
            shopsy=shopsy+1
    if len(g)>2 or len(g)<2:
        print('You are eliminated')
    else:
        print('You have finished creating your team')
        time.sleep(2)
        print("Your players are as follows:")
        time.sleep(2)
        print('PLAYER','COST(IN CRORES)',sep='\t\t\t')
        final=[a,c,e]
        po=final.extend(g)
        finalm=[b,d,f]
        ro=finalm.extend(h)
        grand=b+d+f+h[0]+h[1]
        for pp in range(5):
            print(final[pp],finalm[pp],sep='\t\t\t')
        print("your grand total is",grand)
        if grand>100:
            print("You have expended over the budget. Therefore, you are eliminated")
        else:
            print("you have expended within the budget. Well done")
            time.sleep(2)
            print("Now you have to buy sports equipment for your team")
            time.sleep(2)
            print("this time you have an unlimited budget")
            time.sleep(2)
            print('Welcome to the IPL cricket store')
            time.sleep(2)
            print()

            items = ['Cricket ball', 'Bat', 'Gloves', 'Helmet  ', 'Protection gear  ']
            pric = [9999.99, 120000.99, 14999.99, 19999.99, 1000000.99]

            print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
            for aa in range(len(items)):
                print(str(aa+1)+'. '+items[kk], pric[kk], sep='\t\t')

            shopping_cart1 = [] 
            shopping_quant1= []
            shopping_complete1= 0

            while shopping_complete1==0:

                order = int(input('Enter 1 to 5 to select an item, 6 to proceed to checkout.\n')) 
    
   
    
                if order <= 5:
        
                    print('You selected', items[order-1])
                    time.sleep(2)
                    quant = int(input('How many units do you wish to purchase?\n'))

        
                    if items[order-1] in shopping_cart1:
                        idx = shopping_cart1.index(items[order-1])
            
                        shopping_quant1[idx]+=quant
                    else:
                        shopping_cart1.append(items[order-1])        
                        shopping_quant1.append(quant)        
        
                        print('Added to shopping cart:', quant, 'units of', items[order-1])
                elif order == 6:
                    shopping_complete1= 1
                else: 
                    print("that was not a valid input.")
        



        
 

            print()
            print('Your Shopping Cart:')
            time.sleep(2)

 
            grand_tot1 = 0.0
            print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
            for cc in range(len(shopping_cart1)):
                idx = items.index(shopping_cart1[kk])
                unit_price=price[idx]
                tot_price = round(unit_price*shopping_quant1[cc], 2)
                grand_tot1 += tot_price
                print(shopping_cart1[cc], shopping_quant1[cc], unit_price, tot_price, sep='\t\t\t')

                grand_tot = round(grand_tot1, 2)
                print()
                print('Your total order is (INR)', grand_tot1)
                if shopping_quant1>20 and grand>80:
                    if grand_tot1>=10000000:
                        time.sleep(2)
                        print("You have bought good players and you have bought the right amount of equipment. As a result your team has won the IPL. But you have over expended and your team is making a loss. Therefore you have been fired")
                    else:
                         time.sleep(2)
                         print("You have bought good players and you have bought the right amount of equipment. As a result your team has won the IPL. Well done. You have won.")
                elif shopping_quant1<20 and grand>80:
                    time.sleep(2)
                    print('You have bought good players but you did not buy enough equipment to train them. As a result, they lost the IPL. You lost.')
                elif shopping_quant1>20 and grand<80:
                    time.sleep(2)
                    print('You bought enough equipment to train them but you did not buy good players. As a result, they lost the IPL. You lost.')
                else:
                    time.sleep(2)
                    print('You did not buy good players nor did you buy enough equipment to train them. As a result, they lost the IPL. You lost.')
elif choice=='b':
    print('You are one of the kages of the Ninja World.')
    time.sleep(2)
    print('You have agreed to trade deal with the Village Hidden the Leaves.')
    time.sleep(2)
    print('But the route to the Hidden Leaf Village is really dangerous.')
    time.sleep(2)
    print('For that you have desired to hire the akatsuki. You have been given a list of their ninja.')
    time.sleep(2)
    print('You have to decide who to hire.')
    time.sleep(2)
    print('Your budget is 1000000 ryo')
    time.sleep(2)
    print("Here is the list:")
    time.sleep(2)
    
    ninja=['Itachi Uchiha','Pain          ','Kisame       ','Hidan        ','Sasori       ','Deidara        ','Kakuzu       ','Obito          ','Konan          ','Orochimaru    ']

    ryo=[999999,800000,600000,300000,200000,500000,300000,1000001,100000,600000]
    print('NINJA','FEE',sep='\t\t\t\t\t')
    time.sleep(2)
    for ii in range(len(ninja)):
        print(str(ii+1)+'. '+ninja[ii],ryo[ii],sep='\t\t\t')
    buying=0
    buyquant=[]
    buyguy=[]

    while buying==0:

        buys=int(input("Pick the ninja from 1 to 10, 11 is to proceed to check out."))

        if buys<=10:
            print('You have chosen the ninja',ninja[buys-1])
            
            if ninja[buys-1] in buyguy:
                print('You have already added this guy')
                break
            else:
                buyguy.append(ninja[buys-1])
        elif buys==11:
            print("you have finished your purchases")
            buying=buying+1
        else:
            print('That is not a valid output')

    print('YOUR LIST OF NINJA','AMOUNT SPENT',sep='\t\t')
    tots=0.0
    for hh in range(len(buyguy)):
        ipo=ninja.index(buyguy[hh])
        ut=ryo[ipo]
        tots+=ut
        print(str(hh+1),buyguy[hh],ut,sep='\t\t\t')
    print('The amount you have to pay is',tots)
    time.sleep(2)
    if tots>1000000:
        time.sleep(2)
        print('You have went past the budget. Now, you cannot do the deal. Therefore you lose.')
    else:
        print('You have expended within the budget. Well done.')
        time.sleep(2)
        print('Now, you have to feed your ninja food inorder to rejuvinate him')
        time.sleep(2)
        print('Welcome to the Ramen Store')
        time.sleep(2)
        print()

        menu = ['Tonkutsu Ramen', 'Miso Ramen     ', 'Onigiri        ', 'Dango        ', 'Popsicle     ']
        cost = [99, 109, 79.99, 39.99, 49.99]

        print('ITEM', 'PRICE (RYO), excl. Tax', sep='\t\t\t')
        for oo in range(len(menu)):
            print(str(oo+1)+'. '+menu[oo], cost[oo], sep='\t\t')

        shopping_cart2 = [] 
        shopping_quant2= []
        shopping_complete2 = 0

        while shopping_complete2==0:

            ordering = int(input('Enter 1 to 5 to select an item, 6 to proceed to checkout.\n')) 
    
   
    
            if ordering <= 5:
        
                print('You selected', menu[ordering-1])
                time.sleep(2)
                quant2= int(input('How many units do you wish to purchase?\n'))

        
                if menu[ordering-1] in shopping_cart2:
                    idx1= shopping_cart2.index(menu[ordering-1])
            
                    shopping_quant2[idx1]+=quant2
                else:
                    shopping_cart2.append(menu[ordering-1])        
                    shopping_quant2.append(quant2)        
        
                    print('Added to shopping cart:', quant2, 'units of', menu[ordering-1])
            elif ordering == 6:
                shopping_complete2 = 1
            else: 
                print("Sorry that was not a valid input.")
        




        print()
        print('Your Shopping Cart:')


        grand_tot1 = 0.0
        print('ITEM     ', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
        for zz in range(len(shopping_cart2)):
            idxs= menu.index(shopping_cart2[zz])
            unit_price1=cost[idxs]
            tot_price1 = round(unit_price1*shopping_quant2[zz], 2)
            grand_tot1 += tot_price1
            print(shopping_cart2[zz], shopping_quant2[zz], unit_price1    , tot_price1, sep='\t\t\t')

        grand_tot1 = round(grand_tot1, 2)
        print()
        print('Your total order is (ryo)', grand_tot1)
        if 'Itachi Uchiha' in buyguy:
            time.sleep(2)
            print('You have succesfully passed the forest as you have chosen the very powerful ninja Itachi Uchiha')
            time.sleep(2)
            print('Go to port to see a surprise.')
        elif len(buyguy)>=1 and noo.sum(shopping_quant2)>20:
            if 'Pain' in buyguy:
                time.sleep(2)
                print('You took Pain in your guard, but he betrayed you and killed you.')
            else:
                time.sleep(2)
                print('You have got good ninja and you have rejuvinated them and have passed the forest safely.')
        elif len(buyguy)<=1 and noo.sum(shopping_quant2)>20:
            time.sleep(2)
            print('you failed to buy any ninja and therefore, you got ambushed in the forest and you died.')
        elif len(buyguy)>=1 and noo.sum(shopping_quant2)<20:
            time.sleep(2)
            print('You may have got good ninja, but you have not fed them properly and they died in battle easily and you got kidnapped for ransom.')
        else:
            time.sleep(2)
            print('You effortlessly got killed.')

s=turtle.Turtle()

ts=s.getscreen()
i=turtle.Screen()
i.title("Itachi Mangekyo Sharingan")
i.screensize(600,600)
def draw_line(x0,y0,x1,y1):
    s.penup()
    s.goto(x0,y0)
    s.pendown()
    s.goto(x1,y1)
def draw_rectangle(x0,y0,h,l,c):
    s.fillcolor(c)
    
    s.begin_fill()
    draw_line(x0,y0,x0+l,y0)
    draw_line(x0+l,y0,x0+l,y0+h)
    draw_line(x0+l,y0+h,x0,y0+h)
    draw_line(x0,y0+h,x0,y0)
    s.end_fill()
    

ts.tracer(0)
n_cols=21
x_val=-200
y_val=200

for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<8:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>7 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>15 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=0
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=-200
y_val=-40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=-200
y_val=-80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>11 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
            draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-200
for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20
ts.update()
turtle.mainloop()