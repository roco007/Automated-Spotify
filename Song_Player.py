import pyttsx3
import speech_recognition as sr
from datetime import datetime
import geocoder
import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
import math
import os
import subprocess
import time
from playsound import playsound
import winsound
import selenium
from pywinauto import application
import pyautogui as pa
from pynput.keyboard import Key, Controller
import sys
import screen_brightness_control as sbc
from SimiNames import SimiNames as s



k = Controller()
a = application.Application()
b = application.Application()
engine = pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty("voice", sound[1].id)
listener = sr.Recognizer()
i=0

w,h=pa.size()
name=''
song=''
z=0

def listen:
  while True:
    try:
        with sr.Microphone as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            name = command.lower()
            if name == 'left' or name == 'right':
                return name
            else:
                pass
    except:
        pass




while True:

    print('....')
    if name == 'resume':
        a.start('C://Users\91967\AppData\Roaming\Spotify\Spotify.exe')
        time.sleep(5)
        pa.doubleClick(0.50 * w, 0.92 * h + 5)
        print(pa.getActiveWindowTitle())
        pa.getActiveWindow()
    while True:


        try:
            with sr.Microphone() as source:
                i=i+1
                print(str(i)+' listening....')
                voice = listener.listen(source, phrase_time_limit=4)
                command = listener.recognize_google(voice)
                name = command.lower()
                print(name)
                if any(wrds in name for wrds in s.alxa_stp):
                    os.system('TASKKILL /F /IM Spotify.exe')
                    z=0
                    print('intends to stop')

                elif any(wrds in name for wrds in s.mxmze) :
                    a.start('C://Users\91967\AppData\Roaming\Spotify\Spotify.exe')

                elif any(wrds in name for wrds in s.ps_pl):
                    a.start('C://Users\91967\AppData\Roaming\Spotify\Spotify.exe')
                    time.sleep(2)
                    pa.press('space')

                elif 'recent' in name:

                     pa.keyDown('alt')
                     pa.press('tab')
                     while True:
                         a=listen()

                         if a=='right':
                              pa.press('right')
                         elif a=='left':
                               pa.press('left')
                         elif a=='enter' or a=='ok' or a=='okay':
                             break

                     pa.keyUp('alt')


                elif 'minimize' in name or'minimise' in name:
                    pa.click(91.93 * w / 100, 0.6 * h / 100)



                elif 'volume' in name:

                    if 'full' in name or '100' in name:
                        os.system('SetVol 100')

                    elif '+' in name or '-' in name:

                        v=v=name[len(name)-4:]
                        os.system('SetVol ' + str(v))
                    else:
                        v=name.replace('volume','')

                        v=name[len(name)-2:]

                        os.system('SetVol '+ str(v))

                    print('Volume is changed ')

                elif 'brightness' in name:

                    if 'full' in name or '100' in name:
                        sbc.set_brightness('100')

                    elif '+' in name or '-' in name:

                        v=name[len(name)-4:]
                        sbc.set_brightness(v)
                    else:
                        v=name.replace('brightness','')

                        v=name[len(name)-2:]

                        sbc.set_brightness(v)

                    print('Brightness is changed ')

                elif 'alexa' in name:

                    if z==0:
                       z=1
                       pass
                    elif z==1:
                        a.start('C://Users\91967\AppData\Roaming\Spotify\Spotify.exe')
                        time.sleep(2)
                        pa.press('space')
                    break



                else:
                    pass
        except:
            pass

    while True:
        try:
            engine.say('Which song would you like to listen to?')
            engine.runAndWait()

            with sr.Microphone() as source:
                #playsound('command.mp3')
                voice = listener.listen(source,  phrase_time_limit=4)
                command = listener.recognize_google(voice)
                name = command.lower()
                print(name)
                if 'play ' in name:
                    song=name[5:]
                    print(song)
                break


        except:
              print('Didn\'t hear the song name.')




    if name == 'resume':
        pass

    else:
        engine.say('playing ' + name + ', Spotify')
        engine.runAndWait()
        a.start('C://Users\91967\AppData\Roaming\Spotify\Spotify.exe')
        time.sleep(5)
        # x=29.17%*total_width,y=2.22%*total height srch dialogue box along with 'x' to cancel previous written text if any
        #pa.click(29.17 * w / 100, 2.22 * h / 100)

        pa.click(560, 24)#... FOR MY LAPTOP
        pa.typewrite(name)
        pa.press('enter')
        time.sleep(5)
        # x=19.33% *total wt, y=25.28% * total ht  (includes 70 of toggle bar space) for play button
        #pa.doubleClick(19.33*w/100,25.28*h/100 )
        pa.doubleClick(371, 273)#... FOR MY LAPTOP
        time.sleep(5)


        # x=91.93% *total wt, y=0.6% * total ht....MINIMIZE BUTTON
        #pa.click(91.93*w/100,0.6*h/100 )
        #pa.click(1765, 7)  # ... FOR MY LAPTOP



