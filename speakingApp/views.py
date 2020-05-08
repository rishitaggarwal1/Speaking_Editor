from django.shortcuts import render
import pyttsx3


def home(request):
    if request.method == "POST":
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 125)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        s = request.POST['sound']
        sound = int(s)
        engine.setProperty('voice', voices[sound].id)
        if request.POST['text']:
            text = request.POST['text']
            engine.say(text)
            engine.runAndWait()
        if request.POST['upload']:
            file = request.POST['upload']
            print(file)
    return render(request, 'home.html', {})
