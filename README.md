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
- [How to make Mods](#mods)
- [Usefull Functions](#functions)
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

### Fizzbuzz

The last quest is random game. In fact, you dont have to do anything, just let the game play for you. You are against a certain number of monkeys and their boss. The goal is to enumerate numbers, starting from 1, and to say **fizz** when the number is a multiple of 3, **buzz** if it's a multiple of 5, and **fizzbuzz** if it's both. Otherwise, you just say the number.

## The map and graphical element

All the elements related to the map / animations are in the *map* folder.

### Wich colors are supported

This is the list of the colors and there code:

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

The map folder also contain the code to display the final trailer.

## Mods

The most important point of this game is to be "modable". You have a _mod_ folder in wich you can store moded json file. If you want to do it, you **need** to respect the exact same syntax as the main json file stored in the _data_ folder.

All what's inside the *data* folder can be modified, just copy it in order not to delete the basic file. If you want to do it you must place your new file into the *mod* folder.

- [To create new quests](#to-create-new-quests)
- [To add new items](#to-add-new-items)
- ["Change the value of an existing quest"](#change-the-value-of-an-existing-quest)
- ["Add new skin"](#add-new-skin)
- ["Modify a story"](#modify-a-story)

### To create new quests

If you want to add a new quest, you first need to add its coordinate in a _coordinates.json_ file into the _mods_ folder. You must copy the _coordinates.json_ file in order to add your own coords among the original one. Moreover, you need to specify:

- what kind of mark should your quest be shown as
- what's the name of the folder in wich your file is
- what's the name of the file wich launch the quest

You **need** to have a `main` function into the main file. You can also use the _checkLength_ function to create your own story. To achieve this you can copy the _cinematic.json_ file and add your own story. You **need** to give the same name for the cinematic key and your main file.

### To add new items

Copy *items.json* inside the *data* folder. You can any items you want. It must be a food type (it can be eaten). Specify:

- number: how much do want to spawn on the map
- name: the real name of the item,
- type: tell if it's *food* or *liquid*,
- nutrition: tell how many point it gives (how many water if it's *liquid* or food if it's *food*),
- spawn: always generic,
- mark: the hexadecimal value of your emoji,
- size: the size of the item in the inventory

### Change the value of an existing quest

Copy the json file of the quest you want to change and paste it into the *mod* folder. You can just change the value as what you want.

### Add new skin

Same as [add new Item](#to-add-new-items).

### Modify a story

Same as ["Change the value of an existing quest"](#change-the-value-of-an-existing-quest).

## Functions

This folder contain all the functions used throughout the game and you can reuse. The most important ones are:

- [checkLength](#checkLength)
- [emojiDecoder](#emojiDecoder)
- [Clear](#clear)
- [Position](#position)
- [Colors](#colors)

### checkLength

This function takes *one parameter*: the name of the file wich runs it.

*It returns a list* of all the sentences.

Its use is to get the story / dialog associated to this game. In order for this function to work, you must **set the same name** for the main file wich run the function as well as in the json wich store all the stories.

### emojiDecoder

In this function you pass the *hexadecimal* value of your emoji, and get a str value that you can print wherever you want.

### Clear

This function just clear the screen.

### Position

In this file you have multiple functions. The most important ones are the [position](https://github.com/Redshark61/Python-Island/blob/d7492f0682e9e5460898d53bfe75abca291a4271/functions/Position.py#L1) and [printBox](https://github.com/Redshark61/Python-Island/blob/d7492f0682e9e5460898d53bfe75abca291a4271/functions/Position.py#L8). Go check them if you need, they are pretty self-explanatoring.

### Colors

This class enables you to use colors. You use this class for your own use. If you want so, you should *first use the init() function*. It just clear the buffer of the console. Otherwise you might see strange characters instead of colors.

## Contribution

[@Redshark61](https://github.com/Redshark61)
