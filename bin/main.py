#!/usr/bin/env python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar


import subprocess
#import ntpath
#import inspect

import os

class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class AucunFichierPopup(BoxLayout):
        cancel = ObjectProperty(None)
            
class IncompatiblePopup(BoxLayout):
        cancel = ObjectProperty(None)
            
class SuccessfulPopup(BoxLayout):
                cancel = ObjectProperty(None)
            
class CorruptPopup(BoxLayout):
                cancel = ObjectProperty(None)

class SfarkxtcPopup(BoxLayout):
                cancel = ObjectProperty(None)
class XBoxLayout(BoxLayout):
                cancel = ObjectProperty(None)            
				
class Sfark(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    sfarksf2 = ObjectProperty()
	
	
    global sfarkPath
    sfarkPath = ""
    global sfarkxtc
    sfarkxtc = ""	
    global sfarkFileName 
    sfarkFileName = ""
	
	# call ./sfarkxtc command line, onli from text input for now 
    def convertSfark(self):
        
        sfarkxtcPath = os.getcwd()
        sfarkxtc = sfarkxtcPath + "/sfarkxtc"
        print "#############################"
        print "sfarkxtc = " + (sfarkxtc)
        commandcp = "cp " + (sfarkxtc) + " " + (sfarkPath)
        print "commandcp = " + (commandcp)
        if os.path.isfile(sfarkxtc):
            print "sfarkxtc found"
        
            subprocess.call(commandcp, shell=True)
		
		#
		#a = ("{}".format(self.sfarksf2.text))
		
		### convert file.sfArk to file.sf2
            lenSfarkFileName = len(sfarkFileName)
            lenSfarkFileNameOk = lenSfarkFileName - 5
            sf2FileName =  (sfarkFileName[:lenSfarkFileNameOk]) + "sf2"
			
            exe = "cd " + (sfarkPath) + " && ./sfarkxtc " + (sfarkFileName) + " " + (sf2FileName) + " > sfarkTest.txt" + " && rm " + (sfarkPath) + "/sfarkxtc"
        
            print "sf2FileName = " + (sf2FileName)
            print (exe)
            subprocess.call(exe, shell=True)
		
		
		# call sfarkTest.txt
            sfarkPathtxt = (sfarkPath) + "/sfarkTest.txt"
            print "sfarkPath = " + sfarkPath
            print "sfarkPathtxt = " + sfarkPathtxt
            a = ""
		
		######## Check if sfarkPathtxt exist
            if os.path.isfile(sfarkPathtxt):
                a = open(sfarkPathtxt).read().lower()
            print "a = " + a
            type (a) 
	
		#### test corrupt in sfarkTest
		#test = "corrupt" 
            if "corrupt" in a:
                print "Veuillez choisir un fichier sfArk valide"
			###### need to implement cancel (close)
                def corrupt(self):
                    content = CorruptPopup(cancel=self.dismiss_popup)
                    self._popup = Popup(title="Fichier sfArk non valide", content = content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()
				
                corrupt(self)				
            else:
                pass
		
            if "incompatible" in a:
                print "Version sfArk non prise en charge (version 2 uniquement)"
                def incompatible(self):
                    content = IncompatiblePopup(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content = content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()
	    			
                incompatible(self)
            else: 
                pass	
		
            if "successful" in a:
                print "Conversion reussie"
                def Successful(self):
                    content = SuccessfulPopup(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content = content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()
				
                Successful(self)
            else: 
                pass
		
		####################################
		####################################
		######## use XBoxLayout  or AucunFichierPopup
            if a == "":
                print "Aucun fichier selectionne"
                def aucunFichier(self):
                    
                    content = AucunFichierPopup(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content = content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()
	    			
                aucunFichier(self)
            else: 
                pass
        else:
            print "sfarkxtc introuvable"
            def SfarkxtcSearch(self):
                    
                    content = SfarkxtcPopup(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content = content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()
	    			
            SfarkxtcSearch(self)    
		##################		

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
        print "sfarkPath = " + (sfarkPath)

        sfarkName = (filename)			
		
        sfarkName = sfarkName[0]
		
        print "sfarkName = " + sfarkName
		
        lenSfarkName = len(sfarkName)
        lenSfarkPath = len(sfarkPath)
        lenSfarkPath += 1 
		
        lenok = (lenSfarkPath) - (lenSfarkName)
					
        sfarkFileName = (sfarkName[lenok:])
        print "sfarkFileName = " + (sfarkFileName)
        global sfarkPath
        global sfarkFileName
		
        self.dismiss_popup()
        return (sfarkFileName)

#########	App #################	
class SfarkConvertorApp(App):
    title = "sfArk Convertor"
    pass
	
if __name__ == '__main__':
    SfarkConvertorApp().run()
