#KIVY LIBARY
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition

#OTHER LIBARIES
import os

#PARDIES IMPORTS
import pardies_configuration




#BASE
class ColourThemeBar(Widget):
   def __init__(self, **kwargs):
        super(ColourThemeBar, self).__init__(**kwargs)
        with self.canvas:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = (1920, 60))

class ProfileIcon(Button):
   def __init__(self, **kwargs):
        super(ProfileIcon, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.text = "<username>"
        self.color = (0, 0, 0)
        
class SettingsIcon(Button):
   def __init__(self, **kwargs):
        super(SettingsIcon, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.background_normal = pardies_configuration.path + "\\Icons\\Settings_Icon.png"

class LogoutIcon(Button):
    def __init__(self, **kwargs):
        super(LogoutIcon, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (60, 60)
        self.background_normal = pardies_configuration.path + "\\Icons\\Logout_Icon.png"

class MainButton(Button):
    def __init__(self, **kwargs):
        super(MainButton, self).__init__(**kwargs)
        self.background_color = (0.5, 0.5, 0.5)

class MainButtonSelected(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd)
            Rectangle(pos = self.pos, size = self.size)
    def on_pos(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd)
            Rectangle(pos = self.pos, size = self.size)

class MainButtonsBackground(Widget):
    def __init__(self, **kwargs):
        super(MainButtonsBackground, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.size = (69, 60)
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




#RUN, EDIT, SHOP BASE
class RunEditShopBase(Screen):
    def __init__(self, **kwargs):
        super(RunEditShopBase, self).__init__(**kwargs)
        #colour theme
        self.colour_theme_rel = RelativeLayout()
        self.colour_theme_rel.size_hint = (None, None)
        self.colour_theme_rel.size = (1920, 60)
        self.colour_theme_rel.pos_hint = {"top" : 1}
        self.colour_theme_rel.add_widget(ColourThemeBar())
        #profile, settings, logout
        self.psl_box = BoxLayout(orientation = "horizontal")
        self.psl_box.size_hint = (1, None)
        self.psl_box.size = (69, 60)
        self.psl_box.pos_hint = {"top": 1}
            #profile
        profile_button = ProfileIcon()
        profile_button.bind(on_press = self.toProfile)
        self.psl_box.add_widget(profile_button)
            #buffer
        for i in range(7):
            self.psl_box.add_widget(Widget())
            #settings
        settings_button = SettingsIcon()
        settings_button.bind(on_press = self.toSettings)
        settings_anchor = AnchorLayout(anchor_x = "center", anchor_y = "center")
        settings_anchor.add_widget(settings_button)
            #logout
        logout_button = LogoutIcon()
        logout_button.bind(on_press = self.toLogin)
        logout_anchor = AnchorLayout(anchor_x = "center", anchor_y = "center")
        logout_anchor.add_widget(logout_button)
            #settings and logout added in correct position (THIS WILL NEED ADJUSTING FOR PHONE VERSION)
        boring_box = BoxLayout(orientation = "horizontal", size_hint = (None, 1), size = (150, 1))
        boring_box.add_widget(settings_anchor)
        boring_box.add_widget(logout_anchor)
        self.psl_box.add_widget(boring_box)
        #main buttons background
        self.main_buttons_background = BoxLayout(orientation = "vertical")
        self.main_buttons_background.add_widget(Widget(size_hint = (1, None), size = (69, 60)))
        self.main_buttons_background.add_widget(MainButtonsBackground())
        self.main_buttons_background.add_widget(Widget())
        #main buttons
        self.main_buttons_layout = BoxLayout(orientation = "horizontal")
        self.main_buttons_layout.size_hint = (1, None)
        self.main_buttons_layout.size = (69, 60)
        self.run_button = MainButton(text = "Run")
        self.run_button.bind(on_press = self.toRun)
        self.run_button_selected = MainButtonSelected(text = "Run")
        self.edit_button = MainButton(text = "Edit")
        self.edit_button.bind(on_press = self.toEdit)
        self.edit_button_selected = MainButtonSelected(text = "Edit")
        self.shop_button = MainButton(text = "Shop")
        self.shop_button.bind(on_press = self.toShop)
        self.shop_button_selected = MainButtonSelected(text = "Shop")
    #button bound screen transitions
    def toProfile(self, *args):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "profileSM"
    def toSettings(self, *args):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "settingsSM"
    def toLogin(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "loginSM"
    def toRun(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "runSM"
    def toEdit(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "editSM"
    def toShop(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "shopSM"




#SELF-ADJUSTING WHITE BOX
class AdjWhiteBox(Widget):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1)
            Rectangle(pos = self.pos, size = self.size)




#EDIT COLOUR THEME
class EditColourTheme(Widget):
    def __init__(self, **kwargs):
        super(EditColourTheme, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.size = (69, 145)
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd)
            Rectangle(pos = self.pos, size = self.size)




#POPUP COLOUR THEME
class PopupLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = self.size)
    def on_pos(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(pardies_configuration.r, pardies_configuration.g, pardies_configuration.b)
            Rectangle(pos = self.pos, size = self.size)




#ROBOT ICON (wip)
class PRD(RelativeLayout):
    def __init__(self, **kwargs):
        super(PRD, self).__init__(**kwargs)
        self.size_hint = (None, 1)
        self.size = (110, 69)
        #temp will add circle icons denoting status and connection type soon
        boring_box = BoxLayout(pos_hint = {"top": 0.64}, orientation = "vertical", size_hint = (None, None), size = (110, 110))
        self.prd_name = Label() #in format: "PRD-X, <model no.>"
        self.prd_name.font_size = 13
        boring_box.add_widget(self.prd_name)
        self.robot_icon = Button(pos_hint = {"top": 0.64}, size_hint = (None, None), size = (110, 110), background_normal = pardies_configuration.path + "\\Icons\\Robot_Temp.png") #will become dynamic based on PRD type
        boring_box.add_widget(self.robot_icon)
        self.add_widget(boring_box)


        
        
#PVPL SCIPT ICON (wip)
class PVPL(RelativeLayout):
    def __init__(self, **kwargs):
        super(PVPL, self).__init__(**kwargs)
        self.size_hint = (None, 1)
        self.size = (110, 69)
        boring_box = BoxLayout(pos_hint = {"top": 0.64}, orientation = "vertical", size_hint = (None, None), size = (110, 110))
        self.pvpl_name = Label()
        self.pvpl_name.font_size = 13
        boring_box.add_widget(self.pvpl_name)
        self.script_icon = Button(pos_hint = {"top": 0.64}, size_hint = (None, None), size = (110, 110), background_normal = pardies_configuration.path + "\\Icons\\PVPL_Temp.png") #will become dynamic based on PRD type
        boring_box.add_widget(self.script_icon)
        self.add_widget(boring_box)
