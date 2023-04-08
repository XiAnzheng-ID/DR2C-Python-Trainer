from ReadWriteMemory import ReadWriteMemory
import Offset
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("P1 Unlimited Ammo")
os.system('cls')
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

print("this feature a little but bugged read the .txt file for more information")
print("Dont Close this window just minimized it")
print("Close it when you want to turn off this feature")
while True:
    #P1
    process.write(Offset.doltAmmo, 500)
    process.write(Offset.rifleAmmo, 500)
    process.write(Offset.shotgunAmmo, 500)
    process.write(Offset.gasAmmo, 500)
    #process.write(Offset.Battery, 500)

    #P2
    process.write(Offset.p2d, 500)
    process.write(Offset.p2r, 500)
    process.write(Offset.p2s, 500)
    process.write(Offset.p2g, 500)
    #process.write(Offset.p2b, 500)

    #P3
    process.write(Offset.p3d, 500)
    process.write(Offset.p3r, 500)
    process.write(Offset.p3s, 500)
    process.write(Offset.p3g, 500)
    #process.write(Offset.p3b, 500)

    #P3
    process.write(Offset.p4d, 500)
    process.write(Offset.p4r, 500)
    process.write(Offset.p4s, 500)
    process.write(Offset.p4g, 500)
    #process.write(Offset.p4b, 500)

