# -*- coding: utf-8 -*-
#HTMLParser
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
        bl = BoxLayout()
        return bl


if __name__ == "__main__":
    ParserApp().run()        
