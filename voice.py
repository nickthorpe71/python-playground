import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Mocriphone() as source:
	print("Say something!")
	audio = recognizer.listen(source)

print("You said:")
print(recognizer.recognize_google(audio))
