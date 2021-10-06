#coding: utf-8
import json
from random import randint
from fizz_buzz.setTurn import setTurn
import os.path
import copy
from functions.Colors import Colors
from functions.Position import *
from fizz_buzz.deletePlayer import deletePlayer
import time


def main() -> None:
    # Permettre l'affichage des couleurs
    color = Colors
    color.init()
    color.colorBgEnd

    # Vérifier la présence d'un mod
    if os.path.isfile("mods/fizzBuzz.json"):
        with open('mods/fizzBuzz.json') as file:
            data = json.load(file)
    else:
        with open("data/fizzBuzz.json") as file:
            data = json.load(file)

    # Mise en place des variables de base
    numberMonkeys = data["monkeys"]["number"] + 1

    maxMonkey = data["monkeys"]["maxChance"]
    minMonkey = data["monkeys"]["minChance"]

    maxBoss = data["boss"]["maxChance"]
    minBoss = data["boss"]["minChance"]

    maxPlayer = data["player"]["maxChance"]
    minPlayer = data["player"]["minChance"]

    # Les chances sont attribué aléatoirement entre le max et le min défini dans le json
    chanceMonkey = randint(minMonkey, maxMonkey+1)
    chanceBoss = randint(minBoss, maxBoss+1)
    chancePlayer = randint(minPlayer, maxPlayer+1)

    n = 1
    isPlayerWrong = False

    # Établissement de l'ordre de passage : une liste qui contient la liste du pourcentage de chance de victoire pour chaque joueur
    # Il y a d'abord tout les singes, puis le chefs en -2, et le joueur en -1
    # turns = [chanceMonkey]*(data['monkeys']['number']) + [chanceBoss, chancePlayer]
    turns = {}
    for i in range(data['monkeys']['number']+1):
        turns['singe'+str(i)] = chanceMonkey
    turns['boss'] = chanceBoss
    turns['joueur'] = chancePlayer

    # Le nombre de joueur restant DOIT être une deepcopy
    # En effet la liste turns est modifié au fur et à mesure des éliminations,
    # mais on doit continuer d'itérer à travers elle pour que tout le monde joue au moins une fois
    playerLeft = copy.deepcopy(turns)
    line = -4
    while numberMonkeys > 0 and not isPlayerWrong:

        for index, chance in turns.items():
            time.sleep(1)

            line = clearBox(line, 4)
            print("\033[40m")
            turnData, turn = setTurn(index, data, line)

            # Si c'est FizzBuzz
            if n % 3 == 0 and n % 5 == 0:
                # Si le nombre random est dans l'interval de chance, alors victoire
                if randint(0, 100) < chance:
                    print(position(x=105, y=4+line, text=color.setForeground('brightCyan', turnData["winFizz"] + turnData["winBuzz"])))
                # Sinon défaite
                else:
                    print(position(x=105, y=4+line, text=color.setForeground('red', turnData['loose'])))
                    isPlayerWrong, playerLeft, numberMonkeys = deletePlayer(index, turn, playerLeft, numberMonkeys, isPlayerWrong)
                    if isPlayerWrong:
                        break

            elif n % 3 == 0:
                if randint(0, 100) < chance:
                    print(position(x=105, y=4+line, text=color.setForeground('brightCyan', turnData["winFizz"])))
                else:
                    print(position(x=105, y=4+line, text=color.setForeground('red', turnData['loose'])))
                    isPlayerWrong, playerLeft, numberMonkeys = deletePlayer(index, turn, playerLeft, numberMonkeys, isPlayerWrong)
                    if isPlayerWrong:
                        break

            elif n % 5 == 0:
                if randint(0, 100) < chance:
                    print(position(x=105, y=4+line, text=color.setForeground('brightCyan', turnData["winBuzz"])))
                else:
                    print(position(x=105, y=4+line, text=color.setForeground('red', turnData['loose'])))
                    isPlayerWrong, playerLeft, numberMonkeys = deletePlayer(index, turn, playerLeft, numberMonkeys, isPlayerWrong)
                    if isPlayerWrong:
                        break

            else:
                if randint(0, 100) < chance:
                    print(position(x=105, y=4+line, text=color.setForeground('brightYellow', turnData['play'] + str(n) + "\n")))
                else:
                    print(position(x=105, y=4+line, text=color.setForeground('red', turnData['loose'])))
                    isPlayerWrong, playerLeft, numberMonkeys = deletePlayer(index, turn, playerLeft, numberMonkeys, isPlayerWrong)
                    if isPlayerWrong:
                        break

            print(position(x=105, y=5+line, text=f"Il reste {numberMonkeys} singes"))
            n += 1
        # On met à jour les tours des joueurs
        turns = copy.deepcopy(playerLeft)

    if numberMonkeys == 0:
        print(position(x=105, y=5+line, text=color.setForeground('brightGreen', 'Tous les singes ont été éliminé ! Tu as gagné !')))
        return True
    else:
        print(position(x=105, y=5+line, text=color.setForeground('red', "Tu as perdu !")))
        return False
