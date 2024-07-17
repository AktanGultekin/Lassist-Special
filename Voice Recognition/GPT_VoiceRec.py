import speech_recognition as sr
import pyttsx3

#https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#Sesten gelen text üzerinden regex uygulayarak bilgi edinmek

r = sr.Recognizer() # Define the recognizer

def speak_test(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def record_audio(): # Define Record Audio Function
    with sr.Microphone() as source: # Recording Audio while source gives input
        print("Listening...")
        audio = r.listen(source) 
    return audio

def recognize_speech(audio): # Define Recognize Speech Function
    try:
        text = r.recognize_google(audio) # Starting to recognize sound data
        print(f"You said: {text}")
    except sr.UnknownValueError: #Specifying the possible problems and define the answers
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration= 0.2)

            audio2 = r.listen(source2)

            text = r.recognize_google(audio2)
            text = text.lower()

            print("Did you say ", text)
            speak_test(text)
        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

if __name__ == "__main__": # Make it able to work in main
    audio = record_audio() 
    recognize_speech(audio)





