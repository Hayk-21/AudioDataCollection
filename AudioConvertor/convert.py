from pydub import AudioSegment
import os

i = 1
path = '../../BigData/hy-AM/'
dir = 'clips/'
for file in os.listdir(os.path.join(path, dir)):
    output_file = path+"wav/hy_"+str(i)+".wav"
    sound = AudioSegment.from_mp3(path+dir+file)
    sound.export(output_file, format="wav")
    i += 1
