 # Steven Bui       10/30/2022
 # COM S 127         Assignment 4

import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999




# Functions to represent dungeon rooms
# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room1(goldAmount, visited_room, Health):
   
    if visited_room == False:
        gold = 10 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print('this is the entrance room')
        print()


    direction = input("[n] [e] [w]?: ")
    while direction != "n" and direction != "e" and direction != "w":
        print("Invalid input...")
        direction = input("[n] [e] [w]?: ")
    
    roomChoice = -1 # HINT: Once this section is encapsulated into a function, it would be wise to have a default roomChoice value outside that function.
    if direction == "n":
        roomChoice = 2
    elif direction == "e":
        roomChoice = 3
    elif direction == "w":
        roomChoice = 4
    
    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room, Health

# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room2(goldAmount, visited_room, Health):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print('Player Health:',Health)
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()
        print('.......AMBUSH')
        fight(Health)
        

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = 2
    if direction == "n":
        roomChoice = 5 # THIS IS WHAT IS THE LAST ROOM
    elif direction == "s":
        roomChoice = 1

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room, Health

def room3(goldAmount, visited_room, Health):
    if visited_room == False:
        gold = 15 # This is the amount of gold the room contains.
    
        print()
        print("The room has", gold, "gold pieces in it...")
        
    
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()
        story()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    direction = input("[w]?: ")
    while direction != "w" :
        print("Invalid input...")
        direction = input("[w]?: ")
    
    roomChoice = 3
    if direction == "w":
        roomChoice = 1 
    return roomChoice, goldAmount, visited_room, Health

def room4(goldAmount, visited_room, Health):
    if visited_room == False:
        gold = 15 # This is the amount of gold the room contains.
    
        print()
        print("The room has", gold, "gold pieces in it...")
        
    
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        shop(Health, goldAmount)
        story()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
        shop(Health,goldAmount)
    direction = input("[e]: ")
    while direction != "e":
        print("Invalid input...")
        direction = input("[e]?: ")
    
    roomChoice = 4
    if direction == "e":
        roomChoice = 1 
    return roomChoice, goldAmount, visited_room,Health

def room5(goldAmount, visited_room, Health):
    if visited_room == False:
        gold = 15 # This is the amount of gold the room contains.
    
        print()
        print('Player Health;',Health)
        print("The room has", gold, "gold pieces in it...")
        
    
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = 5
    if direction == "n":
        roomChoice = FINAL_ROOM # THIS IS WHAT IS THE LAST ROOM
    elif direction == "s":
        roomChoice = 2
    return roomChoice, goldAmount, visited_room, Health


#combat system
def fight(Health):

    Enemy = 50
    while Enemy > 0:
        
        print('Enemy Health:',Enemy)
        print('Player Health:',Health)
        userAttack = input('[l]ight attack, [h]eavy attack: ')
        while userAttack != "l" and userAttack != 'h' :
            print("Invalid input...")
            userAttack = input('[l]ight attack, [h]eavy attack: ')
        if userAttack == 'l':
            chance = random.randrange(1,10)
            if chance > 2:
                Enemy = Enemy - 10
                print('Attack Hit!\nEnemy health:',Enemy)
                print()
  
            elif chance <= 2:
                print('Attack Missed!')
                print()
        if userAttack == 'h':
            chance = random.randrange(1,10)
            if chance >5:
                Enemy = Enemy -25
                print('Attack Hit!\nEnemy Health:',Enemy)
                print()
            if chance <=5:
                print('Attack Missed!')
                print()

        if Enemy <= 0:
            break
            
        EnemyTurn = input('[d]odge, [c]ounter: ')
        if EnemyTurn == 'd':
            chance = random.randrange(1,10)
            if chance > 2:
                print('Enemy Attack Dodged!')
                print()
            if chance <= 2:
                Health -= random.randrange(5,15)
                print('Dodge Unsuccesful\nPlayer Health:',Health)
                print()
        if EnemyTurn == 'c':
            chance = random.randrange(1,10)
            if chance >5:
                Enemy = Enemy - 10
                print('Enemy Attack Countered!\nEnemy Health:',Enemy)
                print()
            if chance <= 5:
                Health -= random.randrange(10,20)
                print('Counter Disrupted!\n Player Health:',Health)
                print()
        if Health <= 0:
            death()
    print('Enemy Felled!')
    print()
    return Health

