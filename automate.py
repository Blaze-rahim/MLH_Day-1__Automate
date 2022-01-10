import pywhatkit
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

try:
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
              

        audio2 = r.listen(source2)
              

        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        print("Playing "+MyText)
        SpeakText(MyText)

except:
    pass

try:
  pywhatkit.playonyt(MyText)
  print("Playing...")
 
except:
   
  # printing the error message
  print("Network Error Occured")
 