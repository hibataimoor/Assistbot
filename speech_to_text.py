import speech_recognition as sr
import os

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
        print("Recording audio for 10 seconds...")
        recorded_audio = recognizer.listen(source, timeout = 10)
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

except sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand the audio.")
except sr.RequestError:
    print("Couldn't request results from Google Speech Recognition service.")
except Exception as ex:
    print("Error during recognition: ", ex)