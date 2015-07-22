#!/usr/bin/env python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup

import os

class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class sfark(BoxLayout):
	loadfile = ObjectProperty(None)
	savefile = ObjectProperty(None)
	text_input = ObjectProperty(None)

	sfarksf2 = ObjectProperty()
 
	# call ./sfarkxtc command line, onli from text input for now 
	def convertSfark(self):
		a = ("{}".format(self.sfarksf2.text))
		b = "exemple.sf2"
		exe = "cd /home/user/MAO/sfarkxtc-master && ./sfarkxtc " + (a) + " " +(b)
		print (exe)
		os.system(exe)


	def dismiss_popup(self):
		self._popup.dismiss()

		
	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Fichier sfark", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()	
			
# Choose sfark file here
	def load(self, path, filename):
		sfarkPath =  os.path.join(path)
		print (sfarkPath)
		#with open(os.path.join(path, filename[0])) as stream:
		#	self.text_input.text = stream.read()
			
		#self.dismiss_popup()
		
class sfarkconvertorApp(App):
	title = "sfArk Convertor"
	pass
	
if __name__ == '__main__':
	sfarkconvertorApp().run()
