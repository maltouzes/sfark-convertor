#!/usr/bin/env python

"""sfark-convertor is a simple GUI Sfark decompressor to sf2, it convert
soundfonts in the legacy sfArk v2 file format to sf2.
Only Linux is supported."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import subprocess
import os


class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class XBoxLayout(BoxLayout):
    cancel = ObjectProperty(None)


class Sfark(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def sfarkrootpath(self):
        if subprocess.call(["which", "sfarkxtc"]) == 0:
            p = subprocess.check_output(["which", "sfarkxtc"])
            return p.strip()
        else:
            p = "/"
            return p
# Add current dir path for sfarkxtc
# else:
# p = subprocess.check_output(["pwd"])
# p =  p.strip() +"/sfarkxtc"
# print p
# return p

    def aucunFichier(self):
        XBoxLayout.text = "Aucun fichier selectionn" + u'\u00E9'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def Successful(self):
        XBoxLayout.text = "Conversion reussie"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def incompatible(self):
        XBoxLayout.text = 'Version sfArk non prise en charge \
                          (version 2 uniquement'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def corrupt(self):
        XBoxLayout.text = 'Veuillez choisir un fichier sfArk'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Fichier sfArk non valide",
                            content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def SfarkxtcSearch(self):
        XBoxLayout.text = "sfarkxtc introuvable"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def convertSfark(self):
        instance = SfarkConvertorApp()
        sfarkxtc = self.sfarkrootpath()

        print "sfarkPath"
        print instance.sfarkPath
        sfarkPath = instance.sfarkPath
        if os.path.isfile(sfarkxtc):
            print "sfarkxtc found"

# convert file.sfArk to file.sf2
            sfarkPath = "".join(sfarkPath)
            sfarkFilePath = os.path.dirname(sfarkPath)
            print "sfarkFilePath = " + sfarkFilePath
            sfarkPath = sfarkPath.split("/")
            sfarkFileName = sfarkPath[-1]
            print "sfarkFileName = " + sfarkFileName
            sf2FileName = sfarkFileName[:-5] + "sf2"
            print "sf2FileName = " + (sf2FileName)

            exe = "cd " + (sfarkFilePath) + " && sfarkxtc " + \
                  (sfarkFileName) + " " + (sf2FileName) + " > sfarkTest.txt"
            print exe
            subprocess.call(exe, shell=True)

# call sfarkTest.txt
            sfarkPathtxt = (sfarkFilePath) + "/sfarkTest.txt"
            print "sfarkFilePath = " + sfarkFilePath
            print "sfarkPathtxt = " + sfarkPathtxt
            a = ""

# Check if sfarkPathtxt exist
            if os.path.isfile(sfarkPathtxt):
                a = open(sfarkPathtxt).read().lower()
            print "a = " + a
            type(a)

# test corrupt in sfarkTest
            if "corrupt" in a:
                print "Veuillez choisir un fichier sfArk"
                self.corrupt()
            else:
                pass

            if "incompatible" in a:
                print "Version sfArk non prise en charge \
                       (version 2 uniquement)"
                self.incompatible()
            else:
                pass

            if "successful" in a:
                print "Conversion reussie"
                rmsfarkPathtxt = "rm " + (sfarkPathtxt)
                subprocess.call(rmsfarkPathtxt, shell=True)

                self.Successful()
            else:
                pass

            if a == "":
                print "Aucun fichier selectionne"
                self.aucunFichier()
            else:
                pass
        else:
            print "sfarkxtc introuvable"
            self.SfarkxtcSearch()

# Others def

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Fichier sfark", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

# Choose sfark file here

    def load(self, path, filename):

        instance = SfarkConvertorApp()
        sfarkPath = os.path.join(path)
        print "sfarkPath = " + (sfarkPath)
        sfarkName = (filename)
        print "sfarkName"
        print sfarkName
        if not sfarkName:
            sfarkName = "/"
        del instance.sfarkPath[:]
        instance.sfarkPath.extend(sfarkName)
        print "sfarkPath"
        print (instance.sfarkPath)
        self.dismiss_popup()
        return instance.sfarkPath

    def APropos(self):

        XBoxLayout.text = 'sfArk-convertor, Cre' + u'\u00E9' + ' par Maltouzes'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="A propos", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

# App -------------------------------


class SfarkConvertorApp(App):
    title = "sfArk Convertor"
    sfarkPath = []
    sfarkFileName = []
    pass

if __name__ == '__main__':
    app = SfarkConvertorApp()
    app.run()
