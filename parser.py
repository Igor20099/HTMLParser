# -*- coding: utf-8 -*-
#HTMLParser
#TODO:Сделать рефакторинг!
import requests , bs4
from kivy.app import App
import config
#Импорт виджетов
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#Импортирование настроек экрана
conf = config.Conf()
class ParserApp(App):
    def parse(self,url_input):
            #TODO:Добавить алгортм парсинга
            self.url = requests.get(self.url_input.text)
            self.b = bs4.BeautifulSoup(self.url.text,'html.parser')
            self.tag = self.tag_input.text
            self.p = self.b.select(self.tag)
            self.text = self.p[0].getText()
            self.tit = self.b.select('h1')
            
            self.filename = self.tit[0].getText()
            with open('Chords/'+ self.filename.strip() + '.txt','w') as f:
                f.write(self.text)
    def build(self):
        self.bl = BoxLayout(orientation = 'vertical')
        self.url_bl = BoxLayout(orientation = 'horizontal')
        self.tag_bl = BoxLayout(orientation = 'horizontal')
        self.filename_bl = BoxLayout(orientation = 'horizontal')
        self.url_label = Label(text = 'URL',size_hint = (0.4,1))
        self.tag_label = Label(text ='Tag,class,id',size_hint = (0.4,1))
        self.filename_label = Label(text = 'Filename',size_hint = (0.4,1))
        self.url_input = TextInput()
        self.tag_input = TextInput()
        self.filename_input = TextInput()

        self.url_bl.add_widget(self.url_label)
        self.url_bl.add_widget(self.url_input)
        self.bl.add_widget(self.url_bl)
        
        


        self.btn_parse = Button(text = 'Parse',on_press = self.parse)
       
       

        self.tag_bl.add_widget(self.tag_label)
        self.tag_bl.add_widget(self.tag_input)
        self.bl.add_widget(self.tag_bl)

        self.filename_bl.add_widget(self.filename_label)
        self.filename_bl.add_widget(self.filename_input)
        self.bl.add_widget(self.filename_bl)
        self.bl.add_widget(self.btn_parse)
        

        return self.bl


if __name__ == "__main__":
    ParserApp().run()        
