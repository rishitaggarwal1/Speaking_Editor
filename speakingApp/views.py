from django.shortcuts import render
import pyttsx3


def home(request):
    if request.method == "POST":
        text = request.POST['text']
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 125)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    return render(request, 'home.html', {})
