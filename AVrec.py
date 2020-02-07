from multiprocessing import Process
import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave


def func1():
 cap = cv2.VideoCapture(0)
 

 if (cap.isOpened() == False): 
   print("Unable to read camera feed")
 
 frame_width = int(cap.get(3))
 frame_height = int(cap.get(4))
 
 out = cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
 while(True):
   ret, frame = cap.read()
 
   if ret == True: 
     out.write(frame)
     cv2.imshow('frame',frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   else:
     break 
 cap.release()
 out.release()
 cv2.destroyAllWindows() 


def func2():
 fs = 44100  
 seconds = 3 

 myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
 sd.wait()  
 write('audio.wav', fs, myrecording)

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()
