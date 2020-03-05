import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 4

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("P_audio.wav", fs, myrecording)