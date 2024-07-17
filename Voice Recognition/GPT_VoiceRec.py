import speech_recognition as sr
import pyttsx3

#https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#Sesten gelen text üzerinden regex uygulayarak bilgi edinmek

r = sr.Recognizer()
audio = "audio.wav"

def speakTest(command):
    engine = pyttsx3.init("sapi5", False)
    engine.say(command)
    engine.runAndWait()

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration = 0.2)

            audio2 = r.listen(source2)

            text = r.recognize_google(audio2, language = "tr-TR")
            text = text.lower()

            print(f"Did you say: {text}")
            speakTest(text)
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred!")


