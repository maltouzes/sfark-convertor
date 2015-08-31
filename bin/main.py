#!/usr/bin/env python

"""sfark-convertor is a simple GUI Sfark decompressor to sf2, it convert
soundfonts in the legacy sfArk v2 file format to sf2.
Only Linux is supported."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty

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
        p = subprocess.check_output(["which","sfarkxtc"])
        print p
        return p.strip()

    def convertSfark(self):
        instance = SfarkConvertorApp()
        sfarkxtcPath = os.getcwd()
        sfarkxtc = self.sfarkrootpath()
        print sfarkxtc
        (sfarkPath) = instance.sfarkPath
        print "instance.sfarkPath load = "
        print instance.sfarkPath
        (sfarkFileName) = instance.sfarkFileName
        print "instance.sfarkFileName load = "
        print instance.sfarkFileName

        instance = SfarkConvertorApp()
        sfarkPath = instance.sfarkPath
        print "instance.sfarkPath = "
        sfarkPath = "".join(sfarkPath)
        print sfarkPath
        sfarkFileName = instance.sfarkFileName
        if os.path.isfile(sfarkxtc):
            print "sfarkxtc found"

# convert file.sfArk to file.sf2
            sfarkFileName = ''.join(sfarkFileName)
            lenSfarkFileName = len(sfarkFileName)
            lenSfarkFileNameOk = lenSfarkFileName - 5
            sf2FileName = (sfarkFileName[:lenSfarkFileNameOk]) + "sf2"

            exe = "cd " + (sfarkPath) + " && sfarkxtc " + (sfarkFileName) + \
                  " " + (sf2FileName) + " > sfarkTest.txt"

            print "sf2FileName = " + (sf2FileName)
            print exe
            subprocess.call(exe, shell=True)

# call sfarkTest.txt
            sfarkPathtxt = (sfarkPath) + "/sfarkTest.txt"
            print "sfarkPath = " + sfarkPath
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

                def corrupt(self):
                    XBoxLayout.text = 'Veuillez choisir un fichier sfArk'
                    content = XBoxLayout(cancel=self.dismiss_popup)
                    self._popup = Popup(title="Fichier sfArk non valide",
                    content=content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()

                corrupt(self)
            else:
                pass

            if "incompatible" in a:
                print "Version sfArk non prise en charge (version 2 uniquement)"
                def incompatible(self):
                    XBoxLayout.text = 'Version sfArk non prise en charge \
                                      (version 2 uniquement'
                    content = XBoxLayout(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content=content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()

                incompatible(self)
            else:
                pass

            if "successful" in a:
                print "Conversion reussie"
                rmsfarkPathtxt = "rm " + (sfarkPathtxt) 
                subprocess.call(rmsfarkPathtxt, shell=True)
                def Successful(self):
                    XBoxLayout.text = "Conversion reussie"
                    content = XBoxLayout(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content=content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()

                Successful(self)
            else:
                pass


            if a == "":
                print "Aucun fichier selectionne"

                def aucunFichier(self):
                    XBoxLayout.text = "Aucun fichier selectionn" + u'\u00E9'
                    content = XBoxLayout(cancel=self.dismiss_popup)
                    self._popup = Popup(title="sfArk to sf2", content=content,
                                        size_hint=(0.9, 0.9))
                    self._popup.open()

                aucunFichier(self)
            else:
                pass
        else:
            print "sfarkxtc introuvable"

            def SfarkxtcSearch(self):
                XBoxLayout.text = "sfarkxtc introuvable"
                content = XBoxLayout(cancel=self.dismiss_popup)
                self._popup = Popup(title="sfArk to sf2", content=content,
                                    size_hint=(0.9, 0.9))
                self._popup.open()

            SfarkxtcSearch(self)

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

        sfarkPath = os.path.join(path)
        print "sfarkPath = " + (sfarkPath)

        sfarkName = (filename)
        print sfarkName
        if not sfarkName:
            sfarkName = "/"
        sfarkName = sfarkName[0]
        print "sfarkName = " + sfarkName

        lenSfarkName = len(sfarkName)
        lenSfarkPath = len(sfarkPath)
        lenSfarkPath += 1

        lenok = (lenSfarkPath) - (lenSfarkName)

        sfarkFileName = (sfarkName[lenok:])
        print "sfarkFileName = " + (sfarkFileName)


        instance = SfarkConvertorApp()
        del instance.sfarkPath[:]
        del instance.sfarkFileName[:]
        (instance.sfarkPath).append(sfarkPath)
        print "instance.sfarkPath load = "
        print instance.sfarkPath
        (instance.sfarkFileName).append(sfarkFileName)
        print "instance.sfarkFileName load = "
        print instance.sfarkFileName

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
