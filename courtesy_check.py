import speech_recognition as sr
import os
import gtts
from playsound import playsound
from time import sleep
from twilio.rest import Client

account_sid = "AC7016d23742fe76c7bed711f5c6917841"
auth_token  = "179f00c3098d67675386f42e4cb47405"
client = Client(account_sid, auth_token)
recognizer = sr.Recognizer()

try:
    # List available microphones
    print("Available microphones:")
    print(sr.Microphone.list_microphone_names())

    # Select a specific microphone (optional)
    # with sr.Microphone(device_index = 1) as source:

    with sr.Microphone() as source:
        print("Adjusting noise...")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        tts = gtts.gTTS("Hello. Are you ok?")
        tts.save("hello.mp3")
        sleep(5)
        playsound("hello.mp3")
        print("Recording audio for 15 seconds...")
        recorded_audio = recognizer.listen(source, 14, 10)
        print("Done recording.")

except sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand the audio.")
except sr.RequestError:
    print("Couldn't request results from Google Speech Recognition service.")
except Exception as ex:
    print("Error during recognition: ", ex)
    
try:
    print("Recognizing the text..")
    text = recognizer.recognize_google(recorded_audio, language = "en-US")
    print("Decoded Text: {}".format(text))
    if 'yes' in text:
        tts = gtts.gTTS("Thats great!")
        tts.save("check.mp3")
        playsound("check.mp3")

        #If response is no, reply, Ok, I will call someone to come and check on you.
    if 'no' in text:
        tts = gtts.gTTS("Ok, I will call someone to come and check on you.")
        tts.save("check.mp3")
        playsound("check.mp3")
        call = client.calls.create(to="8177055751",
                        from_="8336083203",
                        twiml='<Response><Say>Hello there. The person says that they are not okay. Please check on them.</Say></Response>')
        print(call.sid)
except sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand the audio.")
except sr.RequestError:
    print("Couldn't request results from Google Speech Recognition service.")
except Exception as ex:
    print("Error during recognition: ", ex)