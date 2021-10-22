# L'île au Python

## Summary

- [Presentation](#presentation)
- [Prerequisite](#prerequisite)
- [Installation](#installation)
- [Quests](#quests)
  - [Guess the number](#guess-the-number)
  - [Fizzbuzz](#fizzbuzz)
  - [Ceasar Code](#ceasar-code)
- [The map and graphical element](#the-map-and-graphical-element)
- [End and credits](#end-and-credits)
- [Mods](#mods)
  - [How to create new quests](#to-create-new-quests)
- [Functions](#functions)
  - [checkLength](#checkLength)
  - [checkMod](#checkMod)
- [Contribution](#contribution)

## Presentation

"Python Island" is a console game. You are a lost surivor after your boat sunk. Your goal is to complete 3 quest in order to leave this island:

- [Guess the number](#guess-the-number)
- [Ceasar Code](#ceasar-code)
- [FizzBuzz](#fizzbuzz)

You need to take care of your energy, thirst and food, otherwise you could die. You also have an inventory, in wich you can store food, water bottles or artifacts to help you during your quests.

![Introduction](https://github.com/Redshark61/Python-Island/blob/master/img/intro.png?raw=true)
![Middle of the game](https://github.com/Redshark61/Python-Island/blob/master/img/milieu.png?raw=true)

## Prerequisite

- The new windows terminal, just click on [this link](https://www.microsoft.com/fr-fr/p/windows-terminal/9n0dx20hk701#activetab=pivot:overviewtab) to download it from the windows store
- Python 3.10

## Installation

Just download all the folder and launch the main.py file.

## Quests

There are 3 different quest. Each quest give a special key, necessary to leave the island.

### Guess the number

This game is pretty simple. All you have to do is to guess a number between 0 and 100 three times. You have 20 try to guess the three numbers. Once it's done, you'll get the bronze key.

There is nothing fancy to say about this game.

### Ceasar Code

In this game, you'll have to decode a secret message. This will give you the silver key.

- **cesar** : this file is main one, it choose a random word as key to encrypt the code, and chenck the input of the player
- **decode** : this file take as parameter the coded sentence, the code you want to use in order to decode the sentence, and the alphabet. It returns the decoded sentence.
- **encode** : this file does the exact opposite : you give the sentence you want to encode, the code and the alphabet and it returns the coded sentence.

### Fizzbuzz

The last quest is random game. In fact, you dont have to do anything, just let the game play for you. You are against a certain number of monkeys and their boss. The goal is to enumerate numbers, starting from 1, and to say **fizz** when the number is a multiple of 3, **buzz** if it's a multiple of 5, and **fizzbuzz** if it's both. Otherwise, you just say the number.

- **fizzBuzz** : it uses all the next functions to display stuff and configure all the chances
- **checkChances** : this function just return a bool wich tell if the function needs to stop (because there are no monkeys anymore or the player failed)
- **configFizzBuzz** : this file just store the important data for the fizzbuzz
- **deletePlayer** : this file delete the player wich failed. It returns *True* if there is a reason for the program to stop (no more monkeys or the player failed). Otherwise it just returns *False*.
- **jsonFetch** : just get all the data from the json and returns it.
- **setTurn** : set the turn in order to know who is currently playing.

## The map and graphical element

All the elements related to the map / animations are in the *map* folder. I won't explain everything, this folder is too heavy, but I'll explain the main part :

- **displayMap** : thif file draw the map. In fact it loops over all the collumns, then the row of a json containing the elements of the map. If the current row and collumn is the same as an element (the player, an item, a tree, a quest...) the cell is not empty but it's another character. It's very easy then to add element on the map.
- **getKeyPress** : it handle all the keypress using the *msvcrt* module from microsoft to read the keyboard input without typing *enter* everytime.
- **inventory** : this file work with the inventory. You can move the arrow, and eat elements.
- **mapBackground** : this is the file wich create the map, with all the colors, and emojies. If you want to use other colors than the current ones, it's this file you must modify.
- **mapLoop** : it's the hub, where all the other file are used.

### Wich colors are supported

This is the list of the colors and there code :

1. dark grey (stone)
2. bright cyan (river)
3. dark blue (sea)
4. bright yellow (sand)
5. palm tree (emoji)
6. dark green (ground)
7. bridge on the river (brown square on blue background)
8. dark yellow (lava)
9. lock (end of the game)
10. bridge on lava (brown square on dark yellow background, hidden when you don't have all the keys)

## End and credits

The map folder also contain the code to display the final trailer

## Mods

The most important point of this game is to be "modable". You have a _mod_ folder in wich you can store moded json file. If you want to do it, you **need** to respect the exact same syntax as the main json file stored in the _data_ folder.

All what's inside the *data* folder  (the json can be modified). If you want to do it you must place your new file into the *mod* folder.

### To create new quests

If you want to add a new quest, you first need to add its coordinate in a _coordinates.json_ file into the _mods_ folder. You must copy the _coordinates.json_ file in order to add your own coords among the original one. Moreover, you need to specify :

- what kind of mark should your quest be shown as
- what's the name of the folder in wich your file is
- what's the name of the file wich launch the quest

You **need** to have a _main_ function into the main file. You can also use the _checkLength_ function to create your own story. To achieve this you can copy the _cinematic.json_ file and add your own story. You **need** to give the same name for the cinematic key and your main file.

## Functions

This folder contain all the functions used throughout the game.

- [checkLength](#checkLength)
- [checkMod](#checkMod)
- [Colors](#colors)

### checkLength

This function takes *one parameter* : the name of the file wich runs it.

*It returns a list* of all the sentences.

Its use is to get the story / dialog associated to this game. In order for this function to work, you must **set the same name** for the main file wich run the function as well as in the json wich store all the stories.

### checkMod

This function takes *one parameter* : the name of the json file we want to read.

*It returns the json* as a list or a dict.

Its use is to get the json file required, but check first if this file already existed as a mod. In order for this function to work, you must set **the same name** for your moded json file as the original one. You also must **copy the original one**, or all the basic data won't be red.

### Colors

This class enables you to use colors. You use this class for your own use. If you want so, you should *first use the init() function*. It just clear the buffer of the console. Otherwise you might see strange characters instead of colors.

## Contribution

[@Redshark61](https://github.com/Redshark61)
