from ReadWriteMemory import ReadWriteMemory
from ReadWriteMemory import ReadWriteMemoryError
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Inventory Editor")
os.system('cls')
rwm = ReadWriteMemory()

try:
    process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
    process.open()
    Inventory = process.get_pointer(0x9DCA8C)

    while True:
        print("THIS CAN BREAK YOUR SAVEDATA BECAREFULL WHAT ITEM OR WEAPON YOU EDIT")
        print("This will edit out anything your first charcter inventory slot have")
        print("open the text file for item/weapon number list and more information")
        itemID = int(input("item ID?: "))
        process.write(Inventory, itemID)
        os.system('cls')

except ReadWriteMemoryError as error:
    print(error)
    print("Error tidak dapat menemukan/menulis process\ncoba jalankan sebagai admin")
