from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Manual Loot/Supply Editor")
os.system('cls' if os.name == 'nt' else 'clear')

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
process.open()

def invalid():
        print("Invalid input. Please enter a valid number.")

#item script
def item():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("This is a manual loot/supply editor you can set how much loot/supply you want")
        print("Your loot can still decreased by an event or trade")
        print("Choose 1 on the main window for Unlimited Loot/Supply\n")

        while True:
                try:
                        item = int(input("How much you want?: "))
                        break 
                except ValueError:
                        invalid()

        process.write(Offset.Gas, item)
        process.write(Offset.Food, item)
        process.write(Offset.Dolt, item)
        process.write(Offset.Rifle, item)
        process.write(Offset.Shotgun, item)
        process.write(Offset.Medkit, item)
        process.write(Offset.doltAmmo, item)

#quantity script
def quantity():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("THIS CAN BREAK YOUR SAVEDATA BECAREFULL WHAT ITEM OR WEAPON YOU EDIT")
        print("DO NOT EDIT WHEN THERE IS NO ITEM/WEAPON AT FIRST INVENTORY SLOT")
        print("IT WILL BUG YOUR SAVE DATA AND PROBABLY CORRUPT IT")
        print("You can edit any item quantity at first inventory slot (top left corner)")
        print("Open the text file for more information")

        while True:
                try:
                        num = int(input("How much you want?: "))
                        break
                except ValueError:
                        invalid()

        process.write(Offset.item_Quantity, num)

#weapon script
def editor():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("THIS CAN BREAK YOUR SAVEDATA BECAREFULL WHAT ITEM OR WEAPON YOU EDIT")
        print("This will edit out anything your first charcter inventory slot have")
        print("open the text file for item/weapon number list and more information")
        
        while True:
                try:
                        weapon = int(input("Item ID?: "))
                        break 
                except ValueError:
                        invalid()

        process.write(Offset.player1_Inventory, weapon)