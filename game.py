import gamefunctions

playerhp = 300
gold = 50
playerdamage = 25
player_inventory =  [
                     {"name": "Charm of Home", "desc": "A charm given to you by your mother before leaving as a good luck token, has no effects.", "type": "trinket"},
                    ]
equipped = None
party = 0
partyactive = True

def loop():
    """Main game loop to start off with."""
    global playerhp, gold, playerdamage, player_inventory, equipped, party
    running = True
    wage = (party*1)

    while running == True:
        if wage > gold:
            
            partyactive = False
            user_input = input(f"You are in town.\n Current HP: {playerhp}, Current Gold: {gold}, You have {party} men in your party. You cannot afford to pay them, and they will not fight with you.\n\nWhat would you like to do?\n1) Leave town (Fight Monster)\n2) Sleep (Restore HP for 5 gold)\n3) Go to the Store\n4) View Inventory\n5) Recruit Troops\n6) Quit")

            if user_input == "1":
                playerhp, gold, equipped, party = gamefunctions.battle(playerhp, gold, playerdamage, player_inventory, equipped, partyactive, party)

            elif user_input == "2":
                print(f"You sleep at the local tavern. \n-5 Gold")
                gold -= 5
                playerhp += 20

            elif user_input == "3":
                gold = gamefunctions.shoploop(gold, player_inventory)
                print("Gold now:", gold)
                print("Inventory:", player_inventory)

            elif user_input == "4":
                gamefunctions.printinv(player_inventory)

            elif user_input == "5":
                party, wage = gamefunctions.recruit(gold, wage, party)

            elif user_input == "6":
                party, wage = gamefunctions.cut(party, wage)

            elif user_input == "7":
                print(f"Thank you for playing, have a good day.")
                running = False

            else:
                print("Invalid Input, Try again.")

        else:

            gold -= wage
            partyactive = True
            user_input = input(f"You are in town.\n Current HP: {playerhp}, Current Gold: {gold}, You have {party} men in your party. You paid them {wage} gold as their wage this turn.\n\nWhat would you like to do?\n1) Leave town (Fight Monster)\n2) Sleep (Restore HP for 5 gold)\n3) Go to the Store\n4) View Inventory\n5) Recruit Troops\n6) Cut Troops\n7) Quit")

            if user_input == "1":
                playerhp, gold, equipped, party = gamefunctions.battle(playerhp, gold, playerdamage, player_inventory, equipped, partyactive, party)

            elif user_input == "2":
                print(f"You sleep at the local tavern. \n-5 Gold")
                gold -= 5
                playerhp += 20

            elif user_input == "3":
                gold = gamefunctions.shoploop(gold, player_inventory)
                print("Gold now:", gold)
                print("Inventory:", player_inventory)

            elif user_input == "4":
                gamefunctions.printinv(player_inventory)

            elif user_input == "5":
                party, wage = gamefunctions.recruit(gold, wage, party)

            elif user_input == "6":
                party, wage = gamefunctions.cut(party, wage)

            elif user_input == "7":
                print(f"Thank you for playing, have a good day.")
                running = False

            else:
                print("Invalid Input, Try again.")

if __name__ == "__main__":
    loop()

    
    

