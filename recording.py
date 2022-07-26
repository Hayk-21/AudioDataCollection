import sounddevice
from scipy.io.wavfile import write
import time
from caps_lock import change_status
from terminal_loading_bar import loadbar

fps = 44100
duration = 2
items = range(5) #<----------------files count
timeout = 1 #sec

l = len(items)
loadbar(0, l, prefix='Progress:', suffix='Complete', length=100)
for i in items:
    time.sleep(timeout)
    change_status()
    loadbar(i+1, l, prefix='Progress:', suffix='Complete', length=100)
    recording = sounddevice.rec(int(duration*fps),samplerate = fps , channels = 2)
    sounddevice.wait()
    write("AudioData/Output_"+str(i)+".wav" , fps, recording)     # for saving our recording in wav file    change_status()
    change_status()
print("Done!")