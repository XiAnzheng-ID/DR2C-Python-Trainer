from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Inventory Quantity Editor")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

while True:
    print("THIS CAN BREAK YOUR SAVEDATA BECAREFULL WHAT ITEM OR WEAPON YOU EDIT")
    print("DO NOT EDIT WHEN THERE IS NO ITEM/WEAPON AT FIRST INVENTORY SLOT")
    print("IT WILL BUG YOUR SAVE DATA AND PROBABLY CORRUPT IT")
    print("You can edit any item quantity at first inventory slot (top left corner)")
    print("Open the text file for more information")
    Quantity = int(input("Quantity?: "))
    process.write(Offset.item_Quantity, Quantity)
    
    os.system('cls')