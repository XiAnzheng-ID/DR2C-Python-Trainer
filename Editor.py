from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Inventory Editor")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
process.open()

while True:
    print("THIS CAN BREAK YOUR SAVEDATA BECAREFULL WHAT ITEM OR WEAPON YOU EDIT")
    print("This will edit out anything your first charcter inventory slot have")
    print("open the text file for item/weapon number list and more information")
    itemID = int(input("item ID?: "))
    process.write(Offset.player1_Inventory, itemID)
    os.system('cls')
