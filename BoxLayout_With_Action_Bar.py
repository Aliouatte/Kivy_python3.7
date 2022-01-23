from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

Builder.load_file("BoxLayout_With_Action_Bar.kv")

class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()