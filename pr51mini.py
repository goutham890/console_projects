x = []
y = input("enter customer name :")
z = int(input("number of tickets :"))
for i in range(z):
    m = input("enter the tickets :")
    if m not in x:
        x.append(m)
while(True):
    print("1 - view booked seats ")
    print("2 - book new seats ")
    print("3 - cancel seat ")
    print("4 - search seat")
    print("5 - exit")
    print("************************")
    O = int(input("choose an option :"))
    if(O == 1):
        print(x)
    elif(O == 2):
        n = input("enter the new seats :")
        if n not in x:
            x.append(n)
        else:
            print("the tickect already booked")
    elif(O == 3):
        B = input("enter the seat to remove :")
        if B in x:
            x.remove(B)
        else:
            print("seat not exist")
    elif(O == 4):
        V = input("enter the seat to search :")
        fount = False
        for i in range(len(x)):
            if(x[i] == V):
                print("seat occupied ")
                fount = True
                break
        if(fount == False):
            print("seat is not occupied :")
            break
    elif(O == 5):
        break