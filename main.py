from interactive_en import *  #for responsive to user english
from interactive_th import *  #for responsive to user thai
from tkinter import * #make gui

"""def btnTH():
    chooseLang = "th"
    interactive = interactive_th
    speechRocognition("th", interactive)
def btnEN():
    chooseLang = "en-US"
    interactive = interactive_en
    speechRocognition("en-US", interactive)"""

"""chooseLang = "th"
interactive = interactive_th"""


"""def speechRocognitionLoop():
    while True:
        speechRocognition()"""

root=Tk()
root.geometry("300x300")
root.title("speech recognition")
root.configure()

label = Label(text="เลือกภาษาข้างล่าง / choose language below").pack()
btnTh = Button(text="พูด", command= speechRocognitionTh).pack(ipadx=15, ipady=10)
btnEn = Button(text="speech", command= speechRocognitionEn).pack(ipadx=15, ipady=10)

root.mainloop()

