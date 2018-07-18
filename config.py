from kivy.config import Config

class Conf:
    def __init__(self):
        #Настройки экрана
        Config.set('graphics','width',320)
        Config.set('graphics','height',480)
        Config.set('graphics','resizable',0)
