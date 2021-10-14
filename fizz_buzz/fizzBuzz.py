#coding: utf-8
import os.path
import time
import copy
from random import randint
from fizz_buzz.jsonFetch import jsonFetch
from fizz_buzz.setTurn import setTurn
from functions.Colors import Colors
from functions.Position import position, clearBoxWithLine, clearBox
from functions.checkLength import checkLength
from fizz_buzz import configFizzBuzz as conf
from fizz_buzz.checkChances import checkChances


def main() -> None:
    conf.numberMonkeys, conf.chance = 0, 0
    conf.playerLeft, conf.turnData = [], []
    conf.index, conf.turn = '', ''
    conf.isPlayerWrong = False

    # Permettre l'affichage des couleurs
    color = Colors()
    color.init()
    # color.colorBgEnd

    fileName = os.path.basename(__file__)[:-3]
    text = checkLength(fileName)

    for index, line in enumerate(text):
        print(position(105, 4+index+1, line), flush=True)
        time.sleep(0.2)

    clearBox()

    # Vérifier la présence d'un mod
    maxMonkey, minMonkey, maxBoss, minBoss, maxPlayer, minPlayer, data = jsonFetch()

    # Les chances sont attribué aléatoirement entre le max et le min défini dans le json
    chanceMonkey = randint(minMonkey, maxMonkey+1)
    chanceBoss = randint(minBoss, maxBoss+1)
    chancePlayer = randint(minPlayer, maxPlayer+1)

    n = 1

    # Établissement de l'ordre de passage : une liste qui contient la liste du pourcentage de chance de victoire pour chaque joueur
    # Il y a d'abord tout les singes, puis le chefs en -2, et le joueur en -1

    turns = {}
    for i in range(data['monkeys']['number']):
        turns['singe'+str(i)] = chanceMonkey
    turns['boss'] = chanceBoss
    turns['joueur'] = chancePlayer

    # Le nombre de joueur restant DOIT être une deepcopy
    # En effet la liste turns est modifié au fur et à mesure des éliminations,
    # mais on doit continuer d'itérer à travers elle pour que tout le monde joue au moins une fois
    conf.playerLeft = copy.deepcopy(turns)
    conf.isPlayerWrong = False
    line = -4
    while conf.numberMonkeys > 0 and not conf.isPlayerWrong:

        for conf.index, conf.chance in turns.items():
            time.sleep(1)

            line = clearBoxWithLine(line, 4)
            print("\033[40m")
            setTurn(data, line)

            # Si c'est FizzBuzz
            if n % 3 == 0 and n % 5 == 0:
                hasFail = checkChances(line, color, 'winFizzBuzz')

                # Si le nombre random est dans l'interval de conf.chance, alors victoire
            elif n % 3 == 0:
                hasFail = checkChances(line, color, 'winFizz')

            elif n % 5 == 0:
                hasFail = checkChances(line, color, 'winBuzz')

            else:
                hasFail = checkChances(line, color, 'play', n)

            if hasFail:
                break
            print(position(x=105, y=5+line, text=f"Il reste {conf.numberMonkeys} singes"))
            n += 1
        # On met à jour les tours des joueurs
        turns = copy.deepcopy(conf.playerLeft)

    if conf.numberMonkeys == 0:
        print(position(x=105, y=5+line, text=color.setForeground('brightGreen', 'Tous les singes ont été éliminé ! Tu as gagné !')))
        return True
    print(position(x=105, y=5+line, text=color.setForeground('red', "Tu as perdu !")))
    time.sleep(2)
    return False
