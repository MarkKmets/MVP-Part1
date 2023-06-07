# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test

age=7
name=''
pulse1,pulse2,pulse3=0,0,0

class FirstScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction,font_size ='12sp',color =(1.0, 0.75, 0.0, 1))
        text1 = Label(text="Введіть ім'я:", halign="right",color =(1.0, 0.75, 0.0, 1))
        self.input_name = TextInput(multiline=False)
        text2 = Label(text="Введіть вік:", halign="right",color =(1.0, 0.75, 0.0, 1))
        self.input_age = TextInput(text="7", multiline=False)
        self.btn = Button(text="Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5},color =(1.0, 0.75, 0.0, 1))
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(text1)
        line1.add_widget(self.input_name)
        line2.add_widget(text2)
        line2.add_widget(self.input_age)
        main_line = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)
    
    def next(self):
        global name
        name = self.input_name.text
        self.manager.current = "screen2"

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test1,color =(1.0, 0.75, 0.0, 1))

        line = BoxLayout(size_hint=(0.8, None), height="30sp")
        text_result = Label(text="Введіть результат:", halign="right",color =(1.0, 0.75, 0.0, 1))
        self.input_result = TextInput(text="0", multiline=False)

        line.add_widget(text_result)
        line.add_widget(self.input_result)
        self.btn = Button(text="Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5},color =(1.0, 0.75, 0.0, 1))
        self.btn.on_press = self.next
        main_line = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)

    def next(self):
        global pulse1
        pulse1 = int(self.input_result.text)
        self.manager.current = "screen3"

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits,color =(1.0, 0.75, 0.0, 1))
        self.btn = Button(text="Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5},color =(1.0, 0.75, 0.0, 1))
        self.btn.on_press = self.next
        main_line = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.current = "screen4"

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3,color =(1.0, 0.75, 0.0, 1))
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        text_result1 = Label(text="Результат:", halign="right",color =(1.0, 0.75, 0.0, 1))
        self.input_result1 = TextInput(text="0", multiline=False)
        line1.add_widget(text_result1)
        line1.add_widget(self.input_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        text_result2 = Label(text="Результат після відпочинку:", halign="right",color =(1.0, 0.75, 0.0, 1))
        self.input_result2 = TextInput(text="0", multiline=False)
        line2.add_widget(text_result2)
        line2.add_widget(self.input_result2)
        self.btn = Button(text="Завершити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5},color =(1.0, 0.75, 0.0, 1))
        self.btn.on_press = self.next
        main_line = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)

    def next(self):
        global pulse2, pulse3
        pulse2 = int(self.input_result1.text)
        pulse3 = int(self.input_result2.text)
        self.manager.current = "result"


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_line = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = Label(text="",color =(1.0, 0.75, 0.0, 1))
        self.main_line.add_widget(self.instr)
        self.add_widget(self.main_line)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(pulse1, pulse2, pulse3, age)





class MVP(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name="screen1"))
        sm.add_widget(SecondScr(name="screen2"))
        sm.add_widget(ThirdScr(name="screen3"))
        sm.add_widget(FourthScr(name="screen4"))
        sm.add_widget(ResultScr(name="result"))
        return sm


app = MVP()
app.run()