# --- FP1-S01 Dictionaries Program --- #
# - Xzavier Moosomin - #
# - 04/07/2024 - #

# - Developer Notes - #
# this was kind of a doozy to figure out
# im smart though, so i got it
# dont worry about how long it took, just a small 5 minute coding adventure

# - Imports - #
import random, time

# - Dictionaries - #

weapons = {"fists": 250, "bow and arrow": 400, "sword": 500}

badguys = {"bear": 300, "wolf": 500, "dragon": 1000}

# - Lists -#

specitems = [ ]

# - Variables - #
run = 1

p_health = 2000

# - Functions - #

def find_bg_dmg(badguy):
    return badguys[badguy] / 6 # figures out the enemy's damage using the value

def fight_enemy(weapon, enemy, health):
    bg_dmg = find_bg_dmg(enemy) # uses the function inside the function no way
    bg_health = badguys[enemy] # takes the enemy's value of the key
    p_dmg = weapons[weapon] # same thing as the enemy's health, but assigns it to damage
    
    print(enemy,"'s damage is", bg_dmg)
    time.sleep(2)
    print("Your weapon is", weapon)
    time.sleep(2)
    print("It deals", p_dmg, "damage.")
    time.sleep(2)
    
    god_wolf_chance = random.randint(1, 100)
    if god_wolf_chance == 25:
        print("Oh god, the super wolf can be found!")
        time.sleep(2)
        badguys["wolf"] = 5000 # updates the wolf's value
        
    elif god_wolf_chance != 25:
        print("Good, you didn't find the super wolf this time.")
        time.sleep(2)
        
    dad_find_chance = random.randint(1, 10)
    
    if dad_find_chance <= 3:
        print("Apparently your dad is wandering around here, so look out.")
        badguys["dad"] = 5
        
    if weapon == "fists" and enemy == "dragon":
        print("You're fighting the Dragon?")
        time.sleep(2)
        print("With your hands?")
        time.sleep(2)
        print("It's over for you, lil' bro.")
    
    while p_health > 0 and bg_health > 0:
        print("Look out, he swings!")
        time.sleep(2)
        bg_hitchance = random.randint(0, 10)
        
        if bg_hitchance <= 4:
            print("No way, he hit you!")
            time.sleep(2)
            health -= bg_dmg
            print("You now have", health, "health.")
            time.sleep(2)
            
        elif bg_hitchance > 4:
            print("He missed. Aww.")
            time.sleep(2)
            
        print("You swing at the mofo!")
        p_hitchance = random.randint(0, 5)
        
        if p_hitchance >= 2:
            print("You hit!")
            time.sleep(2)
            bg_health -= p_dmg
            print(enemy, "now has", bg_health, "health")
            time.sleep(2)
        elif p_hitchance < 2:
            print("Aww, you missed.")
            time.sleep(2)
            
    if health > 0:
        print("You beat the lil' guy!")
        time.sleep(2)
        print("Well done.")
        time.sleep(2)
        print("You have", health, "health.")
            
    return health

# - Main Code - #
print("Set difficulty. Each level reduces your health to make it a challenge.")
print("""
Easy = 2000 HP
Medium = 1250 HP
Hard = 1000 HP
""")
set_diff = input("What do you want to set it to?\n>").lower()
if set_diff == "easy":
    print("Difficulty set to Easy.")

elif set_diff == "medium":
    print("Difficulty set to Medium.")
    p_health = 1250
          
elif set_diff == "hard":
    print("Difficulty set to Hard.")
    p_health = 1000
          
