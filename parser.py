# -*- coding: utf-8 -*-
#HTMLParser
#TODO:Сделать рефакторинг!
import requests , bs4
from kivy.app import App
from kivy.config import Config

#Импорт виджетов
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#Настройки экрана
Config.set('graphics','width',640)
Config.set('graphics','height',480)
Config.set('graphics','resizable',0)


class ParserApp(App):
    def build(self):
        def parse(self):
            pass
        self.bl = BoxLayout()
        self.url_label = Label(text = 'URL')
        self.tag_label = Label(text ='Tag,class,id')
        self.filename_label = Label(text = 'Filename')
        self.url_input = TextInput()
        self.tag_input = TextInput()
        self.filename_input = TextInput()
        self.btn_parse = Button(text = 'Parse')
        return self.bl


if __name__ == "__main__":
    ParserApp().run()        
