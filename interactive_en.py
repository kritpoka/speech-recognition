import speech_recognition as sr  #speech to text
from gtts import gTTS #text to speech
from playsound import playsound #run mp3 audio
from datetime import datetime #get datetime now
import os as os #remove file
import webbrowser as wb #search browser 
import random #random choice for responsive

#variable
howAreYou = ["i'm fine", "i'm great", "i'm good","yes i'm very happy when i see you", "um yeah i'm happy"]
askBack = ["what about you", "thaks and you"]
greeting = ["hey honey", "hello,it's good to hear your voice. how can i help you"]
myAbility = ["i can't do much now. but in future i will do better so much you can read my description"]
myName = ["i'm Moniga","i'm Moniga i will help you"]
refuse = ["sorry can you say again","sorry i don't know can say again"]

#functions
def speechRocognitionEn():
    r = sr.Recognizer() #run Initiate
    with sr.Microphone() as source: 
        playsound("./beep.mp3") #send an alarm
        audio = r.record(source, duration=4) #record voice 4 secconds
        playsound("./beep.mp3") #send an alarm

        try:
            text = r.recognize_google(audio, language= "en-US") #send to google cloud
            if "hi" in text:
                text = text.replace(text, random.choice(greeting))
            if "how are you" in text:
                text = text.replace(text, random.choice(howAreYou))
            if  "what time" in text:
                now = datetime.now() #get the current time
                text = now.strftime("%H:%M:%S")
                print(now.strftime("%H:%M:%S"))
            if "what can you do" in text:
                text = text.replace(text , random.choice(myAbility))
            if "your name" in text:
                text = text.replace(text , random.choice(myName))
            if "search" in text:
                text = text.replace("search" , "")
                url = text
                wb.open_new_tab("https://www.google.com/search?q=" + url)
                text = "กำลังค้นหา"
            if "close" in text:
                exit
        except:
            text = random.choice(refuse)
        tts = gTTS(text, lang= "en-US" ) #send to google cloud
        tts.save("./answer.mp3") #save voice from google cloud
        playsound("./answer.mp3")
        os.remove("./answer.mp3") #remove audio file


