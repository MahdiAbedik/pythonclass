import random


print("sang...")
print("kaghaz...")
print("gheychi...")

player1 = input("player1 , lotfan harekat khod ra entekhab konid :").lower()
randomnumber = random.randint(1, 3)


if player1 == player2 :
    print("mosavi")
elif player1 == "sang" and player2 == "kaghaz":
    print("player2 win")    
elif player1 == "sang" and player2 == "gheychi":
    print("player1 win")
elif player1 == "kaghaz" and player2 == "sang":
    print("player1 win")
elif player1 == "kaghaz" and player2 == "gheychi":
    print("player2 win")
elif player1 == "gheychi" and player2 == "sang":
    print("player2 win")
elif player1 == "gheychi" and player2 == "kaghaz":\
    print("player1 win")
else:
    print("ye chizi eshtebahe!")

