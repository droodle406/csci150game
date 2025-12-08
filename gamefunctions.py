"""Game Functions Module.

This module contains functions relating to gameplay technicalities."""


import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase):

    """
    Purchases an item for a Player

    Parameters:
    itemPrice (float): Price of an individual item
    startingMoney (float): Player Bank Account
    quantityToPurchase (int): Number of items player wishes to buy

    Returns:
    items bought and leftover money

    Example:
        purchase_item(2, 200, 10)
        2, 180
    """
    
    #qtp default value
    if quantityToPurchase <= 0:
        quantityToPurchase = 0
    
    #determining how much you can possibly afford
    max_affordable = startingMoney // itemPrice

    #determining if your order is purchasable
    if max_affordable >= quantityToPurchase:
        items_bought = quantityToPurchase
    #if its not, your quantity becomes the most you can buy
    else:
        items_bought = max_affordable
    #final calculations, return
    LeftoverMoney = startingMoney-(itemPrice*items_bought)

    return items_bought, LeftoverMoney

# DIVIDER

def new_random_monster():

    """
    Generates  a random monster for the player

    Parameters:
    None

    Returns:
    Dictionary of the monsters stats.

    Example:
        new_random_monster()
    """

    # determines monster selection
    monster = (random.randint(1,4))
    #provides attributes for every possible monster
    if monster == 1:
        monstername = "goblin"
        monsterdesc = "The curious green goblin see you and snarls. Good luck."
        monsterhealthpool = (random.randint(100,500))
        monsterpower = (random.randint(1,7))
        monstermoney = (random.randint(245,1000))
    elif monster == 2:
        monstername = "ork"
        monsterdesc = "The hulking green beast stares you down and roars. Good luck."
        monsterhealthpool = (random.randint(1500,3000))
        monsterpower = (random.randint(10,25))
        monstermoney = (random.randint(1,200))
    elif monster == 3:
        monstername = "troll"
        monsterdesc = "As you cross a bridge you hear loud footsteps through the river it crosses, this troll has no riddle. Good luck."
        monsterhealthpool = (random.randint(5000,10000))
        monsterpower = (random.randint(5,15))
        monstermoney = (random.randint(750,2000))
    elif monster == 4:
        monstername = "skeleton"
        monsterdesc = "Those spooky scary skeletons will make you shiver and shriek. Good luck."
        monsterhealthpool = (random.randint(100,150))
        monsterpower = (random.randint(1,5))
        monstermoney = (random.randint(1,100))
    else:
        return None
    monsterdict = {"name": monstername, "description": monsterdesc, "health": monsterhealthpool, "power": monsterpower, "money": monstermoney}
    return monsterdict

def print_welcome(name, width):

    """
    Welcomes the player to the game

    Parameters:
    name (str): Player name
    Width (int): number of characters allowed

    Returns:
    Welcome, Player name between a set amount of spaces/characters

    Example:
        print_welcome(Jeff, 15)
              Welcome, Jeff      
    """
    
    # These 4 lines do some math (probably ineffeciently) to find how many spaces need to come before and after the name
    strlngth = len(name)+7
    twidth = (width - strlngth)
    half = int(twidth/2)
    
    # outputs!
    print(f"{' ' * half}Hello, {name} {' ' * half}")
    return None

# Function Calls
print(print_welcome("Jeff", 20))
print(print_welcome("Audrey", 30))
print(print_welcome("Andrew", 55))

def print_shop_menu(item1name, item1price, item2name, item2price):

    """
    Generates  a menu for a shop

    Parameters:
    item1name (str): Name of item1
    item1Price (float): cost of item1
    item2name (str): Name of item2
    item2Price (float): cost of item2

    Returns:
    None

    Example:
        print_shop_menu(Food, 2, Drink, 3)
        Outputs formatted menu
    """
    # Converts prices to Floats
    item1 = float(item1price)
    item2 = float(item2price)
    # gets the number of spaces between each value for item1
    item1spaces1 = 12 - len(item1name)
    item1leng = len(str(f"{item1:.2f}"))
    item1spaces2 = 8 - item1leng
    #same thing item2
    item2spaces1 = 12 - len(item2name)
    item2leng = len(str(f"{item2:.2f}"))
    item2spaces2 = 8 - item2leng


    print(f"/----------------------\\ \n"
      f"| {item1name}{' ' * item1spaces1}{' ' * item1spaces2}${item1:.2f}|\n"
      f"| {item2name}{' ' * item2spaces1}{' ' * item2spaces2}${item2:.2f}|\n"
      f"\\----------------------/")



    return None


