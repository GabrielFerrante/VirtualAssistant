#-*- coding: utf-8 -*-

#importando os módulos do chatbot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import speech_recognition as sr

bot = ChatBot('Jarvis', read_only = True)

#Treinando o modelo de acordo com arquivos
trainer = ListTrainer(bot)

for _file in os.listdir('chats'): #percorrer todos os arquivos em chats
    lines = open('chats/'+ _file, 'r').readlines() #vamos ler linhas
    trainer.train(lines)


#Treinando com a biblioteca
trainer.train("chatterbot.corpus.Portuguese")

#Lendo o microfone

r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    while True:
        try:
            audio = r.listen(s)
            speech = r.recognize_google(audio,language='pt-BR',show_all=False)
            print ("Você disse: ", speech)
            print("Bot disse: ",bot.get_response(speech))

        except:
            print("Não foi possível interpretar")

        

