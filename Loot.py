from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Unlimited Loot/Supply")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")
while True:
    process.write(Offset.Gas, 99999)
    process.write(Offset.Food, 99999)
    process.write(Offset.Dolt, 99999)
    process.write(Offset.Rifle, 99999)
    process.write(Offset.Shotgun, 99999)
    process.write(Offset.Medkit, 99999)