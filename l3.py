# Import the following module
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from googletrans import Translator 
from tkinter import messagebox
import pyperclip as pc 
from gtts import gTTS  
import os
import speech_recognition as spr


''' This python file consist of all functionalities required for the language translator application to work  '''

# UI is developed using Tkinter library
root = tk.Tk()
root.title('Langauge Translator')
root.geometry('1060x660')
root.maxsize(1060, 660)
root.minsize(1060, 660)
# Tittle bar icon image used in Tkinter GUI
title_bar_icon = PhotoImage(file="image copy 3.png")
root.iconphoto(False,title_bar_icon)
cl =''
output=''

# For Performing Main Translation Function
def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:
         t2.delete(1.0, 'end')
         translator = Translator()
         global output
         output = translator.translate(language_1, dest=cl)
         output = output.text
         t2.insert('end', output)

# For Clearing Textbox Data
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# For Copying Textbox Data after Translation
def copy():
    pc.copy(str(output))

# For Converting Translated Text to Speech
def texttospeech():
    global cl
    cl = choose_langauge.get()
    
    if os.path.exists("text_to_speech.mp3"):
        os.remove("text_to_speech.mp3")
        
    mytext = output
    language = 'en'  # Default to English

    language_codes = {
        'Afrikaans': 'af',
        'Albanian': 'sq',
        'Arabic': 'ar',
        'Armenian': 'hy',
        'Azerbaijani': 'az',
        'Basque': 'eu',
        'Belarusian': 'be',
        'Bengali': 'bn',
        'Bosnian': 'bs',
        'Bulgarian': 'bg',
        'Catalan': 'ca',
        'Cebuano': 'ceb',
        'Chinese': 'zh',
        'Corsican': 'co',
        'Croatian': 'hr',
        'Czech': 'cs',
        'Danish': 'da',
        'Dutch': 'nl',
        'English': 'en',
        'Esperanto': 'eo',
        'Estonian': 'et',
        'Finnish': 'fi',
        'French': 'fr',
        'Frisian': 'fy',
        'Galician': 'gl',
        'Georgian': 'ka',
        'German': 'de',
        'Greek': 'el',
        'Gujarati': 'gu',
        'Haitian Creole': 'ht',
        'Hausa': 'ha',
        'Hawaiian': 'haw',
        'Hebrew': 'he',
        'Hindi': 'hi',
        'Hmong': 'hmn',
        'Hungarian': 'hu',
        'Icelandic': 'is',
        'Igbo': 'ig',
        'Indonesian': 'id',
        'Irish': 'ga',
        'Italian': 'it',
        'Japanese': 'ja',
        'Javanese': 'jv',
        'Kannada': 'kn',
        'Kazakh': 'kk',
        'Khmer': 'km',
        'Kinyarwanda': 'rw',
        'Korean': 'ko',
        'Kurdish': 'ku',
        'Kyrgyz': 'ky',
        'Lao': 'lo',
        'Latin': 'la',
        'Latvian': 'lv',
        'Lithuanian': 'lt',
        'Luxembourgish': 'lb',
        'Macedonian': 'mk',
        'Malagasy': 'mg',
        'Malay': 'ms',
        'Malayalam': 'ml',
        'Maltese': 'mt',
        'Maori': 'mi',
        'Marathi': 'mr',
        'Mongolian': 'mn',
        'Myanmar': 'my',
        'Nepali': 'ne',
        'Norwegian': 'no',
        'Odia': 'or',
        'Pashto': 'ps',
        'Persian': 'fa',
        'Polish': 'pl',
        'Portuguese': 'pt',
        'Punjabi': 'pa',
        'Romanian': 'ro',
        'Russian': 'ru',
        'Samoan': 'sm',
        'Scots Gaelic': 'gd',
        'Serbian': 'sr',
        'Sesotho': 'st',
        'Shona': 'sn',
        'Sindhi': 'sd',
        'Sinhala': 'si',
        'Slovak': 'sk',
        'Slovenian': 'sl',
        'Somali': 'so',
        'Spanish': 'es',
        'Sundanese': 'su',
        'Swahili': 'sw',
        'Swedish': 'sv',
        'Tajik': 'tg',
        'Tamil': 'ta',
        'Tatar': 'tt',
        'Telugu': 'te',
        'Thai': 'th',
        'Turkish': 'tr',
        'Turkmen': 'tk',
        'Ukrainian': 'uk',
        'Urdu': 'ur',
        'Uyghur': 'ug',
        'Uzbek': 'uz',
        'Vietnamese': 'vi',
        'Welsh': 'cy',
        'Xhosa': 'xh',
        'Yiddish': 'yi',
        'Yoruba': 'yo',
        'Zulu': 'zu'
    }

    language = language_codes.get(cl, 'en')  # Get the language code or default to 'en'
    
    try:
        if mytext:
            print(f"Converting text to speech for language: {cl}, code: {language}")
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("text_to_speech.mp3")
            os.system("start text_to_speech.mp3" if os.name == "nt" else "open text_to_speech.mp3")
        else:
            messagebox.showerror('Language Translator', 'No text available for conversion to speech')
    except ValueError as e:
        messagebox.showerror('Language Translator', f"{cl} is currently not supported for Read Aloud (Text to Speech)")
        print(f"An error occurred: {e}")
    except AssertionError as e:
        messagebox.showerror('Language Translator', 'Please enter the data to be translated before using Read Aloud')
        print("Error:", e)

