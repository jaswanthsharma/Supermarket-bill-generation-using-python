from datetime import datetime

name = input("enter your name: ")
# list of items

lists = '''
Rice      Rs 20/kg
Sugar     Rs 30/kg
Salt      Rs 20/kg
Oil       Rs 80/liter
Paneer    Rs 110/kg
Maggie    Rs 50/kg
Boost     Rs 90/each
Colgate   Rs 85/each

'''
#declaration

price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# rates of items

items = {'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}

option = int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("enter your items:")
        quantity = int(input("enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(items)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input("can i bill the item yes or no:")
    if inp == 'yes':
        pass
        if finalamount!=0:
            print(25*"=","jaswanth supermarket",25*"=")
            print(28*" ","mothinagar")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')

            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ",'Thanks for visiting')
            print(75*"-")   
            print(50*" ",'Have a good day')
            print(75*"-")











