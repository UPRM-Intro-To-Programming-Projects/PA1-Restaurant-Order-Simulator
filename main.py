from PIL import Image, ImageDraw, ImageFont

# Dictionary to store ordered items and their quantities.
# For the time being, you don't need to worry about dictionaries but if you are curious feel
# free to look at the documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
order = {}

def GenerateReceiptImage(receipt_text, filename="receipt.png"):
    """Generates an image with the receipt content and saves it."""
    # Create a blank image
    image = Image.new("RGB", (400, 600), "white")
    draw = ImageDraw.Draw(image)

    # Load font (default system font)
    font = ImageFont.load_default()

    # Define text position
    x, y = 20, 20

    # Draw the text on the image
    for line in receipt_text.split("\n"):
        draw.text((x, y), line, fill="black", font=font)
        y += 25  # Move down for the next line

    image.save(filename)
    print(f"Receipt saved as {filename}")

def AddItemToOrder(item, amount):
    """Adds an item and its quantity to the order."""
    order[item] = amount

def ModifyItem(list_ingredients):
    """Allows the user to add or remove ingredients from an item."""
    details = ""
    while True:
        print("Would you like to remove or add an ingredient?")
        print("1. Remove")
        print("2. Add")
        print("3. Exit")
        choice = int(input())  # User selects an option

        if choice == 3:
            break  # Exit the loop if the user chooses to stop modifying

        print(f"The ingredients are {list_ingredients}")
        ingredient = input("Which ingredient would you like to modify?\n").lower()

        if choice == 1:  # Remove ingredient
            details = RemoveIngredient(list_ingredients, details, ingredient)

        elif choice == 2:  # Add ingredient
            details = AddIngredient(list_ingredients, details, ingredient)
    return details  # Return modified ingredient details

def GetSubTotalIterator():
    """Calculates the subtotal of the order."""
    total = 0
    for item, amount in order.items():
        total = GetSubTotal(item, amount, total)  # Function assumed to calculate item subtotal

    print(f"Your subtotal is ${total}")
    return total

def Pay():
    """Calculates and displays the total cost of the order, including tax and tip."""
    print("Your receipt:")
    total = GetSubTotalIterator()  # Calculate subtotal
    total = AddTip(total)  # Apply tip
    total += AddIVU(total)  # Apply tax

    receipt_text = "Jack’s Diner Receipt\n"
    receipt_text += "-" * 30 + "\n"
    for item, amount in order.items():
        receipt_text += f"{item} x{amount}\n"
    receipt_text += "-" * 30 + f"\nSubtotal: ${total:.2f}\n"
    receipt_text += "Thank you for dining with us!\n"

    print(receipt_text)  # Print the receipt in the console

    GenerateReceiptImage(receipt_text)  # Generate and save the receipt image

    print(f"Your total is ${total:.2f}")
    print("Thank you for dining at Jack's Diner!")

def Main():
    """Handles the menu system and ordering process."""
    print("Welcome to Jack's Diner!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Order a burger")
        print("2. Order a side")
        print("3. Order a drink")
        print("4. Order a milkshake")
        print("5. Pay")
        menu = int(input())  # User selects an option from the menu

        if menu == 1:
            BurgerMenu()  # Function assumed to display burger options
        elif menu == 2:
            SidesMenu()  # Function assumed to display side options
        elif menu == 3:
            DrinksMenu()  # Function assumed to display drink options
        elif menu == 4:
            MilkshakesMenu()  # Function assumed to display milkshake options
        elif menu == 5:
            print("\nYour final order:")
            for item, amount in order.items():
                print(f"{item} x{amount}")
            Pay()  # Proceed to payment
            break  # Exit the ordering system

def BurgerMenu():
    # TODO Task 1: Implement the burger menu selection logic. Display available burger options,
    #   show ingredients for each, and allow the user to modify the selected item.
    pass

def SidesMenu():
    # TODO Task 2: Implement the sides menu selection logic. Allow the user to choose side items
    #   and ask for the quantity to add to the order.
    pass

def DrinksMenu():
    # TODO Task 3: Implement the drinks menu selection logic. Display available drinks and call the appropriate
    #   menu function for each drink type.
    pass

def SodaMenu():
    # TODO Task 3: Implement the soda menu selection logic. Allow the user to choose a soda type
    #   and return the selected item.
    pass

def LemonadeMenu():
    # TODO Task 1: Implement the lemonade menu selection logic. Allow the user to choose a lemonade flavor
    #   and return the selected item.
    pass

def CoffeeMenu():
    # TODO Task 3:: Implement the coffee menu selection logic. Allow the user to choose a coffee type
    #   and return the selected item.
    pass

def MilkshakesMenu():
    # TODO Task 4:: Implement the milkshakes menu selection logic. Allow the user to choose a milkshake flavor
    #   and return the selected item.
    pass

def GetSubTotal(item, amount, total):
    # TODO Task 5: Complete the logic for calculating the subtotal of the order.
    #   You should calculate the price based on the item, and update the total accordingly.
    #   Add the price calculation logic for various items and print the item details.
    return 0

def AddTip(total):
    # TODO Task 6: Implement the logic for adding a tip based on user input.
    #   The user should choose between 10%, 15%, or 20% or 'No' tip.
    #   Calculate the tip and return the updated total.
    return 0

def AddIVU(total):
    # TODO Task 7: Implement the logic for adding IVU (tax) to the total.
    #   The IVU rate is 11.5%. Return the updated total.
    pass

def RemoveIngredient(list_ingredients, details, ingredient):
    # TODO Task 8: Implement logic to check if the ingredient exists in list_ingredients,
    #   update details accordingly, and print the appropriate message.
    return details

def AddIngredient(list_ingredients, details, ingredient):
    # TODO Task 8: Implement logic to check if the ingredient exists in list_ingredients,
    #   update details accordingly, and print the appropriate message.
    return details

Main()