# Shop Function
def shop(Health, goldAmount):
    Health = 100
    print()
    print('Hello you found me! I sell all sorts of stuff for adventurers like yourself!')
    shopInput =input('Would you like to look? [y]es, [n]o: ')
    while shopInput != "y" and shopInput != 'n' :
        print("Invalid input...")
        shopInput = input('Would you like to look? [y]es, [n]o: ')
    if shopInput == 'y':
        print('SHOP ITEMS:')
        buyInput=input('[h]ealth potions (heals for 20 hp)\n[e]xit')
        if buyInput == 'h' and goldAmount>= 40:
            goldAmount-=40
            Health += 20
            print('Player Health is now:',Health)
        if buyInput == 'h' and goldAmount<= 40:
            print("Insufficient Gold")
        if buyInput =='e':
            print('ok see you next time!')
   
    if shopInput =='n':
        print('ok see you next time!')
    return Health, goldAmount

#Story Function
def story():
    print()
    storyInput = input('Theres a journal on the ground.... [p]ick up? [d]iscard: ')
    while storyInput != "p" and storyInput != 'd' :
        print("Invalid input...")
        storyInput = input('Theres a journal on the ground.... [p]ick up? [d]iscard: ')
    if storyInput == 'p':
        storyGenerator = random.randrange(1,4)
        print()
        if storyGenerator == 1:
            print('"They say a person needs just three things to be truly happy in this world: \nSomeone to love, something to do, and something to hope for."')
        if storyGenerator == 2:
            print('"O loss of sight, of thee I most complain! Blind among enemies, O worse than chains, Dungeon, or beggary, or decrepit age!"')
        if storyGenerator ==3:
            print('"What other dungeon is so dark as ones own heart! What jailer so inexorable as ones self!')
        if storyGenerator == 4:
            print('”Remind yourself that overconfidence is a slow and insidious killer.”')
    if storyInput =='d':
        print()
        print('Journal discarded')

def death():
    print()
    print('Youve been slain...')
    print()
    sys.exit()


        
        





def main():

    # Set to 'True' when the game is over.
    gameOver = False

    # Player status variables/ constants. 
    # HINT: If you have other player variables to use, such as health, damage, etc. add them here.
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    START_HEALTH = 100
    Health = START_HEALTH
    visited_room1 = False # HINT: Carefully study how these 'visited room' variables are used.
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    
    

    print("Welcome to Dungeon Crawl...")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Steven Bui")
    print("COM S 127 section D")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
        
            while currentRoom != FINAL_ROOM: # HINT: When implmenting combat, if the player's health is <= 0, this loop should not execute.
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1, Health = room1(goldAmount, visited_room1, Health)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2, Health = room2(goldAmount, visited_room2, Health)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3, Health = room3(goldAmount, visited_room3, Health)
                elif currentRoom == 4:
                    currentRoom, goldAmount, visited_room4, Health = room4(goldAmount, visited_room4, Health)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5, Health= room5(goldAmount, visited_room5, Health)

                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
    
            print()
            print("Dungeon Cleared! + 500 xp, gold looted:",goldAmount)
            print()


            goldAmount = START_GOLD
            currentRoom = START_ROOM
            Health = START_HEALTH
            visited_room1 = False
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
    
            
        elif choice == "i": # (**"i" Section Tasks**)
            instructionInput =input('[c]ombat system?, [r]ooms?')
            while instructionInput != "c" and instructionInput != 'r' :
                print("Invalid input...")
                instructionInput = input('[c]ombat system?, [r]ooms? ')
            if instructionInput == 'c':
                print('The combat system is turn based with the options to attack and defend.')
                print('The options for attack include light and heavy attacks.')
                print('Heavy attacks deal more damage than light attacks.')
                print('Light attacks are faster and more likely to land while heavy attacks are slower and less likely to hit.')
                print('The options for defending include dodge and counter.')
                print('The dodge mechanic evades all damage and is likely.\nThe counter mechanic is less likely but gives the player a chance to deal damage on the enemy turn')
                print()
            if instructionInput == 'r':
                print('The rooms moves [n]orth, [s]outh, [e]ast, and [w]est')
                print()
            pass
        elif choice == "q": # (**"q" Section Tasks**)

            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()