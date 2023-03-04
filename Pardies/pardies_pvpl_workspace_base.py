#KIVY LIBARY
from kivy.graphics import Color, Rectangle, Triangle
from kivy.graphics.instructions import VertexInstruction
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.filechooser import FileChooserListView

#OTHER LIBARIES
import os
import shutil

#PARDIES IMPORTS
import pardies_configuration




#BLOCK BASE
class Block(RelativeLayout):
    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.block_button = Button(background_color = (1, 1, 1, 0))
        self.contents_anchor = AnchorLayout(anchor_x = "center", anchor_y = "center")
        self.contents = BoxLayout(orientation = "horizontal", size_hint = (1, 0.75))
        buffer = Widget(size_hint = (None, 1), size = (10, 69))
        self.contents.add_widget(buffer)
        self.contents_anchor.add_widget(self.contents)
class BlockBase(DragBehavior, Block):
    def __init__(self, **kwargs):
        super(BlockBase, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.drag_rectangle = (0, 0, 1920, 1080)
        self.block_number = None
        self.created = False
        self.init = False
    def on_pos(self, instance, value):
        if self.init == False:
            self.init = True
        elif self.block_number not in self.parent.movers:
            self.parent.movers.append(self.block_number)




#... = ...
class FirstBlock(BlockBase):
    def __init__(self, **kwargs):
        super(FirstBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (185, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "=", size_hint = (None, 1), size = (15, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "FirstBlock"
        self.size = (185, 35)
        self.pos = (10, 100)




#... = list: ...
class SecondBlock(BlockBase):
    def __init__(self, **kwargs):
        super(SecondBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (220, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "=", size_hint = (None, 1), size = (15, 69)))
        self.contents.add_widget(Label(text = "list: ", size_hint = (None, 1), size = (35, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "SecondBlock"
        self.size = (220, 35)
        self.pos = (10, 55)




#... = dictionary: ...
class ThirdBlock(BlockBase):
    def __init__(self, **kwargs):
        super(ThirdBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (265, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "=", size_hint = (None, 1), size = (15, 69)))
        self.contents.add_widget(Label(text = "dictionary: ", size_hint = (None, 1), size = (80, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "ThirdBlock"
        self.size = (265, 35)
        self.pos = (10, 10)




#define ... placeholders ( ... ):
class FourthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(FourthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (340, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "define", size_hint = (None, 1), size = (50, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "placeholders", size_hint = (None, 1), size = (98, 69)))
        self.contents.add_widget(Label(text = "(", size_hint = (None, 1), size = (12, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Label(text = "):", size_hint = (None, 1), size = (15, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "FourthBlock"
        self.size = (340, 35)
        self.pos = (300, 100)




#return ...
class FifthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(FifthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (145, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "return", size_hint = (None, 1), size = (50, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "FifthBlock"
        self.size = (145, 35)
        self.pos = (300, 55)




#wait ... seconds
class SixthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(SixthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (165, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "wait", size_hint = (None, 1), size = (40, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "seconds", size_hint = (None, 1), size = (65, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "SixthBlock"
        self.size = (165, 35)
        self.pos = (300, 10)




#+ ... through ... as ... :
class SeventhBlock(BlockBase):
    def __init__(self, **kwargs):
        super(SeventhBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (310, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "+", size_hint = (None, 1), size = (10, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "through", size_hint = (None, 1), size = (62, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Label(text = "as", size_hint = (None, 1), size = (23, 69)))
        self.block_third_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_third_text)
        self.contents.add_widget(Label(text = ":", size_hint = (None, 1), size = (10, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "SeventhBlock"
        self.size = (310, 35)
        self.pos = (675, 100)




#swap ... and ...
class EighthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(EighthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (247, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "swap", size_hint = (None, 1), size = (42, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = "and", size_hint = (None, 1), size = (35, 69)))
        self.block_second_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_second_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "EighthBlock"
        self.size = (247, 35)
        self.pos = (675, 55)




#delete ...
class NinthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(NinthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (145, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "delete", size_hint = (None, 1), size = (50, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "NinthBlock"
        self.size = (145, 35)
        self.pos = (675, 10)
        



#try:
class TenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(TenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (40, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "try:", size_hint = (None, 1), size = (25, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "TenthBlock"
        self.size = (40, 35)
        self.pos = (1020, 100)




#failure:
class EleventhBlock(BlockBase):
    def __init__(self, **kwargs):
        super(EleventhBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (65, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "failure:", size_hint = (None, 1), size = (50, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "EleventhBlock"
        self.size = (65, 35)
        self.pos = (1020, 55)




#success:
class TwelfthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(TwelfthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (77, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "success:", size_hint = (None, 1), size = (60, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (7, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "TwelfthBlock"
        self.size = (77, 35)
        self.pos = (1020, 10)




#if ... ... ... :
class ThirteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(ThirteenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (190, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "if", size_hint = (None, 1), size = (15, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (150, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = ":", size_hint = (None, 1), size = (10, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "ThirteenthBlock"
        self.size = (190, 35)
        self.pos = (1135, 100)




#elif ... ... ... :
class FourteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(FourteenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (205, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "elif", size_hint = (None, 1), size = (30, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (150, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = ":", size_hint = (None, 1), size = (10, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "FourteenthBlock"
        self.size = (205, 35)
        self.pos = (1135, 55)




#else:
class FifteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(FifteenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (55, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "else:", size_hint = (None, 1), size = (37, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "FifteenthBlock"
        self.size = (55, 35)
        self.pos = (1135, 10)




#every ... ... ... :
class SixteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(SixteenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (217, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "every", size_hint = (None, 1), size = (42, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (150, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = ":", size_hint = (None, 1), size = (10, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "SixteenthBlock"
        self.size = (217, 35)
        self.pos = (1380, 100)




#while ... ... ... :
class SeventeenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(SeventeenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (217, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "while", size_hint = (None, 1), size = (42, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (150, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Label(text = ":", size_hint = (None, 1), size = (10, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (5, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "SeventeenthBlock"
        self.size = (217, 35)
        self.pos = (1380, 55)




#other condition ...
class EighteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(EighteenthBlock, self).__init__(**kwargs)
        block_colour_box = BoxLayout(orientation = "vertical", size_hint = (None, None), size = (140, 35))
        self.upper_block_colour = Widget()
        self.lower_block_colour = Widget()
        block_colour_box.add_widget(self.upper_block_colour)
        block_colour_box.add_widget(self.lower_block_colour)
        #upper background colour
        with self.upper_block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Triangle(points = (140,35, 140,0, 0,35))
        #lower background colour
        with self.lower_block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Triangle(points = (0,0, 0,35, 140,0))
        #background colour halves added
        self.add_widget(block_colour_box)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "other condition ...", size_hint = (None, 1), size = (120, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "EighteenthBlock"
        self.size = (140, 35)
        self.pos = (1380, 10)




#break loop
class NineteenthBlock(BlockBase):
    def __init__(self, **kwargs):
        super(NineteenthBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (90, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "break loop", size_hint = (None, 1), size = (70, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "NineteenthBlock"
        self.size = (90, 35)
        self.pos = (1637, 100)

        


#skip loop
class TwentiethBlock(BlockBase):
    def __init__(self, **kwargs):
        super(TwentiethBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (80, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "skip loop", size_hint = (None, 1), size = (60, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "TwentiethBlock"
        self.size = (80, 35)
        self.pos = (1637, 55)




#do nothing
class TwentyfirstBlock(BlockBase):
    def __init__(self, **kwargs):
        super(TwentyfirstBlock, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (90, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "do nothing", size_hint = (None, 1), size = (70, 69)))
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "TwentyfirstBlock"
        self.size = (90, 35)
        self.pos = (1637, 10)




#PRD0_I_Forward
class PRD0IForward(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0IForward, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (185, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_I_Forward =", size_hint = (None, 1), size = (125, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0IForward"
        self.size = (185, 35)
        self.pos = (10, 100)




#PRD_I_Rotate
class PRD0IRotate(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0IRotate, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (175, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_I_Rotate =", size_hint = (None, 1), size = (115, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0IRotate"
        self.size = (175, 35)
        self.pos = (10, 55)




#PRD0_O_Ultrasonic
class PRD0OUltrasonic(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0OUltrasonic, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (205, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_O_Ultrasonic =", size_hint = (None, 1), size = (145, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0OUltrasonic"
        self.size = (205, 35)
        self.pos = (10, 10)




#BlackBackground, cleaner than doing bind(on_x) from within the class
class BlackBackground(Widget):
    def __init__(self, **kwargs):
        super(BlackBackground, self).__init__(**kwargs)
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0)
            Rectangle(pos = self.pos, size = self.size) 
    def on_pos(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0)
            Rectangle(pos = self.pos, size = self.size)
#FileSearcherLayout
class FileSearcherLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super(FileSearcherLayout, self).__init__(**kwargs)
        self.add_widget(Button()) #to soak up touch events in the background
        self.add_widget(BlackBackground())
        self.file_searcher = FileChooserListView(filters = ["*.jpg", "*.png"], multiselect = True)
        self.close_button = Button(size_hint = (None, None), size = (25, 25), text = "X")
        boring_anchor = AnchorLayout(anchor_x = "right", anchor_y = "top")
        boring_anchor.add_widget(self.close_button)
        self.file_searcher.add_widget(boring_anchor)
        self.enter_button = Button(size_hint = (None, None), size = (100, 50), text = "Enter (temp)")
        boring_anchor = AnchorLayout(anchor_x = "right", anchor_y = "bottom")
        boring_anchor.add_widget(self.enter_button)
        self.file_searcher.add_widget(boring_anchor)
        self.add_widget(self.file_searcher)
#PRD0_I_RecImg
class PRD0IRecImg(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0IRecImg, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (207, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_I_RecImg = ", size_hint = (None, 1), size = (125, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        boring_button = Button(background_normal = pardies_configuration.path + "\\Icons\\Folder_Icon.png", size_hint = (None, 1), size = (12, 69)) #LOW-RES, NEEDS FIXING
        boring_button.bind(on_press = self.fileSearch)
        self.contents.add_widget(boring_button)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0IRecImg"
        self.size = (207, 35)
        self.pos = (240, 100)
        self.recimg = []
    def fileSearch(self, *args):
        self.fsl = FileSearcherLayout()
        self.fsl.close_button.bind(on_press = self.closeFSL)
        self.fsl.enter_button.bind(on_press = self.enterFiles)
        self.parent.parent.parent.add_widget(self.fsl)
    def enterFiles(self, *args):
        self.recimg = self.fsl.file_searcher.selection
        self.closeFSL()
    def closeFSL(self, *args):
        self.parent.parent.parent.remove_widget(self.fsl)




#PRD0_I_RecImgParas
class PRD0IRecImgParas(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0IRecImgParas, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (285, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_I_RecImgParas = dict: ", size_hint = (None, 1), size = (190, 69))) #recimg, list: match_type, accuracy, resize_increments, rotate_increments;
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (75, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0IRecImgParas"
        self.size = (285, 35)
        self.pos = (240, 55)




#PRD0_O_RecImg
class PRD0ORecImg(BlockBase):
    def __init__(self, **kwargs):
        super(PRD0ORecImg, self).__init__(**kwargs)
        #background colour
        self.block_colour = Widget()
        with self.block_colour.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (197, 35))
        self.add_widget(self.block_colour)
        #button
        self.add_widget(self.block_button)
        #contents and contents anchor
        self.contents.add_widget(Label(text = "PRD0_O_RecImg =", size_hint = (None, 1), size = (127, 69)))
        self.block_first_text = TextInput(font_size = 11.5, size_hint = (None, 1), size = (40, 69))
        self.contents.add_widget(self.block_first_text)
        self.contents.add_widget(Widget(size_hint = (None, 1), size = (10, 69)))
        self.add_widget(self.contents_anchor)
        #properties
        self.block_type = "PRD0ORecImg"
        self.size = (187, 35)
        self.pos = (240, 10)        




#GLOBAL PVPL COLLECTION
global pvpl_collection
pvpl_collection = {"FirstBlock" : FirstBlock,
                   "SecondBlock" : SecondBlock,
                   "ThirdBlock" : ThirdBlock,
                   "FourthBlock" : FourthBlock,
                   "FifthBlock" : FifthBlock,
                   "SixthBlock" : SixthBlock,
                   "SeventhBlock" : SeventhBlock,
                   "EighthBlock" : EighthBlock,
                   "NinthBlock" : NinthBlock,
                   "TenthBlock" : TenthBlock,
                   "EleventhBlock" : EleventhBlock,
                   "TwelfthBlock" : TwelfthBlock,
                   "ThirteenthBlock" : ThirteenthBlock,
                   "FourteenthBlock" : FourteenthBlock,
                   "FifteenthBlock" : FifteenthBlock,
                   "SixteenthBlock" : SixteenthBlock,
                   "SeventeenthBlock" : SeventeenthBlock,
                   "EighteenthBlock" : EighteenthBlock,
                   "NineteenthBlock" : NineteenthBlock,
                   "TwentiethBlock" : TwentiethBlock,
                   "TwentyfirstBlock" : TwentyfirstBlock,
                   "PRD0IForward" : PRD0IForward,
                   "PRD0IRotate" : PRD0IRotate,
                   "PRD0OUltrasonic" : PRD0OUltrasonic,
                   "PRD0IRecImg" : PRD0IRecImg,
                   "PRD0IRecImgParas" : PRD0IRecImgParas,
                   "PRD0ORecImg" : PRD0ORecImg}
