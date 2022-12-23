from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from PyPDF2 import PdfReader
import os

TITLE_COLOR = "#00ADB5"
WORD_FONT = ("Times New Roman", 20)
WORD_COLOR = "#EEEEEE"
BACKGROUND_COLOR = "#222831"
BTN_BACKGROUND_COLOR = "#393E46"

def open_pdf():
    global audio_name
    
    pdf_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
    )
    
    reader = PdfReader(pdf_file)
    pdf_content = ""
    for page in reader.pages:
        pdf_content += page.extract_text() + "\n"
    
    pdf_name = os.path.split(pdf_file)[1].split(".pdf")[0]
    audio_name = f'{pdf_name}-audio.mp3'
    tts = gTTS(text=pdf_content, lang='en')
    tts.save(audio_name)
    
    play_btn.config(fg=TITLE_COLOR)

def play_audio():
    os.startfile(audio_name)


screen = Tk()
screen.title('PDF to Audio')
screen.config(padx=40, pady=20, bg=BACKGROUND_COLOR)

canvas=Canvas(width=260,height=260,background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
logo_img=PhotoImage(file='logo.png')
canvas.create_image(130,130,image=logo_img)
canvas.grid(row=0,column=0,pady=20)

open_btn = Button(
    text="1. Select PDF", 
    font=WORD_FONT, 
    width=15, 
    fg=WORD_COLOR, 
    bg=BTN_BACKGROUND_COLOR, 
    command=open_pdf
    )

play_btn = Button(
    text="2. Play Audio", 
    font=WORD_FONT, 
    width=15, 
    fg=WORD_COLOR, 
    bg=BTN_BACKGROUND_COLOR,
    command=play_audio
    )

open_btn.grid(column=0, row=1, pady=5)
play_btn.grid(column=0, row=2, pady=5)

screen.mainloop()