print("Good luck!")
print("Welcome, Traveller, to Gooneria.")
time.sleep(2)
print("Right now, you're broke as hell.")
time.sleep(2)
print("Go use your muscles to fight some bad guys, and make bank.")
# the list(badguys(keys)) takes the badguys keys and turns it into a list
# then it takes the len of that and if it's greater than 0, the game keeps running
while p_health > 0 and len(list(badguys.keys())) > 0:
    choice_1 = input("""
What do you want to do?
1 - Move
2 - Fight
3 - Inventory
4 - Die (what?)
>""").lower()
   
    if choice_1 == "1" or choice_1 == "move":
        move_choice_1 = input("""
Where do you want to go?
1 - Shop
2 - Park
3 - Back
>""").lower()
        # --- Shop --- #
        if move_choice_1 == "1" or move_choice_1 == "shop":
            if 'Strange Artifact' in specitems:
                print("Looks like you already got what you came for.")
                time.sleep(2)
                print("You check the orb.")
                time.sleep(2)
                print("It gently pulses.")
                time.sleep(2)
                print("Doesn't seem like the place to use it.")
                   
            else:
                print("Right now, it looks like the store's closed.")
                time.sleep(2)
                print("But wait.")
                time.sleep(2)
                print("What's that?")
                time.sleep(2)
                print("Looks like a cool artifact!")
                time.sleep(2)
                print("You got a 'Strange Artifact'!")
                specitems.append('Strange Artifact')
                time.sleep(3)
        # --- Park --- #   
        elif move_choice_1 == "2" or move_choice_1 == "park":
            if 'Strange Artifact' in specitems:
                print("You check the orb.")
                time.sleep(2)
                print("It pulses brighter.")
                time.sleep(2)
                print("You vaguely follow the direction where it shines brighter.")
                time.sleep(2)
                print("It leads you to the fountain.")
                time.sleep(2)
                print("You drop the orb into the water.")
                time.sleep(2)
                print("It disolves into ash.")
                time.sleep(2)
                print("I don't know if it was meant to do that...")
                time.sleep(2)
                lost_item = specitems.pop(0) # pops the strange artifact and removes it from the special inventory list
                print(lost_item, "was removed from your inventory.")
                time.sleep(2)
                weapons["gun"] = 5000
                print("Something was added to your inventory!")
                time.sleep(2)
                
            # if player doesnt have orb in special items, run this block        
            else:
                print("You stumble around the park, and find nothing.")
                time.sleep(2)
                print("But you did find an enemy to fight, so good luck.")
                time.sleep(2)
                bg_list = list(badguys.keys())
                enemy_choice = bg_list[random.randint(0, len(bg_list)-1)]
                print("looks like you're fighting a", enemy_choice)
                time.sleep(2)
                print("You have", len(bg_list), "monsters to fight.")
                # ^ ex. "you have 5 monsters to fight."^
                time.sleep(2)
                print(weapons) # prints out the players weapons so they know what weapons they can use
                weapon_count = 1
                    
                while weapon_count == 1:
                    weapon_choice = input("What weapon do you want to use?\n>").lower()
                    if weapon_choice in weapons:
                        p_health = fight_enemy(weapon_choice, enemy_choice, p_health)
                        weapon_count = 0
                    else:
                        print("That's not a valid weapon, try again.")
                        
                del badguys[str(enemy_choice)]
                    
    # --- Fight Option --- #
    elif choice_1 == "2" or choice_1 == "fight":
        print("You wander around the area for a little while.")
        time.sleep(2)
        print("You enjoy the scenery.")
        time.sleep(2)
        print("A bad guy stands in your way!")

        bg_list = list(badguys.keys())
        enemy_choice = bg_list[random.randint(0, len(bg_list)-1)]
        print("looks like you're fighting a", enemy_choice)
        time.sleep(2)
        print("You have", len(badguys), "monsters to fight.")
        # ^ ex. "you have 5 monsters to fight."^
        time.sleep(2)
        print(weapons) # prints out the players weapons so they know what weapons they can use
        weapon_count = 1
            
        while weapon_count == 1:
            weapon_choice = input("What weapon do you want to use?\n>").lower()
            if weapon_choice in weapons:
                p_health = fight_enemy(weapon_choice, enemy_choice, p_health)
                weapon_count = 0
            else:
                print("That's not a valid weapon, try again.")
                        
        del badguys[str(enemy_choice)] # when the player wins, removes the enemy from the dictionary
        # ^ i dunno if it has to be a string or not to remove ^
    # --- Inventory Option --- #    
    elif choice_1 == "3" or choice_1 == "inventory":
        print("Special Inventory:")
        for item in specitems:
            print(item)
            time.sleep(2)
        if len(specitems) == 0:
            print("Nothing to show.")
            time.sleep(2)
            
        print("Avaliable weapons:")
        for weapon in weapons:
            print(weapon)
            time.sleep(2)
        if len(list(weapons)) == 0:
            print("How do you have 0 weapons?")
                
    elif choice_1 == "4" or choice_1 == "die":
        print("What?")
        time.sleep(2)
        print("Why would you do that?")
        time.sleep(2)
        print("Guess you're dead now.")
        time.sleep(3)
        game_run = 0
            
if p_health <= 0:
    print("You died!")
    time.sleep(2)
    print("Bro for real got mogged on. What the heck.")
    
else:
    print("wait, you killed everything?")
    time.sleep(2)
    print("I mean, you killed everything!")
    
