from ReadWriteMemory import ReadWriteMemory
from ReadWriteMemory import ReadWriteMemoryError
import ctypes
import os
import subprocess

ctypes.windll.kernel32.SetConsoleTitleW("DR2C Trainer")
os.system('cls')
rwm = ReadWriteMemory()

try:
    subprocess.Popen(["python", "Editor.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
    process.open()
    print("DR2C Hacks by XiAnzheng Enjoy")
    print("Feature:\nUnlimited Loot/Supply")
    print("Player 1 Unlimited Ammo & Health")
    print("Weapon & Item Editor")

    #Inventory
    Gas = process.get_pointer(0x9DC468)
    Food = process.get_pointer(0x9DC464)
    Dolt = process.get_pointer(0x9DC470)
    Rifle = process.get_pointer(0x9DC474)
    Shotgun = process.get_pointer(0x9DC478)
    Medkit = process.get_pointer(0x9DC46C)

    #P1 Ammo & health
    doltAmmo = process.get_pointer(0x9DCA70)
    rifleAmmo = process.get_pointer(0x9DCA74)
    shotgunAmmo = process.get_pointer(0x9DCA78)
    gasAmmo = process.get_pointer(0x9DCA68)
    Health = process.get_pointer(0x9DC918)

    while True:
        #Inventory
        process.write(Gas, 99999)
        process.write(Food, 99999)
        process.write(Dolt, 99999)
        process.write(Rifle, 99999)
        process.write(Shotgun, 99999)
        process.write(Medkit, 99999)
        process.write(doltAmmo, 99999)

        #P1 Ammo & Health 
        process.write(rifleAmmo, 99999)
        process.write(shotgunAmmo, 99999)
        process.write(gasAmmo, 99999)
        process.write(Health, 6)


except ReadWriteMemoryError as error:
    print(error)
    print("Error tidak dapat menemukan/menulis process\ncoba jalankan sebagai admin")


#ignore this as the memory pattern in this game is static no need to find the pointer
#base = 0x400000
#memory = base + 0x9DC468

#while True:
    #value = process.read(gas)
    #print(value)
    

