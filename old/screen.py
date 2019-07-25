import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2

        button1 = Button(text='Reboot', font_size=25)
        button2 = Button(text='Status', font_size=25)
        button3 = Button(text='Shutdown', font_size=25)
        button4 = Button(text='Restart\nHomeAssistant', font_size=25)
        button5 = Button(text='Test1', font_size=25)
        button6 = Button(text='Test2', font_size=25)
        
        
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)       
   
        self.add_widget(button1)
        button1.bind(on_press=callback)
        self.add_widget(button2)
        button2.bind(on_press=callback)
        self.add_widget(button3)
        button3.bind(on_press=callback)
        self.add_widget(button4)
        button4.bind(on_press=callback)
        self.add_widget(button5)
        button5.bind(on_press=callback)
        self.add_widget(button6)
        button6.bind(on_press=callback)



class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()