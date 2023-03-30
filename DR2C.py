from ReadWriteMemory import ReadWriteMemory
import ctypes

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe")
process.open()
ctypes.windll.kernel32.SetConsoleTitleW("DR2C Trainer")
print("DR2C Hacks by XiAnzheng Enjoy")
print("Feature\nUnlimited Inventory")
print("Player 1 Unlimited Ammo")

base = 0x400000
#memory = base + 0x9DC468
#Inventory
Gas = process.get_pointer(0x9DC468)
Food = process.get_pointer(0x9DC464)
Dolt = process.get_pointer(0x9DC470)
Rifle = process.get_pointer(0x9DC474)
Shotgun = process.get_pointer(0x9DC478)
Medkit = process.get_pointer(0x9DC46C)
#P1 Ammo
doltAmmo = process.get_pointer(0x9DCA70)
rifleAmmo = process.get_pointer(0x9DCA74)
shotgunAmmo = process.get_pointer(0x9DCA78)
gasAmmo = process.get_pointer(0x9DCA68)

#while True:
    #value = process.read(gas)
    #print(value)
    
while True:
        process.write(Gas, 99999)
        process.write(Food, 99999)
        process.write(Dolt, 99999)
        process.write(Rifle, 99999)
        process.write(Shotgun, 99999)
        process.write(Medkit, 99999)
        process.write(doltAmmo, 99999)
        process.write(rifleAmmo, 99999)
        process.write(shotgunAmmo, 99999)
        process.write(gasAmmo, 99999)
