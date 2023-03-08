from kivy.clock import Clock 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader

class Staple(App):
    def build(self):
        self.sound = SoundLoader.load('mytest.wav')
        self.marker_sound = SoundLoader.load('metro.wav')
        self.sound_two = SoundLoader.load('mytest.wav')
        self.playing = True

        self.window = GridLayout()
        self.window.cols = 1
        self.window.rows = 5
        self.window.size_hint = (0.9, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y" :0.5 }

        #Layer 0

        #Layer 1

        self.grid_layer_one = GridLayout()
        self.grid_layer_one.size_hint = (1, .2) 

        self.grid_layer_one.cols = 5

        self.button_next_chunk = Button(
                        text = "->",
                        size_hint = (.2, .2)
                        )   
        self.button_shift_forward = Button(
                        text = ">",
                        size_hint = (.2, .2)
                        )   
        self.button_next_chunk.bind(on_press = self.play)
            
        self.float_layer_one = FloatLayout()

        self.position_bar = Slider(orientation = "horizontal")

        self.button_last_chunk = Button(
                        text = "<-",
                        size_hint = (.2, .2)
                        )
        self.button_shift_backward = Button(
                        text = "<",
                        size_hint = (.2, .2)
                        )

        self.button_last_chunk.bind(on_press = self.stop)

        self.grid_layer_one.add_widget(self.button_last_chunk)
        self.grid_layer_one.add_widget(self.button_shift_backward)
        self.grid_layer_one.add_widget(self.position_bar)
        self.grid_layer_one.add_widget(self.button_shift_forward)
        self.grid_layer_one.add_widget(self.button_next_chunk)

        #Layer 1+n
        self.grid_layer_two = FloatLayout() 

        self.temp_float = FloatLayout()

        self.window.add_widget(self.grid_layer_one)
        self.window.add_widget(self.grid_layer_two)
        self.window.add_widget(self.temp_float)
        return self.window

    def play(self, value):
        self.marker_sound.play()

    def play_two(self, value):
        self.sound_two.play()

    def stop(self, value):
        self.playing = False
        

if __name__ == "__main__":
        Staple().run() 
