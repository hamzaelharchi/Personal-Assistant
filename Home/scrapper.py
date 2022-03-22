import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
import webbrowser
import os
import subprocess as sp

weather_key= "63500e07fa46d117e3af8e5b01ba213f"
def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric").json()
    weather = res["weather"][0]["description"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"



def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+212{number}", message)


def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(s):
    link='https://www.google.com/search?q='+s
    webbrowser.open_new(link)

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

