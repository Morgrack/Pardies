#KIVY LIBARY
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition




#LOGIN
class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        boring_button = Button(text = "<login screen>")
        boring_button.bind(on_press = self.toRun)
        self.add_widget(boring_button)
    def toRun (self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "runSM" 




#PROFILE
class Profile(Screen):
    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)
        boring_button = Button(text = "<profile screen>")
        boring_button.bind(on_press = self.toRun)
        self.add_widget(boring_button)
    def toRun (self, *args):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "runSM"




#SETTINGS
class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        boring_button = Button(text = "<settings screen>")
        boring_button.bind(on_press = self.toRun)
        self.add_widget(boring_button)
    def toRun (self, *args):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "runSM"
