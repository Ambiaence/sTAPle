from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider


class Marker(BoxLayout):
    pass


class StapleApp(App):
    def build(self):
        return Marker()


if __name__ == '__main__':
    StapleApp().run()
