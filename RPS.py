c=1;
while c==1:
    print("enter 1 for Rock, 2 for Paper and 3 for Scissors")
    p1=int(input("1. enter your input"))
    p2=int(input("2. enter your input"))
    if (p1==1 and p2==3)or(p1==3 and p2==2)or(p1==2 and p2==1):
        print("player 1 wins!")
    elif(p1==p2):
        print("draw")
    else:
        print("player 2 wins!")
    c=int(input("to play another game press 1"))

    
