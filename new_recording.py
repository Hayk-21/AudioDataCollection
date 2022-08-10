import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import multiprocessing as mp
from tkinter import *
from tkinter.ttk import *

fps = 44100
duration = 1
items = 10

def process_1():
    def print_sound_2(indata, outdata, frames, time, status):
        volume = np.max(indata*200)
        volume_bar['value'] = volume
        text.set("Volume: "+str(int(volume))+"%")

    window = Tk()
    window.title('Volume')
    window.geometry('50x350')
    window.config(bg='#345')
    text = StringVar()
    style = Style()
    style.theme_use('alt') 
    style.configure("2.Vertical.TProgressbar", troughcolor ='black', background='#009aff') 

    volume_bar = Progressbar(window, orient=VERTICAL, style="2.Vertical.TProgressbar", length=300)
    volume_bar.pack(pady=10)
    textLabel = Label(window, textvariable=text, background='#345', foreground="#009aff").pack()

    with sd.Stream(callback=print_sound_2):
        window.mainloop()


def process_2():
    def exit_func():
        window.quit()
        exit(0)

    def print_progress(interation, total):
        val = interation / total * 100
        progress_bar['value'] = val
        text.set("Data Collection: "+str(int(val))+"%")

    window = Tk()
    window.title('Data Collection Progress')
    window.geometry('350x100')
    window.config(bg='#345')
    text = StringVar()
    style = Style()
    style.theme_use('alt') 
    style.configure("1.Horizontal.TProgressbar", troughcolor ='black', background='#009aff') 
    style.configure("Emergency.TButton", background='#009aff') 
    

    progress_bar = Progressbar(window, orient=HORIZONTAL, style="1.Horizontal.TProgressbar", length=300)
    progress_bar.pack(pady=10)
    textLabel = Label(window, textvariable=text, background='#345', foreground="#009aff").pack()
    stopButton = Button(window, style='Emergency.TButton', command=exit_func).pack()

    i = 0
    while (i < items):
        sd.sleep(1000)
        style.configure("Emergency.TButton", background='red')
        window.update() 
        recording = sd.rec(int(duration*fps),samplerate = fps , channels = 1)
        sd.wait()
        write("AudioData/Output_"+str(i)+".wav" , fps, recording)     # for saving our recording in wav file
        i += 1
        style.configure("Emergency.TButton", background='#009aff') 
        print_progress(i, items)
        window.update()
    
    exit_func()
    

if __name__ == '__main__':

    proc_1 = mp.Process(target=process_1)
    proc_2 = mp.Process(target=process_2)

    proc_2.start()
    proc_1.start()
    