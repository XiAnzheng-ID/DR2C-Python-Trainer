from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("P1 Stats Hack")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")
print("This feature still in development right now only morale that affected")
while True:
    process.write(Offset.Morale, 98300)