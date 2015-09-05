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
    """ Kivy BoxLayout """
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class XBoxLayout(BoxLayout):
    """ Kivy default BoxLayout """
    cancel = ObjectProperty(None)


class Sfark(BoxLayout):
    """ Main Kivy Boxlatout """
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    _popup = ObjectProperty(None)

    @staticmethod
    def sfark_root_path():
        """ Check if sfarkxtc exist in path """
        if subprocess.call(["which", "sfarkxtc"]) == 0:
            process_sfark = subprocess.check_output(["which", "sfarkxtc"])
            return process_sfark.strip()
        else:
            process_sfark = "/"
            return process_sfark
# Add current dir path for sfarkxtc
# else:
# p = subprocess.check_output(["pwd"])
# p =  p.strip() +"/sfarkxtc"
# print p
# return p

    def about(self):
        """ About me popup """
        XBoxLayout.text = 'sfArk-convertor, Cre' + u'\u00E9' + ' par Maltouzes'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="A propos", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def no_file_selected(self):
        """ Popup window if no file is selected """
        XBoxLayout.text = "Aucun fichier selectionn" + u'\u00E9'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def successful(self):
        """ Popup window successfull conversion  """
        XBoxLayout.text = "Conversion reussie"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def incompatible(self):
        """ Popup window Inconpatible sfArk version """
        XBoxLayout.text = 'Version sfArk non prise en charge \
                          (version 2 uniquement'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def corrupt(self):
        """ Popup window file corrupt """
        XBoxLayout.text = 'Veuillez choisir un fichier sfArk'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Fichier sfArk non valide",
                            content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def sfark_xtc_search(self):
        """ Popup window sfarkxtc not found """
        XBoxLayout.text = "sfarkxtc introuvable"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def convert_sfark(self):
        """ Convert processs """
        instance = SfarkConvertorApp()
        sfarkxtc = Sfark.sfark_root_path()

        print "sfarkPath"
        print instance.sfark_path
        sfark_path = instance.sfark_path
        if os.path.isfile(sfarkxtc):
            print "sfarkxtc found"

# convert file.sfArk to file.sf2
            sfark_path = "".join(sfark_path)
            sfark_file_path = os.path.dirname(sfark_path)
            print "sfarkFilePath = " + sfark_file_path
            sfark_path = sfark_path.split("/")
            sfark_file_name = sfark_path[-1]
            print "sfarkFileName = " + sfark_file_name
            sf2_file_name = sfark_file_name[:-5] + "sf2"
            print "sf2FileName = " + (sf2_file_name)

            exe = "cd " + (sfark_file_path) + " && sfarkxtc " + \
                  (sfark_file_name) + " " + (sf2_file_name) + \
                  " > sfarkTest.txt"
            print exe
            subprocess.call(exe, shell=True)

# call sfarkTest.txt
            sfark_path_txt = (sfark_file_path) + "/sfarkTest.txt"
            print "sfarkFilePath = " + sfark_file_path
            print "sfarkPathtxt = " + sfark_path_txt
            result_file = ""

# Check if sfarkPathtxt exist
            if os.path.isfile(sfark_path_txt):
                result_file = open(sfark_path_txt).read().lower()
            print "result_file = " + result_file
            type(result_file)

# test corrupt in sfarkTest
            if "corrupt" in result_file or "i/o" in result_file:
                print "Veuillez choisir un fichier sfArk"
                self.corrupt()
            else:
                pass

            if "incompatible" in result_file:
                print "Version sfArk non prise en charge \
                       (version 2 uniquement)"
                self.incompatible()
            else:
                pass

            if "successful" in result_file:
                print "Conversion reussie"
                rm_sfark_path_txt = "rm " + (sfark_path_txt)
                subprocess.call(rm_sfark_path_txt, shell=True)

                self.successful()
            else:
                pass

            if result_file == "":
                print "Aucun fichier selectionne"
                self.no_file_selected()
            else:
                pass
        else:
            print "sfarkxtc introuvable"
            self.sfark_xtc_search()

# Others def

    def dismiss_popup(self):
        """ Method: Used for dismiss popup """
        self._popup.dismiss()

    def show_load(self):
        """ Popup window filechooser """
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Fichier sfark", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

# Choose sfark file here

    def load(self, path, filename):
        """ File select Method """
        instance = SfarkConvertorApp()
        sfark_path = os.path.join(path)
        print "sfarkPath = " + (sfark_path)
        sfark_name = (filename)
        print "sfarkName"
        print sfark_name
        if not sfark_name:
            sfark_name = "/"
        del instance.sfark_path[:]
        instance.sfark_path.extend(sfark_name)
        print "sfarkPath"
        print instance.sfark_path
        self.dismiss_popup()
        return instance.sfark_path

# App -------------------------------


class SfarkConvertorApp(App):
    """ Main class  """
    title = "sfArk Convertor"
    sfark_path = []
    sfark_file_name = []

if __name__ == '__main__':
    PROG = SfarkConvertorApp()
    PROG.run()
