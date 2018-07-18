from kivy.config import Config

class Conf:
    def __init__(self):
        #Настройки экрана
        Config.set('graphics','width',800)
        Config.set('graphics','height',120)
        Config.set('graphics','resizable',0)
