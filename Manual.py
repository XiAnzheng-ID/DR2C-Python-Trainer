from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os
import time

ctypes.windll.kernel32.SetConsoleTitleW("Manual Loot/Supply Editor")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("This is a manual loot/supply editor you can set how much loot/supply you want")
print("Your loot can still decreased by an event or trade")
print("Choose 1 on the main window for Unlimited Loot/Supply\n")
edit = int(input("How much you want?: "))
process.write(Offset.Gas, edit)
process.write(Offset.Food, edit)
process.write(Offset.Dolt, edit)
process.write(Offset.Rifle, edit)
process.write(Offset.Shotgun, edit)
process.write(Offset.Medkit, edit)
process.write(Offset.doltAmmo, edit)

os.system('cls')
print("Done :D")
print("This window will close by itself in 3 sec")
time.sleep(3)