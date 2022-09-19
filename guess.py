from random import *

rand_cp = randint(1, 100)
game = False
i = 1
while game == False:
    guess = input("Num : ")
    if int(guess) == rand_cp:
        print(f"{i}번의 기회만에 정답을 맞췄어요!")
        break
    elif int(guess) > rand_cp:
        print("DOWN!")
        i = i + 1
    elif int(guess) < rand_cp:
        print("UP!")
        i = i + 1


