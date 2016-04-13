from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import speech_recognition as sr
from PyDictionary import PyDictionary
import os
import time


def firefox(websites):
	default=webdriver.FirefoxProfile('C:\\Users\\Bharath_BaBu\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\hfuu3cnu.default')
	driver = webdriver.Firefox(default)
	links={'google':'http://www.google.com','facebook':'http://www.facebook.com','hotmail':'http://www.hotmail.com','manga':'http://www.mangapanda.com/one-piece','news':'http://www.msn.in','fb':'http://www.facebook.com'}
	for i in websites:
		print links[i]
		
		driver.get(links[i])


		k.press_key(k.control_key)
		k.tap_key('t')
		k.release_key(k.control_key)


def mediaplayer(websites):
	os.startfile('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
	time.sleep(3)

	k.tap_key(k.tab_key)
	
	k.tap_key(k.return_key)

def gameranger(websites):
	os.startfile('C:\Users\Bharath_BaBu\AppData\Roaming\GameRanger\GameRanger\GameRanger.exe')

def idm(websites):
	os.startfile('C:\Program Files (x86)\Internet Download Manager\IDMan.exe')

def telegram(websites):
	os.startfile('C:\Users\Bharath_BaBu\AppData\Roaming\Telegram Desktop\Telegram.exe')

def windows(websites):
	os.startfile('E:\\')
def parsespeech(word):
	functions=[]
	links=[]
	parsed=[]
	word=word.lower()
	sentence=word.split()
	for i in sentence:

		if (i=='fire' or 'fox' or 'firefox'):
			functions.append(i)
		if (i=='media'):
			functions.append(i)
		if (i=='ranger'):
			functions.append(i)
		if (i=='idm'):
			functions.append(i)
		if (i=='telegram'):
			functions.append(i)
		if (i=='windows'):
			functions.append(i)
		if (i=='google'):
			links.append(i)
		if (i=='facebook' or i=='fb'):
			links.append(i)
		if (i=='hotmail'):
			links.append(i)
		if (i=='manga'):
			links.append(i)
		if (i=='news'):
			links.append(i)	
	parsed=[functions,links]
	return parsed



r = sr.Recognizer()
m = sr.Microphone()
k=PyKeyboard()
M=PyMouse()

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
except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Plese Check your internet Connection")

parsed=parsespeech(word)
functions=parsed[0]
links=parsed[1]

print links
action={'firefox':firefox,'media':mediaplayer,'ranger':gameranger,'idm':idm,
'telegram':telegram,'windows':windows,'fire':firefox,'fox':firefox}
for i in functions:
	action[i](links)





