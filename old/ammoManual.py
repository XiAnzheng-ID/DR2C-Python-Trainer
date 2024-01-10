from ReadWriteMemory import ReadWriteMemory
import Offset
import os

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
process.open()

print("This is a manual ammo/supply editor you can set how much ammo/supply you want")
print("Your loot can still decreased by an event or trade")

item = int(input("How much you want?: "))
process.write(Offset.Gas, item)
process.write(Offset.Food, item)
process.write(Offset.Dolt, item)
process.write(Offset.Rifle, item)
process.write(Offset.Shotgun, item)
process.write(Offset.Medkit, item)
process.write(Offset.doltAmmo, item)

os.system("cls")