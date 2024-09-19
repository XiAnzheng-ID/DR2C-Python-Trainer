from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe")
process.open()

#Inventory:
Food = process.get_pointer(0x9E2264)
Gas = process.get_pointer(0x9E2268)
Medkit = process.get_pointer(0x9E226C)
Dolt = process.get_pointer(0x9E2270)
Rifle = process.get_pointer(0x9E2274)
Shotgun = process.get_pointer(0x9E2278)

#P1 Ammo & health:
Health = process.get_pointer(0x9E2718)
sHealth = process.get_pointer(0x9E4998)
aHealth = process.get_pointer(0x9E3578)
gasAmmo = process.get_pointer(0x9E2868)
doltAmmo = process.get_pointer(0x9E2870)
rifleAmmo = process.get_pointer(0x9E2874)
shotgunAmmo = process.get_pointer(0x9E2878)
Battery = process.get_pointer(0x9E2888)

#P1 Stats:
#Morale = process.get_pointer(0x9DC9A0)
#Strenght = process.get_pointer(in progress)
#fitness = process.get_pointer(in progress)
#shooting = process.get_pointer(in progress)
#mechanical = process.get_pointer(in progress)
#medical = process.get_pointer(in progress)

#Inventory
inventory_Slot = process.get_pointer(0x9E2280)
item_Quantity = process.get_pointer(0x9E2284)

#P2-P4 Health: (idk why all player have different offset for special and normal character)
p2Health = process.get_pointer(0x9E29F8)
p2sHealth = process.get_pointer(0x9E3E18)
p3Health = process.get_pointer(0x9E2CD8) 
p3sHealth = process.get_pointer(0x9E3298)
p4Health = process.get_pointer(0x9E2FB8)
p4sHealth = process.get_pointer(0x9E29F8)

#P2-P4 Ammo
p2d = process.get_pointer(0x9E2B50)
p2r = process.get_pointer(0x9E2B54)
p2s = process.get_pointer(0x9E2B58)
p2g = process.get_pointer(0x9E2B48)
p2b = process.get_pointer(0x9E2B68)

p3d = process.get_pointer(0x9E2E30)
p3r = process.get_pointer(0x9E2E34)
p3s = process.get_pointer(0x9E2E38)
p3g = process.get_pointer(0x9E2E28)
p3b = process.get_pointer(0x9E2E54)

p4d = process.get_pointer(0x9E3110)
p4r = process.get_pointer(0x9E3114)
p4s = process.get_pointer(0x9E3118)
p4g = process.get_pointer(0x9E3108)
p4b = process.get_pointer(0x9E3140)

sd = process.get_pointer(0x9E33F0)
sr = process.get_pointer(0x9E33F4)
ss = process.get_pointer(0x9E33F8)
sg = process.get_pointer(0x9E33E8)
sb = process.get_pointer(0x9E3140)