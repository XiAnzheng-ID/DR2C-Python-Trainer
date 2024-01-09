import sys
import subprocess
import threading
import ctypes
import os
import time

#importing other scripts
import Ammo
import Health
import Loot
import Manual

ctypes.windll.kernel32.SetConsoleTitleW("DR2C Trainer by XiAnzheng v16.06.2023 , Enjoy :D ")
os.system('cls' if os.name == 'nt' else 'clear')

print('Checking required module....')
time.sleep(2)
try:
    from ReadWriteMemory import ReadWriteMemory
    from ReadWriteMemory import ReadWriteMemoryError
    print('Required module is installed')
    time.sleep(2)
    os.system('cls')

except ModuleNotFoundError:
    print('Required module is NOT installed!!!')
    print('Installing Required Module....')

    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', 'ReadWriteMemory'],
        stdout=subprocess.DEVNULL
    )

finally:
    from ReadWriteMemory import ReadWriteMemory
    from ReadWriteMemory import ReadWriteMemoryError

rwm = ReadWriteMemory()
try:
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    status = [False] * 4
    subprocesses = [None] * 4
    while True:
        os.system('cls')
        print("https://github.com/XiAnzheng-ID/DR2C-Python-Trainer-with-Inventory-Editor")
        print("Feature:")
        print("ON" if status[0] else "OFF"," 1. Unlimited Loot/Supply")
        print("ON" if status[1] else "OFF"," 2. Unlimited Ammo")
        print("ON" if status[2] else "OFF"," 3. Unlimited Health")
        print("ON" if status[3] else "OFF"," 4. P1 Max Stat")
        print("5. Weapon & Item Editor")
        print("6. Quantity Editor")
        print("7. Manual Supply Editor\n")
        choice = int(input("Choice?: "))

        #Changing the status
        if 1 <= choice <= 4:
            status[choice - 1] = not status[choice - 1]
            
            # Terminate the subprocess if the status is OFF
            if not status[choice - 1] and subprocesses[choice - 1] is not None:
                subprocesses[choice - 1].terminate()
                subprocesses[choice - 1] = None
    
        if choice == 1:
            if status[0]:
                subprocesses[0] = subprocess.Popen([sys.executable, "Loot.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            os.system('cls')
        elif choice == 2:
            if status[1]:
                subprocesses[1] = subprocess.Popen([sys.executable, "Ammo.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            os.system('cls')
        elif choice == 3:
            if status[2]:
                subprocesses[2] = subprocess.Popen([sys.executable, "Health.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            os.system('cls')
        elif choice == 4:
            if status[3]:
                subprocesses[3] = subprocess.Popen([sys.executable, "Stats.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            os.system('cls')
        elif choice == 5:
            subprocess.Popen(["python", "Editor.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        elif choice == 6:
            subprocess.Popen(["python", "Quantity.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        elif choice == 7:
            subprocess.Popen(["python", "Manual.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        else:
            print("Error , put 1-7 on the console")
            time.sleep(2)
            os.system('cls')

except ReadWriteMemoryError as error:
    print(error)
    print("Error cant write/found the process , try run it as administrator")
    print("Does the game running? , or check the process name in the code and try again")
    print("Do you use Steam or GOG version?")

#ignore this as the memory pattern in this game is static no need to find the pointer
#base = 0x400000
#memory = base + 0x9DC468

#while True:
    #value = process.read(gas)
    #print(value)
    

