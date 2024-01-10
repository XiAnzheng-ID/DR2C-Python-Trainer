import threading
import ctypes
import os
import time
from ReadWriteMemory import ReadWriteMemory

unlimited_loot_status = False
unlimited_ammo_status = False
unlimited_health_status = False
max_stat_status = False

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def background(script, stop_event):
    threading.Thread(target=script, args=(stop_event,)).start()

def create_stop_event():
    return threading.Event()

try:
    import Ammo
    import Health
    import Loot
    import Manual
    import Stats

    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe")
    process.open()

    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("DR2C Trainer by XiAnzheng v09.01.2024 , Enjoy :D ")
        cls()
        print("https://github.com/XiAnzheng-ID/Death-Road-2-Canada-Trainer-by-XiAnzheng")
        print("Feature:")
        print(f"1.[{'ON' if unlimited_loot_status else 'OFF'}] Unlimited Loot")
        print(f"2.[{'ON' if unlimited_ammo_status else 'OFF'}] Unlimited Ammo")
        print(f"3.[{'ON' if unlimited_health_status else 'OFF'}] Unlimited Health")
        print(f"4.[{'ON' if max_stat_status else 'OFF'}] P1 Max Stat (underdevelopment only morale work for now!)")
        print("5. Weapon & Item Editor")
        print("6. Quantity Editor")
        print("7. Manual Supply Editor\n")
        choice = int(input("Choice?: "))

        if choice == 1:
            unlimited_loot_status = not unlimited_loot_status  # Toggle status
            if unlimited_loot_status:
                stop_event_loot = create_stop_event()
                background(Loot.loot, stop_event_loot)
            else:   
                stop_event_loot.set()

        elif choice == 2:
            unlimited_ammo_status = not unlimited_ammo_status
            if unlimited_ammo_status:
                stop_event_ammo = create_stop_event()
                background(Ammo.ammo, stop_event_ammo)
            else:
                stop_event_ammo.set()

        elif choice == 3:
            unlimited_health_status = not unlimited_health_status
            if unlimited_health_status:
                stop_event_health = create_stop_event()
                background(Health.health, stop_event_health)
            else:
                stop_event_health.set()

        elif choice == 4:
            max_stat_status = not max_stat_status
            if max_stat_status:
                stop_event_stats = create_stop_event()
                background(Stats.stats, stop_event_stats)
            else:
                stop_event_stats.set() 

        elif choice == 5:
            Manual.editor()
        elif choice == 6:
            Manual.quantity()
        elif choice == 7:
            Manual.item()
        else:
            print("Error, put 1-7 on the console")
            time.sleep(2)
            cls()

except Exception as ex:
    print(f"Unhandled exception: {ex}")
    print("Error cant write/found the process , try run it as administrator")
    print("Does the game running?")
    input("Press Enter to close this app")