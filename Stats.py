from ReadWriteMemory import ReadWriteMemory
import Offset
import time

def stats(stop_event):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    while not stop_event.is_set():
        process.write(Offset.Morale, 98300)
        time.sleep(2)
