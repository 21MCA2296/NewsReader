# 978d11cb725942218bec2ff3d4404cb3
import requests
import time
from datetime import datetime
import json
from win32com.client import Dispatch
# import win32com

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':

    url= "http://newsapi.org/v2/top-headlines?country=in&apiKey=978d11cb725942218bec2ff3d4404cb3"
    news = requests.get(url).text
    # print(news)
    loaded_file = json.loads(news)
    # print(loaded_file["totalResults"])
    # speak(loaded_file["articles"]["title"])
    speak("News for today..")
    

    articles = loaded_file["articles"]
    print("--------------------TIMES OF INDIA---------------------")
    print("\n\n\n\t\t\t Date:",time.strftime('%Y-%m-%d'))#
    
    for art in articles:
    
        speak(art['title'])
        speak(art['description'])
        print(art["url"])
        speak("for more news.... click on the link given below")
        speak("Now.... the next news...")
       
    

    