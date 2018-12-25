from pygame import mixer
import pygame
import time
import speech_recognition as sr
import paho.mqtt.publish as publish

r = sr.Recognizer()

def play_despacito():
    mixer.init()
    mixer.music.load('/Users/Jesse/Desktop/Carbot/se101-f18-group-ejchen-j294sun/despacito.mp3')
    mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def get():
    try:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        print(command)
        if(command == "play despacito"):
            print(True)
            play_despacito()
        if(command == "forward"):
            publish.single("carbot/server", payload="Forward", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        if(command == "left"):
            publish.single("carbot/server", payload="Left", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        if(command == "back"):
            publish.single("carbot/server", payload="Back", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        if(command == "right"):
            publish.single("carbot/server", payload="Right", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        if(command == "stop"):
            publish.single("carbot/server", payload="Stop", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

with sr.Microphone() as source:
    while True:
        get()
