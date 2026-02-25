from kivymd.app import MDApp
from kivy.lang import Builder
import math


kv = """
MDScreen:
	MDTopAppBar:
    	title: "My Calculator"
    	left_action_items: [["calculator", lambda x: None]]
	MDBoxLayout:
		orientation:"vertical"
		padding:10
		MDRaisedButton:
			text: "Calculator"
			pos_hint:{"center_x":0.5,"center_y":0.8}
            on_release: app.switch_screen("calculator")

        MDRaisedButton:
        	text: "Converter"
			pos_hint:{"center_x":0.5,"center_y":0.7}
        	on_release: app.switch_screen("converter")
		ScreenManager:
			id : sm
			MDScreen:
				name:"calculator"
				MDFloatLayout:
					MDLabel:
						text:"Dark Mode"
						theme_text_color:"Custom"
						text_color:0,0,0.8,1
						pos_hint: {"center_x":0.9,"center_y":0.3}
					MDSwitch:
						active:False
						on_active:app.switch_mode(*args)
						pos_hint: {"center_x":0.7,"center_y":0.3}
				MDBoxLayout:
					orientation:"vertical"
					padding:150
					spacing:20
					
					MDTextField:
						id:calc_input
						font_size:"30dp"
						mode:"rectangle"
						readonly:True
						line_color_normal:0, 0.2, 1, 1
	
						
					MDGridLayout:
						cols:5
						spacing:10
						padding:10
						MDRectangleFlatButton:
							text:"7"
							font_size:"30sp"
							on_release:app.add_text("7")
						MDRectangleFlatButton:
							text:"8"
							font_size:"30sp"
							on_release:app.add_text("8")
						MDRectangleFlatButton:
							text:"9"
							font_size:"30sp"
							on_release:app.add_text("9")
						MDRectangleFlatButton:
							text:"/"
							font_size:"30sp"
							on_release:app.add_text("/")
						MDRectangleFlatButton:
							text:"*"
							font_size:"30sp"
							on_release:app.add_text("*")
						MDRectangleFlatButton:
							text:"6"
							font_size:"30sp"
							on_release:app.add_text("6")
						MDRectangleFlatButton:
							text:"5"
							font_size:"30sp"
							on_release:app.add_text("5")
						MDRectangleFlatButton:
							text:"4"
							font_size:"30sp"
							on_release:app.add_text("4")
						MDRectangleFlatButton:
							text:"-"
							font_size:"30sp"
							on_release:app.add_text("-")
						MDRectangleFlatButton:
							text:"+"
							font_size:"30sp"
							on_release:app.add_text("+")
						MDRectangleFlatButton:
							text:"1"
							font_size:"30sp"
							on_release:app.add_text("1")
						MDRectangleFlatButton:
							text:"2"
							font_size:"30sp"
							on_release:app.add_text("2")
						MDRectangleFlatButton:
							text:"3"
							font_size:"30sp"
							on_release:app.add_text("3")
						MDRectangleFlatButton:
							text:"."
							font_size:"30sp"
							on_release:app.add_text(".")
						MDRectangleFlatButton:
							text:"^"
							font_size:"30sp"
							on_release:app.add_text("**")
						MDRectangleFlatButton:
							text:"C"
							font_size:"30sp"
							on_release:app.clear()
						MDRectangleFlatButton:
							text:"0"
							font_size:"30sp"
							on_release:app.add_text("0")
						MDRectangleFlatButton:
							text:"e"
							font_size:"30sp"
							on_release:app.add_text("math.e")
						MDRectangleFlatButton:
							text:"("
							font_size:"30sp"
							on_release:app.add_text("(")
						MDRectangleFlatButton:
							text:")"
							font_size:"30sp"
							on_release:app.add_text(")")
						MDRectangleFlatButton:
							text:"x!"
							font_size:"30sp"
							on_release:app.add_text("math.factorial(")
						MDRectangleFlatButton:
							text: "%"
							font_size:"30sp"
							on_release: app.add_text("%")
						MDRectangleFlatButton:
							text: "π"
							font_size:"30sp"
							on_release: app.add_text("math.pi")
						MDRectangleFlatButton:
							text:"√"
							font_size:"30sp"
							on_release:app.add_text("math.sqrt(")
						MDRectangleFlatButton:
							text:"="
							font_size:"30sp"
							theme_text_color:"Custom"
							text_color:1,1,1,1
							md_bg_color:app.theme_cls.primary_color
							on_release:app.calculate()
					
			MDScreen:
				name:"converter"
				MDBoxLayout:
					orientation:"vertical"
					padding:20
					MDGridLayout:
						cols:3
						padding:50
						spacing:200
						MDIconButton:
							icon:"ruler"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
							on_release:app.lenght()
						MDIconButton:
							icon:"weight-kilogram"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
							on_release:app.weight()
						MDIconButton:
							icon:"square-outline"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"calendar"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"sale"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"cube-outline"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"numeric"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"speedometer"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"thermometer"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"human"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"file-document-outline"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
						MDIconButton:
							icon:"finance"
							theme_text_color:"Custom"
							icon_color:0,0,1,1
							icon_size:"50sp"
					
			MDScreen:
				name:"length"
				MDFloatLayout:
					MDLabel:
						text:"Lenght Measurement"
						font_style:"H4"
						theme_text_color:"Custom"
						text_color:0,0.2,0.8,1
						pos_hint:{"center_x":0.7,"center_y":0.970}
						
					MDTextField:
						id:input_value
						input_filter:"float"
						hint_text:"Enter value"
						mode:"rectangle"
						theme_text_color:"Custom"
						text_color:1,0,0.7,1
						line_color_focus:1,0,0,1
						size_hint_x:0.9
						line_color_normal:0,0,0.6,1
						pos_hint: {"center_x":0.5,"center_y":0.8}
					MDDropDownItem:
						id:unit
						text:"Meter"
						pos_hint:{"center_x":0.15,"center_y":0.750}
					
						on_release:app.change_unit()
					MDRaisedButton:
						text:"Convert"
						pos_hint:{"center_x":0.5,"center_y":0.65}
						on_release:app.convert_lenght()
					MDLabel:
						id:result
						font_style:"H5"
						theme_text_color:"Custom"
						text_color:0,0.8,0,1
						pos_hint:{"center_x":0.8,"center_y":0.4}																					    	
			MDScreen:
				name:"mass"
				MDFloatLayout:
					MDLabel:
						text:"Mass Measurement"
						font_style:"H4"
						theme_text_color:"Custom"
						text_color:0,0.2,0.8,1
						pos_hint:{"center_x":0.7,"center_y":0.970}
					MDTextField:
						id:input
						hint_text:"Enter Value"
						input_filter:"float"
						hint_text:"Enter value"
						mode:"rectangle"
						theme_text_color:"Custom"
						text_color:1,0,0.7,1
						line_color_focus:1,0,0,1
						size_hint_x:0.9
						line_color_normal:0,0,0.6,1
						pos_hint: {"center_x":0.5,"center_y":0.8}
					MDDropDownItem:
						id:weight_unit
						text:"Gram"
						pos_hint:{"center_x":0.15,"center_y":0.750}
						on_release:app.mass_unit()
					MDRaisedButton:
						text:"Convert"
						pos_hint:{"center_x":0.5,"center_y":0.65}
						on_release:app.convert_mass()
					MDLabel:
						id:result_1
						font_style:"H5"
						theme_text_color:"Custom"
						text_color:0,0.8,0,1
						pos_hint:{"center_x":0.8,"center_y":0.4}
							
							
							
							





"""


