import speech_recognition as sr  #speech to text
from gtts import gTTS #text to speech
from playsound import playsound #run mp3 audio
from datetime import datetime #get datetime now
import os as os #remove file
import webbrowser as wb #search browser 
import random #random choice for responsive

#variable
greeting = ["สวัสดีค่ะ", "สวัสดีค่ะ ดีใจที่ได้ยินเสียงคุณนะคะ"]
howAreYou = ["สบายดีค่ะ","ยอดเยี่ยมค่ะ วันนี้อากาศดีนะคะ"]
askBack = ["หวังว่าคุณจะรู้สึกเหมือนฉันนะคะ", "ขอบคุณที่ถามนะคะ"]
myAbility = ["ฉันทำอะไรไม่ได้มาก แต่ในอนาคตฉันพัฒนาตัวเอง คุณสามรถอ่านรายละเอียดเกี่ยวกับฉันได้นะคะ"]
myName = ["ฉันชื่อ โมนิกา","ฉันชื่อ โมนิกา ชื่อน่ารักใช่ไหมคะ"]
refuse = ["ขอโทษ ฉันไม่เข้าใจค่ะ"]

#functions
def speechRocognitionTh():
    r = sr.Recognizer() #run Initiate
    with sr.Microphone() as source: 
        playsound("./beep.mp3") #send an alarm
        audio = r.record(source, duration=4) #record voice 4 secconds
        playsound("./beep.mp3") #send an alarm

        try:
            text = r.recognize_google(audio, language= "th") #send to google cloud
            if "สวัสดี" in text:
                text = text.replace(text, random.choice(greeting))
            if "เป็นอย่างไร" in text:
                text = text.replace(text, random.choice(howAreYou))
            if  "กี่โมงแล้ว" in text:
                now = datetime.now() #get the current time
                text = now.strftime("%H:%M:%S")
                print(now.strftime("%H:%M:%S"))
            if "ทำอะไรได้บ้าง" in text:
                text = text.replace(text , random.choice(myAbility))
            if "ชื่ออะไร" in text:
                text = text.replace(text , random.choice(myName))
            if "ค้นหา" in text:
                text = text.replace("ค้นหา" , "")
                url = text
                wb.open_new_tab("https://www.google.com/search?q=" + url)
                text = "กำลังค้นหา"
            if "ปิดการใช้งาน" in text:
                exit
        except:
            text = random.choice(refuse)
        tts = gTTS(text, lang= "th" ) #send to google cloud
        tts.save("./answer.mp3") #save voice from google cloud
        playsound("./answer.mp3")
        os.remove("./answer.mp3") #remove audio file
