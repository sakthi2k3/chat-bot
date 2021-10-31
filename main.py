import time
from pygame import mixer
from db import reply  
import speech_recognition as sr
import pyttsx3 
from gtts import gTTS

text="hi i am neymar"
lang="en"
output=gTTS(text=text,lang=lang,slow=False)
output.save("reply.mp3")
mixer.init()
mixer.music.load("reply.mp3")
mixer.music.play()
while mixer.music.get_busy():  
    time.sleep(1)
mixer.music.unload()


  
r = sr.Recognizer() 
  

def SpeakText(command):

    
      
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      

  
while(1):    
      
 
    try:
          
        with sr.Microphone() as source2:
              
            audio_data = r.record(source2, duration=4)
            print("Recognizing...")
            text = r.recognize_google(audio_data)
            if text!="stop" and text!="bye":
                text=reply(text)
                output=gTTS(text=text,lang=lang,slow=False)
                output.save("reply.mp3")
                mixer.music.load("reply.mp3")
                mixer.music.play()
                while mixer.music.get_busy():  
                    time.sleep(1)
                mixer.music.unload()
            else:    
                text="ok goodbye have a nice day"
                output=gTTS(text=text,lang=lang,slow=False)
                output.save("reply.mp3")
                mixer.music.load("reply.mp3")
                mixer.music.play()
                while mixer.music.get_busy():  
                    time.sleep(1)
                mixer.music.unload()
                
              
    except sr.RequestError as e:
            pass          
    except sr.UnknownValueError:
            pass

