from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class metaapp(App):
    def build(self):
        return metaapp()

if __name__ == '__main__':
    metaapp().run()
