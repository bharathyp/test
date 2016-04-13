import speech_recognition as sr
from PyDictionary import PyDictionary


dictionary=PyDictionary()

r = sr.Recognizer()
m = sr.Microphone()


print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))

print("Say The Word....")
with m as source: audio = r.listen(source)
print("Got it! Now to recognize it...")
try:
    # recognize speech using Google Speech Recognition
    value = r.recognize_google(audio)
    word=str(value)
    print word
    word=word.replace(' ','')
    print word

except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Plese Check your internet Connection")
if(type(None)!=type(dictionary.googlemeaning(word))):

	print('\n\n\n'+dictionary.googlemeaning(word))
else:
	print "Even Google Doesn't Know Its Meaning ...!!!!!!!"
