import pyttsx3

while True:
    voice = pyttsx3.init()
    x=input("Enter what you want you speak to me:")
    if x=="z":
        voice.say("say 'bye bye friend'")
        break
    command=f"{x}"
    voice.say(command)
    voice.runAndWait()