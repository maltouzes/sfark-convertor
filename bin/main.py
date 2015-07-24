#!/usr/bin/env python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup

import ntpath
import inspect

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
		
		sfarkxtcPath = os.getcwd()
		sfarkxtc = sfarkxtcPath + "/sfarkxtc"
		print (sfarkxtc)
		commandcp = "cp " + (sfarkxtc) + " " + (sfarkPath)
		print (commandcp)
		os.system(commandcp)
		
		#
		#a = ("{}".format(self.sfarksf2.text))
		
		### convert file.sfArk to file.sf2
		lenSfarkFileName = len(sfarkFileName)
		lenSfarkFileNameOk = lenSfarkFileName - 5
		sf2FileName =  (sfarkFileName[:lenSfarkFileNameOk]) + "sf2"
			
		exe = "cd " + (sfarkPath) + " && ./sfarkxtc " + (sfarkFileName) + " " + (sf2FileName) + " && rm " + (sfarkPath) + "/sfarkxtc"
		print (exe)
		print (sf2FileName)
		os.system(exe)
		
		
		
###### Check if path exist
		#os.path.exists(path)

    	## Return True if path refers to an existing path. Returns False for broken symbolic links. On some platforms, this function may return False if permission is not granted to execute os.stat() on the requested file, even if the path physically exists.
		


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

		sfarkName = (filename)			
		
		sfarkName = sfarkName[0]
		
		print sfarkName
		
		lenSfarkName = len(sfarkName)
		lenSfarkPath = len(sfarkPath)
		lenSfarkPath += 1 
		
		lenok = (lenSfarkPath) - (lenSfarkName)
					
		sfarkFileName = (sfarkName[lenok:])
		print (sfarkFileName)
		global sfarkPath
		global sfarkFileName
		
		self.dismiss_popup()
		return (sfarkFileName)

#########	App #################	
class sfarkconvertorApp(App):
	title = "sfArk Convertor"
	pass
	
if __name__ == '__main__':
	sfarkconvertorApp().run()
