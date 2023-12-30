from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe")
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
Battery = process.get_pointer(0x9DCA88)

#P1 Stats:
Morale = process.get_pointer(0x9DC9A0)
#Strenght = process.get_pointer(in progress)
#fitness = process.get_pointer(in progress)
#shooting = process.get_pointer(in progress)
#mechanical = process.get_pointer(in progress)
#medical = process.get_pointer(in progress)

#P1 Inventory Slot:
player1_Inventory = process.get_pointer(0x9DCA8C)

#Inventory
inventory_Slot = process.get_pointer(0x9DC480)
item_Quantity = process.get_pointer(0x9DC484)

#P2-P4 Health:
p2Health = process.get_pointer(0x9DCBF8)
p3Health = process.get_pointer(0x9DCED8)
p4Health = process.get_pointer(0x9DD1B8)

#P2-P4 Ammo
p2d = process.get_pointer(0x9DCD50)
p2r = process.get_pointer(0x9DCD54)
p2s = process.get_pointer(0x9DCD58)
p2g = process.get_pointer(0x9DCD48)
p2b = process.get_pointer(0x9DCD68)

p3d = process.get_pointer(0x9DD030)
p3r = process.get_pointer(0x9DD034)
p3s = process.get_pointer(0x9DD038)
p3g = process.get_pointer(0x9DD028)
p3b = process.get_pointer(0x9DD054)

p4d = process.get_pointer(0x9DD310)
p4r = process.get_pointer(0x9DD314)
p4s = process.get_pointer(0x9DD318)
p4g = process.get_pointer(0x9DD308)
p4b = process.get_pointer(0x9DD340)

#Inventory Slot:
#bagInventory = process.get_pointer(0x9DC480)