# Function Calls
print(print_shop_menu("Apple", 31, "Pear", 1.234))
print(print_shop_menu("Egg", .23, "Bag of Oats", 12.34))
print(print_shop_menu("Sword", 4000, "Ham", 22.25))

def test_functions():
    
    """
    Tests all above code

    Parameters:
    None

    Returns:
    None

    Example:
        test_functions()
    """

    #Each Test run
    print_welcome("Jeff", 20)
    print_shop_menu("Sword", 4000, "Ham", 22.25)
    purchase_item(Potion, 10, 50)
    random_monster()

    return None

def battle(playerhp, gold, playerdamage, player_inventory, equipped, partyactive, party):
    monster_info = new_random_monster()
    
    while playerhp > 0 and monster_info["health"] > 0:

        partydamage = (party*5)

        if equipped:
            totaldamage = playerdamage + equipped["damage"]
        else:
            totaldamage = playerdamage
        
        print(f"{monster_info['description']}\nThe {monster_info['name']} has {monster_info['health']} health and does {monster_info['power']} damage.")
        if equipped:
            print(f"You do {totaldamage} damage, you have a {equipped['name']} equipped and you have {playerhp} health.")
        else:
            print(f"You do {totaldamage} damage and you have {playerhp} health.")
        if partyactive and party > 0:
            print(f"Your men are fighting with you, they will deal {partydamage} damage each turn.")
        elif partyactive == False:
            print(f"Your men were not paid, and refuse to fight")
        else:
            print(f"You have no men to fight with you.")
        
        user_action = input("What would you like to do? \n1) Fight \n2) Equip Item (Will use your turn!!)\n3) Use consumable\n4) Run\n")
        
        if user_action == "1":
            if equipped:
                equipped["currentDurability"] -= 1
                monster_info["health"] -= totaldamage
                playerhp -= monster_info["power"]
                if partyactive and party > 0:
                    print(f"Your men lash out, dealing {partydamage} damage!")
                    monster_info["health"] -= partydamage
                if equipped["currentDurability"] == 0:
                    print("Your sword shatters in your hand!")
                    if equipped in player_inventory:
                        player_inventory.remove(equipped)
                    equipped = None
            else:
                monster_info["health"] -= totaldamage
                playerhp -= monster_info["power"]
                if partyactive and party > 0:
                    print(f"Your men lash out, dealing {partydamage} damage!")
                    monster_info["health"] -= partydamage

        elif user_action == "2":
            item_type = input("What type of item would you like to equip? \nChoices: weapon")
            if item_type == "weapon":
                equipped = equip_item(player_inventory, "weapon")
                if partyactive and party > 0:
                    print(f"Your men lash out, dealing {partydamage} damage!")
                    monster_info["health"] -= partydamage
                    
            else:
                print("That is not a supported type, try again.")

        elif user_action == "3":
            printinv(player_inventory)
            consumable_name = input("Which consumable would you like to use? ")

            playerhp, monster_info["health"] = use_consumable(player_inventory, consumable_name, playerhp, monster_info)
            if partyactive and party > 0:
                    print(f"Your men lash out, dealing {partydamage} damage!")
                    monster_info["health"] -= partydamage
            
        elif user_action == "4":
            print("You ran away.")
            return playerhp, gold, equipped, party
        else:
            print("Unrecognized command")
        
        if playerhp <= 0:
            print("Your character passed out. Your men scatter...")
            party = 0
            return playerhp, gold, equipped, party
        elif monster_info["health"] <= 0:
            print(f"Congratulations! You have defeated the {monster_info['name']}!")
            gold += 15
            return playerhp, gold, equipped, party

    return playerhp, gold, equipped, party

