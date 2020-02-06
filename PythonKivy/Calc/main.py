from kivy.app import App
from kivy.uix.button import *
import math
from kivy.uix.label import *
from kivy.uix.gridlayout import *
from kivy.uix.anchorlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set('graphics','resizable', '1');
Config.set('graphics','width','318');
Config.set('graphics','height','470');

class MyApp(App):
	def update_label(self):
		self.lbl.text = self.formula
	def add_number(self, inctance):
		if(self.formula == "0"):
			self.formula = ""
		if str(inctance.text) == ",":
			self.formula += "." 
		else:
			self.formula += str(inctance.text)
		self.update_label()
	def add_operation(self,inctance):
		if (str(inctance.text).lower() == "x"):
			self.formula += "*"
		else:
			self.formula += str(inctance.text)
		self.update_label()
	def calc_result(self,inctance):
		try:
			self.lbl.text = str(eval(self.lbl.text))
		except Exception:
			self.formula = "Err"
			self.update_label()
		else:
			self.formula = "0"
		self.formula = "0"
	def hard_operation(self,inctance):
		if inctance.text == "%":
			self.formula = str(float(self.formula) * 0.01)
		elif inctance.text == "C" or inctance.text == "CE":
			self.formula = "0"
		elif inctance.text == "<=":
			self.formula = self.formula[:-1]
		elif inctance.text == "1/x":
			try:
				self.formula = str(1 / float(self.formula))
			except Exception:
				self.formula = "Err"
				self.update_label()
		elif inctance.text == "x^2":
			self.formula = str(float(self.formula)**2)
		elif inctance.text == "√x":
			self.formula = str(math.sqrt(float(self.formula)))
		elif inctance.text == "+/-":
			self.formula = str(float(self.formula) * -1)
		self.update_label()
	def build(self):
		self.formula = "0"
		bl = BoxLayout(orientation = "vertical")
		gl = GridLayout(cols= 4, size_hint = (1,.6))

		self.lbl = Label(text= "0", font_size = 40, halign = "right", valign = "center",size_hint = (1,.4),text_size = (318-50,470*.4-50))
		bl.add_widget(self.lbl)
		gl.add_widget(Button(text = "%", on_press = self.hard_operation))
		gl.add_widget(Button(text = "CE", on_press = self.hard_operation))
		gl.add_widget(Button(text = "C", on_press = self.hard_operation))
		gl.add_widget(Button(text = "<=", on_press = self.hard_operation))

		gl.add_widget(Button(text = "1/x", on_press = self.hard_operation))
		gl.add_widget(Button(text = "x^2", on_press = self.hard_operation))
		gl.add_widget(Button(text = "√x", on_press = self.hard_operation))
		gl.add_widget(Button(text = "/",on_press = self.add_operation))

		gl.add_widget(Button(text = "7",on_press = self.add_number))
		gl.add_widget(Button(text = "8",on_press = self.add_number))
		gl.add_widget(Button(text = "9",on_press = self.add_number))
		gl.add_widget(Button(text = "X",on_press = self.add_operation))

		gl.add_widget(Button(text = "4",on_press = self.add_number))
		gl.add_widget(Button(text = "5",on_press = self.add_number))
		gl.add_widget(Button(text = "6",on_press = self.add_number))
		gl.add_widget(Button(text = "-",on_press = self.add_operation))

		gl.add_widget(Button(text = "1",on_press = self.add_number))
		gl.add_widget(Button(text = "2",on_press = self.add_number))
		gl.add_widget(Button(text = "3",on_press = self.add_number))
		gl.add_widget(Button(text = "+",on_press = self.add_operation))

		gl.add_widget(Button(text = "+/-", on_press = self.hard_operation))
		gl.add_widget(Button(text = "0",on_press = self.add_number))
		gl.add_widget(Button(text = ",",on_press = self.add_number))
		gl.add_widget(Button(text = "=",on_press = self.calc_result))
		bl.add_widget(gl)

		return bl
if __name__ == "__main__":
	MyApp().run()