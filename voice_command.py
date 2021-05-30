import speech_recognition as sr
from os import system as command_

uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWX"
lowercase_alphabet = "abcdefghijklmnopqrstuvwx"

def lower(text:str):
    new_text = str()
    for i in text:
        if i in uppercase_alphabet:
            index = uppercase_alphabet.index(i)
            new_text += lowercase_alphabet[index]

        else:
            new_text += i

    return new_text

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    command_("cls") # for MacOs 'clear'
    print("Say: Run the program")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
flag = False

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use 'r.recogine_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of 'r.recognize_google(audio)'
    text = r.recognize_google(audio, language = "eng")
    print("Perceived: " + text)
    flag = True
    text = lower(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if flag:
    if text == "run the program":
        command_("atom")
