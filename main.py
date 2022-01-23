# c'est la structure de base pour n'importe quelle projet kivy
# widget : c'est des controles (ex: bouton)

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget




from navigation_screen_manager import NavigationScreenManager
from canvas_Exemple import *

class MyScreenManager(NavigationScreenManager):
    pass

class LeLabAPP(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        #return CanvasExemple2()
        #return CanvasExemple7()



LeLabAPP().run()