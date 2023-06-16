from ReadWriteMemory import ReadWriteMemory
import Offset

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog-GOG.exe") #change the process name to what version u use
process.open()

while True:
    process.write(Offset.Morale, 98300)