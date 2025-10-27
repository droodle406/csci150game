import gamefunctions

def main():
    """Main game function to demonstrate gamefunctions usage."""
    name = input("Enter your name, hero: ")
    cash = float(input("How much gold do you have?"))
    
    
    gamefunctions.print_welcome(name, 30)
    gamefunctions.print_shop_menu("Sword", 4000, "Ham", 22.25)
    
    filler = input("What would you like to purchase?")
    num = float(input("How many of that would you like to purchase?"))
    price = float(input("What is the cost on the menu?"))
    gamefunctions.purchase_item(price, cash, num)

    gamefunctions.new_random_monster()
    print("A monster approaches!")
    # To be fleshed out later
    

if __name__ == "__main__":
    main()
