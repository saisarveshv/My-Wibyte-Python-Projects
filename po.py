print('Welcome to the WiByte Bakery')
print()

menu = ['Milkshake', 'Ice Cream', 'Chocolate', 'Eclairs  ', 'CupCake  ']
price = [99.99, 120.99, 89.99, 37.99, 51.99]

print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
for kk in range(len(menu)):
    print(str(kk+1)+'. '+menu[kk], price[kk], sep='\t\t')

shopping_cart = [] 
shopping_quant= []
shopping_complete = 0

while shopping_complete==0:

    order = int(input('Enter 1 to 5 to select an item, 6 to proceed to checkout.\n')) 
    
   
    
    if order <= 5:
        # User wants to purchase something.
        print('You selected', menu[order-1])
        quant = int(input('How many units do you wish to purchase?\n'))

        # Add the item to the shopping cart. 
        # List 1: Shopping Cart items
        # List 2: Quantity
        if menu[order-1] in shopping_cart:
            idx = shopping_cart.index(menu[order-1])
            
            shopping_quant[idx]+=quant
        else:
            shopping_cart.append(menu[order-1])        
            shopping_quant.append(quant)        
        
        print('Added to shopping cart:', quant, 'units of', menu[order-1])
    elif order == 6:
        shopping_complete = 1
    else: 
        print("Sorry that was not a valid input.")
        



        
# Show the shopping cart. 

print()
print('Your Shopping Cart:')

# Separate the number. 
# Give title to the shopping cart. 
# Add the price of every item in the shopping cart, and also the total. 
grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

grand_tot = round(grand_tot, 2)
print()
print('Your total order is (INR)', grand_tot)
print(idx)


buying_item=[]
    itemcost=[]
    shopping_complete=0

    while shopping_complete==0:
        order=int(input('Enter 1 to 5 to select a player.'))


        if order<=5:
            print('You have selected player',batterlist[order-1])
            buying_item.append(batterlist[order-1])
            itemcost.append(price[order-1])
            shopping_complete=shopping_complete+1
        else:
            print('invalid input')

    print("Next you have the choose your all-rounder")       
    all_round=['Hardik Pandya     ','Ravindra Jadeja'  ,'Axar Patel      ','Sunil Narine    ','Shivam Dube     ']
    prices=[20,18,13,16,8]
    print('PLAYER(ALL-ROUNDER)','PRICE(IN CRORE)',sep='\t\t\t')
    for ll in range(len(all_round)):
        print(str(ll+1)+'. '+all_round[ll],prices[ll],sep='\t\t\t')

    
    shoping=0

    while shoping==0:
        orde=int(input("enter 1 to 5 to select a player"))
        if orde<=5:
            print('You have chosen',all_round[orde-1])
            buying_item.append(all_round[orde-1])
            itemcost.append(prices[orde-1])
            shoping=shoping+1
        else:
            print('Invalid player')


    print('Next you have to buy a bowler')
    bowler=['Bumrah        ','Siraj        ', 'Kuldeep Yadav ','Starc          ','Harshit Rana  ']
    pricess=[20,18,13,16,8]
    print('PLAYER(BOWLER)','PRICE(IN CRORE)',sep='\t\t\t')
    for bb in range(len(bowler)):
        print(str(bb+1)+'. '+bowler[bb],pricess[bb],sep='\t\t')
    
    
    shopingg=0
    
    while shopingg==0:
        orders=int(input("enter 1 to 5 to select a player"))
        if orders<=5:
            print('You have chosen',all_round[orde-1])
            buying_item.append(bowler[orders-1])
            itemcost.append(pricess[orders-1])
            shopingg=shopingg+1
        else:
            print('Invalid player')


    print("now you have to choose your two substitutes")
    print("You will have a choice of ten players to choose from")
    subs=['Sanju Samson   ','Devdutt Padikkal','Tilak Varma   ','Sai Sudharshan','Romario Shepherd','Corbin Bosch   ','Khaleel Ahmed','Bhuvneshwar Kumar','Varun Chakravarty','Mohammad Shami']
    pricesy=[15,11,17,9,2,1,4,10,5,8]
    print('PLAYER NAME(SUB)','PRICE(IN CRORES)',sep='\t\t\t')
    for ss in range(len(subs)):
        print(str(ss+1)+'. '+subs[ss],pricesy[ss],sep='\t\t\t')

    shopsy=0

    while shopsy==0:

        ordersss=int(input("choose two players and enter number between 1 to 10,11 to finish"))
        if ordersss<=10:
            print("You have chosen",subs[ordersss-1])
            buying_item.append(subs[ordersss-1])
            itemcost.append(pricesy[ordersss-1])
        elif ordersss==11:
            print('You have finished your purchases')
            shopsy=shopsy+1
    if len(buying_item)>5 or len(buying_item)<5:
        print('You are eliminated')
    else:

 print('You have finished creating your team')
        print("Your players are as follows:")
        print('PLAYER','COST(IN CRORES)',sep='\t\t\t')
        idx = batterlist.index(buying_item[kk])
        idxs=all_round.index(buying_item[ll])
        idxz=bowler.index(buying_item(bb))
        idfe=subs.index(buying_item[ss])
        p=price[idx]
        q=prices[idxs]
        r=pricess[idxz]
        s=pricesy[idfe]
        grandtot=p+q+r+s
        for pp in range(5):
            print(buying_item[pp],itemcost[pp],sep='\t\t\t')


        print("Your total cost for buying all players is",grandtot)
        if grandtot>100:
            print('You have expended over the budget. Therefore you are eliminated')
        else:
            print('As you have expended under the budget, you can continue')