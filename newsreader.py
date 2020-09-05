import requests
import json

def speak(strr):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(strr)

url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=7d252cc8b0624836b5fc14a1cedf295c"

data=requests.get(url).text           #request.get(url) get data from url .text get text

dict1=json.loads(data)                 #convert json to dictionary loads-str as input
#jobj=json.dumps(dict1)                #convert dict to json

speak("Todays Entertainment News of India are")
for i,art in enumerate(dict1["articles"]):
    print("Headline No :",i+1)
    speak(art["title"])
    if i!=len(dict1["articles"])-1:
        speak("Next headline is")
    else:
        speak("News Ended")