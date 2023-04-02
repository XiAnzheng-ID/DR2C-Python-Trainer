from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Unlimited Health")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")
while True:
    process.write(Offset.Health, 6)    
    process.write(Offset.p2Health, 6)
    process.write(Offset.p3Health, 6)
    process.write(Offset.p4Health, 6)