from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("P1 Unlimited Ammo")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")
while True:
    process.write(Offset.doltAmmo, 500)
    process.write(Offset.rifleAmmo, 500)
    process.write(Offset.shotgunAmmo, 500)
    process.write(Offset.gasAmmo, 500)
    process.write(Offset.Battery, 500)

