"""
Numbri äraarvamise mäng
"""
from random import  randint
pc_rand_num = randint(1, 100)  # Juhuslik number
steps = 0  # Mitu sammu äraarvamiseni
game_over = False  # Mäng ei ole läbi
# print(pc_rand_num)  # Testiks. Senikaua kuniks on tagauks valmis ehitatud

def ask():
    global game_over, steps  # Pääseb globaalmuutujatele ligi

    user_num = int(input('Sisesta number 1-100ni: '))
    if user_num > pc_rand_num and user_num != 10000:  # 10000 on TAGAUKS!
        steps += 1  # Pane üks samm lisaks
        print('Väiksem')
    elif user_num < pc_rand_num and user_num != 10000:
        steps += 1
        print('Suurem')
    elif user_num == pc_rand_num and user_num != 10000:
        steps += 1
        game_over = True
        print(f'Juhuu, ära arvasid. Õige vastus oli {pc_rand_num}. Sammude arv {steps}.')
    elif user_num == 10000:
        steps += 1
        print(f'Opaa, leidsid mu nõrga koha. Pssst! Õige vastus on {pc_rand_num}')


def lets_play():
    global game_over, pc_rand_num, steps
    while not game_over:  # For loop ei tööta, sest for loop tahab teada, mitu korda sa mängid
        ask()
    answer = input('Kas mängime veel? [J/E] ')
    if answer.lower() == 'j':
        pc_rand_num = randint(1, 100)  # Genereeri uus number
        steps = 0  # Sammude arv nulli ära
        game_over = False  # Mäng ei ole läbi
        lets_play()  # Käivita mäng uuesti

lets_play()