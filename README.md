# L'île au Python

## Summary

- [Presentation](#presentation)
- [Prerequisite](#prerequisite)
- [Quests](#quests)
- [Mods](#mods)
- [Contribution](#contribution)

## Presentation

"Python Island" is a console game. You are a lost surivor after your boat sunk. Your goal is to complete 3 quest in order to leave this island:

- [Guess the number](#guess-the-number)
- [Ceasar Code](#ceasar-code)
- [FizzBuzz](#fizzbuzz)

You need to take care of your energy, thirst and food, otherwise you could die. You also have an inventory, in wich you can store food, water bottles or artifacts to help you during your quests.

## Prerequisite

In order for this game to works, and have the best graphical experience you must install the new windows terminal. Indeed, this game use emojis to display the player, palm trees, quests...  You don't *need* to install this console, but if you don't you'll just have squares in place of emojis.

To install the new windows terminal, go to the `windows store` and type `terminal` in the search box. You'll then see the new Windows terminal.

## Quests

There are 3 different quest. Each quest give a special key, necessary to leave the island.

### Guess the number

This game is pretty simple. All you have to do is to guess a number between 0 and 100 three times. You have 20 try to guess the three numbers. Once it's done, you'll get the bronze key.

---

First we get the name of the current file in order to get the story associated with this quest and display it into the right panel. Then we check if there is any mod in the mod folder, and we fetch its data. Next we show the cursor and let the player find the number.

### Ceasar Code

In this game, you'll have to decode a secret message. This will give you the silver key.

### Fizzbuzz

The last quest is random game. In fact, you dont have to do anything, just let the game play for you. You are against a certain number of monkeys and their boss. The goal is to enumerate numbers, starting from 1, and to **fizz** when the number is a multiple of 3, **buzz** if it's a multiple of 5, and **fizzbuzz** if it's both. Otherwise, you just say the number.

## Mods

The most important point of this game is to be "modable". You have a _mod_ folder in wich you can store moded json file. If you want to do it, you **need** to respect the exact same syntax as the main json file stored in the *data* folder.

### To create new quests

If you want to add a new quest, you first need to add its coordinate in a *coordinates.json* file into the *mods* folder. You must copy the *coordinates.json* file in order to add your own coords among the original one. Moreover, you need to specify :

- what kind of mark should your quest be shown as
- what's the name of the folder in wich your file is
- what's the name of the file wich launch the quest

You **need** to have a *main* function into the main file. You can also use the *checkLength* function to create your very own story. To achieve this you can copy the *cinematic.json* file and add your own story. You **need** to give the same name for the cinematic key and your main file.

## Contribution

[@Redshark61](https://github.com/Redshark61)