def shoploop(gold, inventory):
    curgold = gold
    print_shop_menu("Sword", 10, "Charm of Doom", 15)
    choice = input("What would you like to buy?\n1) Sword\n2)Charm of Doom\n0) Exit shop")

    if choice == "0":
        print("Have a good day, come again soon!")
        return gold

    if choice == "1":
        item_name = "1"
        price = 10
    elif choice == "2":
        item_name = "2"
        price = 15
    else:
        print("Invalid choice.")
        return gold

    qty = int(input(f"How many would you like to buy? "))

    items_bought, gold = purchase_item(price, curgold, qty)

    for _ in range(items_bought):
        if item_name == "1":
            inventory.append({
                "name": "Sword",
                "type": "weapon",
                "maxDurability": 10,
                "currentDurability": 10,
                "damage": 5,
                "equipped": False
            })
        elif item_name == "2":
            inventory.append({
                "name": "Pendant of Doom",
                "type": "consumable",
                "effect": "auto_defeat"
            })

    print(f"Bought!")
    return gold

def equip_item(inventory, item_type):
    items = [item for item in inventory if item["type"] == item_type]

    if not items:
        print(f"You have no {item_type}s to equip.")
        return None

    print(f"Choose a {item_type} to equip:")
    for i, item in enumerate(items, start=1):
        print(f"{i}) {item['name']}")
    print(f"{len(items)+1}) None")

    choice = int(input("Enter choice: "))

    if choice == len(items) + 1:
        return None
    
    else:
        return items[choice - 1]

def use_consumable(player_inventory, item_name, playerhp, monster_info):

    for item in player_inventory:
        if item["name"].lower() == item_name.lower() and item["type"] == "consumable":

            if item.get("effect") == "heal":
                playerhp += item["heal"]
                print(f"You drink a {item['name']} and heal {item['heal']} HP!")
            
            if item.get("effect") == "damage":
                monster_info["health"] -= item["damage"]
                print(f"You throw a {item['name']} and deal {item['damage']} damage!")

            if item.get("effect") == "auto_defeat":
                monster_info["health"] = 0
                print(f"You use your charm, it lights up and instantly turns the monster and itself to dust!")

            player_inventory.remove(item)
            return playerhp, monster_info["health"]
    
    print("You don't have that consumable.")
    return {"playerhp": playerhp, "monster": monster}

def printinv(player_inventory):
    if not player_inventory:
        print("Your inventory is empty.")
        return
    
    print("\n--- Your Inventory ---")
    for i, item in enumerate(player_inventory, start=1):
        if item["type"] == "weapon":
            print(f"{i}) {item['name']} (Weapon, Damage: {item['damage']}, Durability: {item['currentDurability']}/{item['maxDurability']})")

        elif item["type"] == "consumable":
            if item.get("effect") == "heal":
                print(f"{i}) {item['name']} (Consumable, Heals: {item['heal']})")
            elif item.get("effect") == "damage":
                print(f"{i}) {item['name']} (Consumable, Damage: {item['damage']})")
            elif item.get("effect") == "auto_defeat":
                print(f"{i}) {item['name']} (Consumable), Instant Victory in Battle")
        
        else:
            print(f"{i}) {item['name']} ({item['type']})")
    print("-----------------------\n")

def recruit(gold, wage, party):
    nummen = monster = (random.randint(1,3))
    costmen = nummen*10
    costwage = nummen*1
    startgold = gold
    
    if startgold >= costmen:
        recruitinput = input(f"{nummen} men wander about town, ready to join you for {costmen} gold. You will have to pay {costwage} gold in wages per turn after recruiting them.\n\nWhat would you like to do?\n1)Recruit them\n2) Leave")
        if recruitinput == "1":
            print(f"The men's eyes light up as you pay them, they will follow you.")
            party += nummen
            wage += costwage
            return party, wage
        elif recruitinput == "2":
            return
        else:
            print("Invalid Input, Try again.")
    if startgold < costmen:
        recruitinput = input(f"{nummen} men wander about town, ready to join you for {costmen} gold. You will have to pay {costwage} gold in wages per turn after recruiting them. You cannot pay enough to recruit them, come back later.")
        return

def cut(party, wage):
    if party > 0:
        cutin = input(f"You have {party} men in your party, taking up {wage}.\nHow many men would you like to cut?")
        if cutin <= party:
            party -= cutin
            wage -= cutin*1
            print(f"You tell {cutin} men to leave you, they listen and leave. You now have {party} men taking up {wage} wages.")
            return party, wage
        elif cutin > party:
            print("You do not have {cutin} men in your party, try again.")
        else:
            print("Invalid Input, Try again.")
    else:
        print(f"Why are you here? You have no men!")
        return

        

    
