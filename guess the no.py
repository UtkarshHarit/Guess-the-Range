import random
def funName(a,randomno):
    
    ranplus=randomno+10
    ranminus=randomno-10
    
    if(a<=ranplus and a>=ranminus):
        print("congratulations!!!!!!! Your no is in range our no is %d" %randomno)
    elif(a<ranminus):
        print("Wrong answer")
        print("Your guessed no is too low")
        x=input("Input 'y' to try again......")
        return x
    elif(a>ranplus):
        print("wrong answer")
        print("Your guessed no is too high")
        x=input("Input 'y' to try again......")
        return x




print('''
Welcome!!!
we have alredy have choosen a number you have to guess our number(up down range 10 will be considered)
so lets get started!!!!!!
''')
randomno=random.randint(1,100)
x='y'
while(x=='y'):
    choose=int(input("choose a no from 0 to 100: "))
    if(choose>0 and choose<101):
        x=funName(choose,randomno)
    else:
        print("your number is not in range...")
