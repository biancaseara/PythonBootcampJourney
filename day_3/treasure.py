print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure!\nYour mission is find the treasure.')

print('BTS is currently on a world tour and you have just purchased tickets to one of their concerts. However, before you can attend the concert, you must overcome a series of obstacles and challenges.')

city = input('The first clue to finding the treasure lies in one of two cities: Rio de Janeiro or Mexico City. Which one will you choose to start your quest?\n').lower()

if city == 'rio de janeiro':
    right = input('\nYou stand in awe next to the towering Christ statue, marveling at its grandeur. To your left lies the breathtaking beach, beckoning you to explore its sandy shores. Which way will you go? Type "L" to head towards the beach or "R"" to venture further on your treasure hunt.\n').lower()
    if right == 'r':
        yellow = input("\nYou've arrived at the bus stop, eager to continue your quest for treasure. Three buses await you, each headed to the beach. Which one will you choose based on its color? Will it be the shimmering GOLD, the bright YELLOW, or the bold ORANGE? The choice is yours. Make it wisely and let the adventure continue!\n").lower()
        if yellow == 'yellow':
            go_go = input("\nThe sound of crashing waves fills your ears as you arrive at the sun-drenched beach. You notice three quiosques, each with a different song blaring from its speakers. Will you follow the soulful beats of 'Blood Sweat and Tears,' the upbeat rhythm of 'Go Go,' or the fiery melody of 'Fire?' Choose your path wisely, adventurer, for it could lead you one step closer to the treasure you seek.\n").lower()
            if go_go == 'go go':
                food = input("\nYou're so close to your destination, adventurer! Before you can claim your treasure, you must choose your path wisely. Will you indulge in a delectable FOOD TOUR, exploring the local cuisine and savoring each bite? Or will you opt for a fascinating CITY TOUR, immersing yourself in the history and culture of this vibrant place? The choice is yours, but choose carefully, as it could lead you one step closer to unlocking the treasure's location.\n").lower()
                if food == 'food tour':
                    print("\nCongratulations, adventurer! You've made it to the treasure concert. Sit back, relax, and enjoy the soulful vocals of the boys as they take the stage. You've earned this moment of rest and celebration after all your hard work. Let the music wash over you and bask in the glory of your triumph!\n")
                else:
                    print("\nAlas, adventurer! It seems you've been led astray from the treasure concert. Your quest has come to an end, and it's game over for now. But fear not, for with determination and perseverance, you can always try again and perhaps uncover the treasure's location on your next adventure. Keep exploring, and may luck be on your side!")
            elif go_go == 'Fire' or go_go == 'FIRE' or go_go == 'fire':
                print("\nOh no, adventurer! It seems you've stumbled into the wrong quiosque, and it's engulfed in flames. Your quest has come to an unfortunate end, and it's game over for now. But don't lose hope, for with perseverance and a bit of luck, you can always try again and perhaps uncover the treasure's location on your next adventure. Stay vigilant and stay safe, and let the treasure hunt continue!")
            else:
                print("\nOh no, adventurer! It seems you've stumbled into a quiosque drenched in blood. Your quest has come to a gruesome end, and it's game over for now. But don't give up hope, for with persistence and a bit of luck, you can always try again and perhaps uncover the treasure's location on your next adventure. Stay alert and stay focused, and let the treasure hunt continue!")
        else:
            print("\nAlas, adventurer! It seems you will arrive far away from the treasure concert. Your quest has come to an end, and it's game over for now. But don't despair, for with determination and a bit of luck, you can always try again and perhaps uncover the treasure's location on your next adventure. Keep exploring and stay focused, and may the treasure be yours in the end!")
    else:
        print("\nOh no, adventurer! It seems you've gotten stuck in the midst of a crowded space, unable to move forward. Your quest has come to a halt, and it's game over for now. But don't lose heart, for with persistence and a bit of luck, you can always try again and perhaps uncover the treasure's location on your next adventure. Keep a sharp eye and stay nimble, and let the treasure hunt continue!")

else:
    left = input("\nYou've arrived at the Frida Kahlo Museum, a place of wonder and beauty. Now it's time to make a choice. Will you move forward with your quest and type L, or will you pause for a moment and wait, typing R? Remember, every decision can bring you closer to the treasure's location, so choose wisely and let the adventure continue!\n").lower()
    if left == 'l':
        gold = input("\nAhoy, adventurer! You find yourself standing in front of three magnificent doors, each adorned with a vibrant color. Will you choose the sunny YELLOW door, the fiery ORANGE door, or the sparkling GOLDen door? Remember, every choice can lead you closer to the treasure's location, so choose with care and let the adventure begin!\n").lower()
        if gold == 'gold':
            go_go = input("\nBravo, adventurer! You've entered a wondrous door, revealing three stunning galleries, each filled with a different song. Will you follow the passionate beats of 'Fire,' the soulful lyrics of 'Blood Sweat and Tears,' or the upbeat rhythm of 'Go Go'? Every choice can bring you closer to the treasure's location, so listen closely and let the adventure continue!\n").lower()
            if go_go == 'go go':
                food = input("\nYou're so close to your destination, adventurer! Before you can claim your treasure, you must choose your path wisely. Will you indulge in a delectable FOOD TOUR, exploring the local cuisine and savoring each bite? Or will you opt for a fascinating CITY TOUR, immersing yourself in the history and culture of this vibrant place? The choice is yours, but choose carefully, as it could lead you one step closer to unlocking the treasure's location.\n").lower()
                if food == 'food tour':
                    print("\nCongratulations, adventurer! You've made it to the treasure concert. Sit back, relax, and enjoy the soulful vocals of the boys as they take the stage. You've earned this moment of rest and celebration after all your hard work. Let the music wash over you and bask in the glory of your triumph!\n")
            elif go_go == 'fire':
                print("\nAs you step through the gallerie, you're met with intense heat and flames. It's too dangerous to continue, and your journey comes to an end. Game over!")
            else:
                print("\nThe gallerie you've entered is dimly lit, and you can see bloodstains on the walls. It's too eerie and unsettling to continue, and your quest comes to an end. Game over!")
        else:
            print("\nOh no, adventurer! As you enter the door, you suddenly find yourself stuck, unable to move forward or backward. Your quest comes to an unfortunate end. Game over! Remember, every door and every step can hold a surprise in this adventure. So stay alert and let the quest continue!")
    else:
        print("\nAlas, adventurer! You chose to wait, and as time passes, you realize that you've lost your way. The path that could have led you to the concert is no longer visible, and your quest comes to an end. Game over! Remember, every decision counts, and every second can make a difference in this adventure. So choose carefully and let the quest continue!")
        
    