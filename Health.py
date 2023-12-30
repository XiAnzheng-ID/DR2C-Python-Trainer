from ReadWriteMemory import ReadWriteMemory
import Offset

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
process.open()

while True:
    process.write(Offset.Health, 6)    
    process.write(Offset.p2Health, 6)
    process.write(Offset.p3Health, 6)
    process.write(Offset.p4Health, 6)