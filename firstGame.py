import random 
dic = { 's':1 , 'g':-1 , 'w':0}
dic2 = { 1: 'Snake', -1 : 'Gun', 0 : 'Water'}

chose = input("Enter 's' for snake, 'w' for water and 'g' for gun : ")
cam = random.choice([ 1, -1, 0])

if chose in dic :
    you = dic[chose]
    print(f"You Chose: {dic2[you]}")
    print(f"Computer chose: {dic2[cam]}")

    if you == cam :
        print("It's Drawww !!!! ")

    elif (you == 1 and cam == -1 ) or (you == -1 and cam == 0) :
        print("Computer won the match") 

    elif (you == -1 and cam == 1) or ( you == 0 and cam == -1) : 
        print("You Won the Match!!!!!!!!!")
else : 
    print("Chose Between the 's' 'w' 'g' ")
