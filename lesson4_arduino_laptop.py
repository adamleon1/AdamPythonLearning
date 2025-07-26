import serial
import time
import tkinter as tk
def turnon():
    with serial.Serial('COM7',9600,timeout=1) as s:
        time.sleep(1)
        s.write(b'on\n')
    

def turnoff():
    with serial.Serial('COM7',9600,timeout=1) as s:
        time.sleep(1)
        s.write(b'off\n')
    

def turnonled():
    with serial.Serial('COM7',9600,timeout=1) as s:
        time.sleep(1)
        s.write(b'ledon1\n')
    

def turnoffled():
    with serial.Serial('COM7',9600,timeout=1) as s:
        time.sleep(1)
        s.write(b'ledoff1\n')
    

b1 = tk.Button(text ='turn on fan',command=turnon)
b2 = tk.Button(text ='turn off fan',command=turnoff)

b1.pack()
b2.pack()


b3 = tk.Button(text ='turn on led',command=turnonled)
b4 = tk.Button(text ='turn off led',command=turnoffled)
b3.pack()
b4.pack()

tk.mainloop()