class Calculator(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Blue"
		return Builder.load_string(kv)



	def add_text(self, value):
		self.root.ids.calc_input.text += value
	def clear(self):
		self.root.ids.calc_input.text = ""
		
	def calculate(self):
		try:
			experssion = self.root.ids.calc_input.text
			result = eval(experssion, {"__builtins__": None}, {"math": math})
			self.root.ids.calc_input.text = str(result)
		except:
			self.root.ids.calc_input.text = "Error"
	def switch_mode(self,instance,value):
		if value:
			self.theme_cls.theme_style = "Dark"
		else:
			self.theme_cls.theme_style = "Light"	

	def lenght(self):
		self.root.ids.sm.current = "length"
		
	def change_unit(self):
		if self.root.ids.unit.text=="Meter":
			self.root.ids.unit.text="Kilometer"
		else:
			self.root.ids.unit.text="Meter"
		
	
	
	
			 


	def convert_lenght(self):
		try:
			value = float(self.root.ids.input_value.text)
			unit = self.root.ids.unit.text
			
			if unit == "Meter":
				result  = value/1000
				self.root.ids.result.text = f"{result} Kilometer"
			else:
				result  = value*1000
				self.root.ids.result.text = f"{result} Meter"
		except:
			self.root.ids.result.text = "Invalid Input" 
		
	def weight(self):
		self.root.ids.sm.current = "mass"
	def mass_unit(self):
		if self.root.ids.weight_unit.text == "Gram":
			self.root.ids.weight_unit.text = "Kilogram"
		else:
			self.root.ids.weight_unit.text = "Gram"
	def convert_mass(self):
		try:
			value = float(self.root.ids.input.text)
			unit = self.root.ids.weight_unit.text
			if unit == "Gram":
				result = value/1000
				self.root.ids.result_1.text = f"{result} Kilogram"
			else:
				result = value * 1000
				self.root.ids.result_1.text = f"{result} Gram"
		except:
			self.root.ids.result_1.text = "Invalid Input "
	def switch_screen(self, screen_name):
	    self.root.ids.sm.current = screen_name
				
		
if __name__ == "__main__":
	Calculator().run()