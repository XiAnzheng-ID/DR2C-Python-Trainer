import sys
import subprocess
import ctypes
import os
import time

ctypes.windll.kernel32.SetConsoleTitleW("DR2C Trainer by XiAnzheng v08.04.2023 , Enjoy :D ")
os.system('cls')
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
    process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
    process.open()

    while True:
        print("https://github.com/XiAnzheng-ID/DR2C-Python-Trainer-with-Inventory-Editor")
        print("Feature:\n1. Unlimited Loot/Supply")
        print("2. Unlimited Ammo")
        print("3. Unlimited Health")
        print("4. P1 Max Stat")
        print("5. Weapon & Item Editor")
        print("6. Quantity Editor")
        print("7. Manual Supply Editor\n")
        choice = int(input("Choice?: "))

        if choice == 1:
            subprocess.Popen(["python", "Loot.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        elif choice == 2:
            subprocess.Popen(["python", "Ammo.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        elif choice == 3:
            subprocess.Popen(["python", "Health.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system('cls')
        elif choice == 4:
            subprocess.Popen(["python", "Stats.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
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
    

