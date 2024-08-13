from ReadWriteMemory import ReadWriteMemory
import Offset
import time

def loot(stop_event):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    while not stop_event.is_set():
        process.write(Offset.Gas, 99999)
        process.write(Offset.Food, 99999)
        process.write(Offset.Dolt, 99999)
        process.write(Offset.Rifle, 99999)
        process.write(Offset.Shotgun, 99999)
        process.write(Offset.Medkit, 99999)
        time.sleep(0.1)
    