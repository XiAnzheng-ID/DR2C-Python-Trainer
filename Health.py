from ReadWriteMemory import ReadWriteMemory
import Offset
import time

def health(stop_event):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    while not stop_event.is_set():
        process.write(Offset.Health, 6)    
        process.write(Offset.p2Health, 6)
        process.write(Offset.p3Health, 6)
        process.write(Offset.p4Health, 6)

        time.sleep(2)