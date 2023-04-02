from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe")
process.open()

#Inventory:
Gas = process.get_pointer(0x9DC468)
Food = process.get_pointer(0x9DC464)
Dolt = process.get_pointer(0x9DC470)
Rifle = process.get_pointer(0x9DC474)
Shotgun = process.get_pointer(0x9DC478)
Medkit = process.get_pointer(0x9DC46C)

#P1 Ammo & health:
doltAmmo = process.get_pointer(0x9DCA70)
rifleAmmo = process.get_pointer(0x9DCA74)
shotgunAmmo = process.get_pointer(0x9DCA78)
gasAmmo = process.get_pointer(0x9DCA68)
Health = process.get_pointer(0x9DC918)
Battery = process.get_pointer(0x9DCAA0)

#P1 Stats:
Morale = process.get_pointer(0x9DC9A0)
#Strenght = process.get_pointer()
#fitness = process.get_pointer()
#shooting = process.get_pointer()
#mechanical = process.get_pointer()
#medical = process.get_pointer()

#P1 Inventory Slot:
player1_Inventory = process.get_pointer(0x9DCA8C)

#P2-P4 Health:
p2Health = process.get_pointer(0x9DCBF8)
p3Health = process.get_pointer(0x9DCED8)
p4Health = process.get_pointer(0x9DD1B8)

#Inventory Slot:
bagInventory = process.get_pointer(0x9DC480)

