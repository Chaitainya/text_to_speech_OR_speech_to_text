# first of all we need to install "SpeechRecognition"
# We can copy the command from this link --> "https://pypi.org/project/SpeechRecognition/", and paste paste it in the terminal in vs code or Command Prompt.
# Command for python 2 --> "pip install SpeechRecognition"
# Command for python 3 --> "pip3 install SpeechRecognition"
# If the requirement is already satisfied it shows "Requirement already satisfied: SpeechRecognition", else it will install.

# now coding
# first we have to import
# writing speech_recognition all the time when we need is not a good idea, so we took it as sr.

import speech_recognition as sr
# This is the only library that we need

# We need to initialize the recognizer
recognizer = sr.Recognizer()  # This will work to recognize our audio

# it can we sr.Microphone or it can be audio file, but we're using "sr.Microphone" here.
with sr.Microphone() as source:
    print("Hey! I'm Chaitanya. Speak anthing that i'll convert to text")

    # We've to listen to the source. So, it'll listen to the source and save it in the audio variable.
    audio = recognizer.listen(source)

    try:
        # and this will convert the audio into text.
        text = recognizer.recognize_google(audio)
        # Whatever we say, it'll print here
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")


# install there two packages if error appear related to these,
# pip install pipwin
# then
# pipwin install pyaudio
