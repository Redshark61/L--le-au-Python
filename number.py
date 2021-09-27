from random import randint

answer = ''
rand = randint(0, 100)
print(rand)

while(answer != rand):
    answer = int(input('Quel est mon nombre ? \n'))

    if(answer < rand):
        print("Mon nombre est plus grand")
    elif(answer > rand):
        print("Mon nombre est plus petit")
    else:
        print("Tu as gagné !")
