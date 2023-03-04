#Copyright 2021 all Pardies files, Morgan Purkis, all rights reserved.

#KIVY LIBARY
from kivy.app import App

#PARDIES IMPORTS
from pardies_login_profile_settings import *
from pardies_run_edit_shop import *




#SCREENMANAGER
class SM(ScreenManager):
    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)
        self.transition = NoTransition()
        LoginSM = Login(name = "loginSM")
        RunSM = Run(name = "runSM")
        EditSM = Edit(name = "editSM")
        ShopSM = Shop(name = "shopSM")
        ProfileSM = Profile(name = "profileSM")
        SettingsSM = Settings(name = "settingsSM")
        self.add_widget(LoginSM)
        self.add_widget(RunSM)
        self.add_widget(EditSM)
        self.add_widget(ShopSM)
        self.add_widget(ProfileSM)
        self.add_widget(SettingsSM)




#BUILD
class Pardies(App):
    def build(self):
        return SM()




#RUN PARDIES
if __name__ == '__main__':
    Pardies().run()
