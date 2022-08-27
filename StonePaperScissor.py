print(">>>>>>>WELCOME TO GAME<<<<<<<")
print(">>>>>>BEST OF LUCK<<<<<<")

your_point = 0
computer_point = 0
draw = 0
n=1
while(n<=10):
    import random
    lst = [1, 2, 3] #1- Stone  2- Paper 3- Scissor
    a = int(random.choice(lst))
    b = int(input("Enter your choice\n 1- Stone\n 2- Paper\n 3- Scissor\n"))
    if b == 1:
        if a == 1:
            print("tie")
            draw += 1
        elif a == 2:
            print("You Loss a round")
            computer_point +=1
        elif a == 3:
            print("You got a point")
            your_point += 1
        else:
            print("invalid")
    elif b == 2:
        if a == 1:
            print("You got a point")
            your_point += 1
        elif a == 2:
            print("tie")
            draw += 1
        elif a == 3:
            print("You Loss a round")
            computer_point +=1
        else:
            print("invalid")
    elif b== 3:
        if a == 1:
            print("You Loss a round")
            computer_point +=1
        elif a == 2:
            print("You got a point")
            your_point += 1
        elif a == 3:
            print("tie")
            draw += 1
        else:
            print("invalid")
    else:
        print("invalid")
    n = n + 1


print("Game over")
print("Your point : ", your_point)
print("Computer Point : ", computer_point)
print("No. of times draw : ", draw)

if your_point > computer_point:
    print("Congrats, You win the Game")
elif computer_point > your_point:
    print("You loss the Game")
else:
    print("Game Draw")
