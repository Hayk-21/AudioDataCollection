import sounddevice as sd
from scipy.io.wavfile import write
import time
from caps_lock import change_status
from terminal_loading_bar import loadbar

fps = 44100
duration = 1
items = range(5) #<----------------files count
timeout = 1 #sec

l = len(items)
loadbar(0, l, prefix='Progress:', suffix='Complete', length=100)
change_status()
i = 0
for i in items:
    time.sleep(timeout)
    change_status()
    loadbar(i+1, l, prefix='Progress:', suffix='Complete', length=100)
    recording = sd.rec(int(duration*fps),samplerate = fps , channels = 1)
    sd.wait()
    write("AudioData/Output_"+str(i)+".wav" , fps, recording)     # for saving our recording in wav file    change_status()
    i += 1
print("Done!")
