from kivy.core.audio import SoundLoader
from kivy.graphics import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
class Marker:
    def __init__(self, kind, pos):
        self.kind = kind
        self.pos = pos

class DrawingBoard:
    def __init__(self):
        self.time_one = "00:00"
        self.time_two = "00:01"
        self.time_three = "00:02"

        self.start = 0
        self.end = 3

        self.markers = [] 

class MarkerPage(BoxLayout):
    pass

    def draw_drawing_board(self):
        board = self.ids.drawing_board
        with self.canvas:
            Color(1., 0, 0)
            self.drawing_board = Rectangle(pos=board.pos, size=board.size)

class StapleApp(App):
    def build(self):
        self.metro_sound = SoundLoader.load('metro.wav')
        self.song_sound = SoundLoader.load('mytest.wav')
        self.drawing_board = DrawingBoard();


        #self.test_marker_one Marker("Cut", ) :
        return MarkerPage()


if __name__ == '__main__':
    StapleApp().run()