# For converting Speech to Text [ Please Note : Only English is currently supported as from-language in Speech to Text Translation ]
def speechtotext():
    cl = choose_langauge.get()
    language = 'en'

    if cl == 'English':
        language = 'en'
    else:
        messagebox.showerror('Language Translator', 'Only English is currently supported for speech-to-text input')
        return

    from_lang = "en"
    to_lang = language

    recog1 = spr.Recognizer()
    mc = spr.Microphone()

    try:
        with mc as source:
            t1.insert("end", "Listening...\n")
            recog1.adjust_for_ambient_noise(source, duration=0.9)
            audio = recog1.listen(source)
            get_sentence = recog1.recognize_google(audio)

            t1.insert("end", "You said: " + get_sentence + "\n")
            translator = Translator()
            text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
            text = text_to_translate.text

            speak = gTTS(text=text, lang=to_lang, slow=False)
            global output
            output = text
            t2.insert("end", output + "\n")
            translate()

    except spr.UnknownValueError:
        t1.insert("end", "Unable to Understand the Input\n")
        messagebox.showerror('Language Translator', 'Unable to Understand the Input')
    except spr.RequestError as e:
        t1.insert("end", f"Unable to provide Required Output; {e}\n")
        messagebox.showerror('Language Translator', 'Unable to provide Required Output'.format(e))
    except Exception as e:
        t1.insert("end", f"An error occurred: {e}\n")
        messagebox.showerror('Language Translator', f"An error occurred: {e}")


# Background Image settings using Tkinter
img = ImageTk.PhotoImage(Image.open('image copy 2.png'))
label = Label(image=img)
label.place(x=0, y=0)

# combobox for from-language selection
a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20,textvariable=a, state='readonly', font=('Corbel', 20, 'bold'), )

auto_detect['values'] = (
    'Auto Detect',
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

auto_detect.place(x=50, y=140)
auto_detect.current(0)
l = tk.StringVar()

# combobox for to-language selection
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=600, y=140)
choose_langauge.current(0)

# Load and resize the icon images for buttons
translate_text_icon_img = Image.open("image copy 6.png")
resized_translate_text_icon = translate_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
translate_text_icon = ImageTk.PhotoImage(resized_translate_text_icon)

clear_text_icon_img = Image.open("image copy 5.png")
resized_clear_text_icon = clear_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
clear_text_icon = ImageTk.PhotoImage(resized_clear_text_icon)

copy_text_icon_img = Image.open("image copy 4.png")
resized_copy_text_icon = copy_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
copy_text_icon = ImageTk.PhotoImage(resized_copy_text_icon)

read_aloud_icon_img = Image.open("image copy.png")
resized_read_aloud_icon = read_aloud_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
read_aloud_icon = ImageTk.PhotoImage(resized_read_aloud_icon)

voice_input_icon_img = Image.open("image.png")
resized_voice_input_icon = voice_input_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
voice_input_icon = ImageTk.PhotoImage(resized_voice_input_icon)


# Text Widget settings used in Tkinter GUI
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t2.place(x=550, y=200)

# Button settings used in Tkinter GUI
translate_button = Button(root, text=" Translate Text ",image=translate_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=translate,bg="#ffffff")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ",image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
               command=clear,bg="#ffffff")
clear_button.place(x=270, y=565)

copy_button = Button(root, text=" Copy ",image=copy_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=copy,bg="#ffffff")
copy_button.place(x=485, y=565)

read_aloud = Button(root, text=" Read Aloud ",image=read_aloud_icon, compound="right" ,relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=texttospeech,bg="#ffffff")
read_aloud.place(x=650, y=565)

voice_input = Button(root, text=" Voice Input ", image=voice_input_icon, compound="right", relief=RIDGE, borderwidth=0,
                     font=('Corbel', 20, 'bold'), cursor="hand2", command=speechtotext, bg="#ffffff")
voice_input.place(x=850, y=565)

root.mainloop()