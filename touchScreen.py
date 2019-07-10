import os
import subprocess
os.environ['KIVY_GL_BACKEND'] = 'gl'

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Builder.load_string("""
<Screen1>:
    GridLayout:
        cols: 3
        spacing: [20,20]
        padding: [20,20]
        Button:
            id: b11
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb11()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./homeassistant_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b12
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb12()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./internet_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b13
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            opacity: 1 if self.state == 'normal' else .5
            on_press: root.actionb13()
            Image:
                source: "./speaker_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

        Button:
            id: b14
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb14()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./restart_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b15
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb15()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./power_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b16
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb16() 
            #on_press: root.manager.current = 'Screen2'
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./router_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<Screen2>:
    GridLayout:
        cols: 3
        spacing: [20,20]
        padding: [20,20]
        Button:
            id: b21
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb21()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./backup_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b22
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb22()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./homeassistant_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b23
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            text: 'Screen 2, 3rd Action'
            on_press: root.actionb23()
        Button:
            id: b24
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            text: 'Screen 2, 4th Action'
            on_press: root.actionb24()
        Button:
            id: b25
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            text: 'Screen 2, 5th Action'
            on_press: root.actionb25()
        Button:
            id: b26
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
            Image:
                source: "./left_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<RestartHAPopup>:
    title: ""                 
    separator_height: 0    
    size_hint: None, None
    size: 600, 300            
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Restart HomeAssistant?"
            font_size: '35sp'
        BoxLayout: 
            size_hint_y: 0.3   
            Button:
                text: "Yes"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.actionrestartHA_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.dismiss()

<ShutdownPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "System SHUTDONW?"
            font_size: '35sp'
        BoxLayout: 
            Button:
                text: "Yes"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.actionshutdown_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: root.dismiss()

<RebootPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "System REBOOT?"
            font_size: '35sp'
        BoxLayout: 
            size_hint_y: 0.3   
            Button:
                id: reboot_yes
                text: "Yes"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.actionreboot_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: root.dismiss()

<BeeperOffPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Beeper OFF?"
            font_size: '35sp'
        BoxLayout: 
            size_hint_y: 0.3   
            Button:
                id: reboot_yes
                text: "Yes"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.actionbeeperoff_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: root.dismiss()

<RestartFritzBoxPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Restart Fritzbox?"
            font_size: '35sp'
        BoxLayout: 
            size_hint_y: 0.3   
            Button:
                id: reboot_yes
                text: "Yes"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: 
                    root.actionrestartfritzbox_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: root.dismiss()

""")

class RestartFritzBoxPopup(Popup):
    def actionrestartfritzbox_yes(self):
        print("restart fritzbox!!!")
        os.system('/home/pi/touchScreen/scripts/fritzbox_restart.sh')
    pass

class BeeperOffPopup(Popup):
    def actionbeeperoff_yes(self):
        print("beeper off!!!")
        os.system('/home/pi/touchScreen/scripts/beep_off.sh')
    pass

class RebootPopup(Popup):
    def actionreboot_yes(self):
        print("reboot!!!")
        os.system('/home/pi/touchScreen/scripts/reboot.sh')
    pass

class ShutdownPopup(Popup):
    def actionshutdown_yes(self):
        print("shutdown!!!")
        os.system('/home/pi/touchScreen/scripts/poweroff.sh')
    pass

class RestartHAPopup(Popup):
    def actionrestartHA_yes(self):
        print("restart HA!!!")
        os.system('/home/pi/touchScreen/scripts/homeassistant_restart.sh')
    pass

# Declare both screens
class Screen1(Screen):
    def actionb11(self):
        print("action b11 - restart HA")
        p = RestartHAPopup()
        p.open()
    def actionb12(self):
        print("action b12")
    def actionb13(self):
        print("action b13 - beeper off")
        p = BeeperOffPopup()
        p.open()
    def actionb14(self):
        print("action b14 - reboot")
        p = RebootPopup()
        p.open()
    def actionb15(self):
        print("action b14 - shutdown")
        p = ShutdownPopup()
        p.open()
    def actionb16(self):
        print("action b16 - restart fritzbox")
        p = RestartFritzBoxPopup()
        p.open()
    pass

class Screen2(Screen):
    def actionb21(self):
        print("action b21")
    def actionb22(self):
        print("action b22")
    def actionb23(self):
        print("action b23")
    def actionb24(self):
        print("action b24")
    def actionb25(self):
        print("action b25")
    pass

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())

sm.add_widget(Screen1(name='Screen1'))
sm.add_widget(Screen2(name='Screen2'))

class ScreenApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    print("Start...")
    ScreenApp().run()
    
