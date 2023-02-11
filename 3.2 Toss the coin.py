# Монета
# Симулятор подбрасывания монеты 100 раз. Программа сообщает, сколько раз выпали орел и решка.
# Created by Luero, 22.04.2022

import random
print ('Подбрасываем монету 100 раз')
toss = 1
orel = 0
reshka = 0
while toss <=100:
    toss +=1
    coin = random.randint (1,2)
    if coin == 1:
        orel +=1
    elif coin == 2:
        reshka +=1
    else:
        print ('Something goes wrong')
print ('Орел выпал ', orel, 'раз. Решка выпала', reshka, 'раз')
input ('\n\nPress Enter to escape')
