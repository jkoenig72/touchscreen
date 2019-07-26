import os
import subprocess
os.environ['KIVY_GL_BACKEND'] = 'gl'

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
import datetime

Builder.load_string("""
<Screen1>:
    GridLayout:
        cols: 4
        spacing: [10,10]
        padding: [10,10]
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
            on_press: 
            #    root.img_src = './internet_green.png' 
                root.actionb12()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                id: b12pic
                source: root.img_src
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
        Button:
            id: b17
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb17()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./iRobot_start_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            id: b18
            color: [0,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.actionb18()
            opacity: 1 if self.state == 'normal' else .5
            Image:
                source: "./iRobot_stop_white.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<BlankScreen>:
    GridLayout:
        cols: 4
        spacing: [20,20]
        padding: [20,20]
        Button:
            id: b21
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
            opacity: 1 if self.state == 'normal' else .5
        Button:
            id: b22
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
            opacity: 1 if self.state == 'normal' else .5
        Button:
            id: b23
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
        Button:
            id: b24
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
        Button:
            id: b25
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
        Button:
            id: b26
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
        Button:
            id: b27
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'
        Button:
            id: b28
            color: [1,1,1,1]
            background_normal: ''
            background_color: [0, 0, 0, 0]
            on_press: root.manager.current = 'Screen1'

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

<StartiRobotPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Start iRobot?"
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
                    root.actionstartirobot_yes()
                    root.dismiss()
            Button:
                text: "No"
                font_size: '35sp'
                background_normal: ''
                background_color: [0, 0, 0, 0]
                opacity: 1 if self.state == 'normal' else .5
                on_press: root.dismiss()

<DockiRobotPopup>:
    title: ""                 # <<<<<<<<
    separator_height: 0       # <<<<<<<<
    size_hint: None, None
    size: 600, 300
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Dock iRobot?"
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
                    root.actiondockirobot_yes()
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
        os.system('/home/pi/bin/ts/fritzbox_restart.sh')
    pass

class BeeperOffPopup(Popup):
    def actionbeeperoff_yes(self):
        print("beeper off!!!")
        print(lastactiontimestamp)
        os.system('/home/pi/bin/ts/beep_off.sh')
    pass

class RebootPopup(Popup):
    def actionreboot_yes(self):
        print("reboot!!!")
        os.system('/home/pi/bin/ts/reboot.sh')
    pass

class ShutdownPopup(Popup):
    def actionshutdown_yes(self):
        print("shutdown!!!")
        os.system('/home/pi/bin/ts/poweroff.sh')
    pass

class RestartHAPopup(Popup):
    def actionrestartHA_yes(self):
        print("restart HA!!!")
        os.system('/home/pi/bin/ts/homeassistant_restart.sh')
    pass

class StartiRobotPopup(Popup):
    def actionstartirobot_yes(self):
        print("start irobot!!!")
        os.system('/home/pi/bin/ts/startRoomba.sh')
    pass

class DockiRobotPopup(Popup):
    def actiondockirobot_yes(self):
        print("dock irobot!!!")
        os.system('/home/pi/bin/ts/dockRoomba.sh')
    pass

# Declare both screens
class Screen1(Screen):
    global lastactiontimestamp
    img_src = StringProperty('./internet_red.png')
    def actionb11(self):
        print("action b11 - restart HA")
        lastactiontimestamp = datetime.datetime.now() 
        p = RestartHAPopup()
        p.open()
    def actionb12(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b12")
    def actionb13(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b13 - beeper off")
        p = BeeperOffPopup()
        p.open()
    def actionb14(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b14 - reboot")
        p = RebootPopup()
        p.open()
    def actionb15(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b14 - shutdown")
        p = ShutdownPopup()
        p.open()
    def actionb16(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b16 - restart fritzbox")
        p = RestartFritzBoxPopup()
        p.open()
    def actionb17(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b17 - start iRobot")
        p = StartiRobotPopup()
        p.open()
    def actionb18(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b18 - dock iRobot")
        p = DockiRobotPopup()
        p.open()
    pass

class BlankScreen(Screen):
    global lastactiontimestamp
    def actionb21(self):
        print("action b21")
        lastactiontimestamp = datetime.datetime.now() 
    def actionb22(self):
        lastactiontimestamp = datetime.datetime.now() 
        print("action b22")
    def actionb23(self):
        print("action b23")
        lastactiontimestamp = datetime.datetime.now() 
    def actionb24(self):
        print("action b24")
        lastactiontimestamp = datetime.datetime.now() 
    def actionb25(self):
        print("action b25")
        lastactiontimestamp = datetime.datetime.now() 
    pass

# Create the screen manager
lastactiontimestamp = datetime.datetime.now()

sm = ScreenManager()
sm.add_widget(Screen1(name='Screen1'))
sm.add_widget(BlankScreen(name='BlankScreen'))



class ScreenApp(App):
    def build(self):
        return sm
    def timer_checkInternet(dt):
        #print("timer - check Internet")
        result = subprocess.run(['/home/pi/bin/ts/checkInternet.sh', ''], stdout=subprocess.PIPE)
        if int(result.stdout.decode('utf-8')) == 1:
            #print("OK")
            sm.get_screen('Screen1').ids['b12pic'].source = './internet_green.png'
        else:
            print("FAILD")    
            sm.get_screen('Screen1').ids['b12pic'].source = './internet_red.png'
        pass    
    def timer_checkInactivity(dt):
        global lastactiontimestamp
        nowtime = datetime.datetime.now()
        if ((nowtime - datetime.timedelta(seconds=10)) > lastactiontimestamp):
            print("timer - ScreenSaver - On")
            lastactiontimestamp = nowtime
            sm.current = "BlankScreen"
        pass    

if __name__ == '__main__':
    global lastactiontimestamp
    lastactiontimestamp = datetime.datetime.now()
    print("Start...")
    Clock.schedule_interval(ScreenApp.timer_checkInternet, 10)
    Clock.schedule_interval(ScreenApp.timer_checkInactivity, 30)
    ScreenApp().run()
    
