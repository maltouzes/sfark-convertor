#!/usr/bin/env python

"""sfark-convertor is a simple GUI Sfark decompressor to sf2, it convert
soundfonts in the legacy sfArk v2 file format to sf2.
Only Linux is supported."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

import subprocess
import os
import threading


class LoadDialog(BoxLayout):
    """ Kivy BoxLayout """
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class LoadingPopup(BoxLayout):
    """ LoadingPopup  """


class XBoxLayout(BoxLayout):
    """ Kivy default BoxLayout """
    cancel = ObjectProperty(None)


class Sfark(BoxLayout):
    """ Main Kivy Boxlatout """
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    _popup = ObjectProperty(None)
    file_selected_is = StringProperty('No file selected')
    file_selected = StringProperty('')
    file_hello = StringProperty('Please choose a sfArk file')
    result_file = ""
    exe = StringProperty("/")
    sfarkxtc_path = StringProperty('/')

    @staticmethod
    def sfark_root_path():
        """ Check if sfarkxtc exist in path """
        if subprocess.call(["which", "sfarkxtc"]) == 0:
            process_sfark = subprocess.check_output(["which", "sfarkxtc"])
            Sfark.sfarkxtc_path = "sfarkxtc found"
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
        XBoxLayout.text = 'sfArk-convertor, made by Maltouzes'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="About", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def no_file_selected(self):
        """ Popup window if no file is selected """
        XBoxLayout.text = "No file selected"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def successful(self):
        """ Popup window successfull conversion  """
        XBoxLayout.text = "Successful conversion"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk to sf2", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def incompatible(self):
        """ Popup window Inconpatible sfArk version """
        XBoxLayout.text = 'sfArk file is incompatible (file is not a sfArk v2)'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Please choose a sfArk v2 file",
                            content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def corrupt(self):
        """ Popup window file corrupt """
        XBoxLayout.text = 'This file is not a sfArk file'
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Please choose a sfArk file",
                            content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def loading(self):
        """ Popup window loading """
        LoadingPopup.text = "Loading, please wait..."
        content = LoadingPopup()
        self._popup = Popup(title="Please wait",
                            content=content,
                            size_hint=(1, 1))
        self._popup.open()

    def sfark_xtc_search(self):
        """ Popup window sfarkxtc not found """
        XBoxLayout.text = "Can't find sfarkxtc, please see Installation"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="sfarkxtc not found", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    @staticmethod
    def cmd_method(word):
        """ Convert word: terminal command compatibility  """
        word = word.replace(" ", "\\ ")
        word = word.replace("(", "\\(")
        word = word.replace(")", "\\)")
        return word

    def test_convert(self, exe):
        """ test_convert """
        p_exe = subprocess.Popen(exe, shell=True)
        p_exe.communicate()
        code_return = p_exe.returncode
        print "code_return"
        print code_return
        if code_return != "":
            print "bye bye"
            print code_return
            self._popup.dismiss()
            if "0" in str(code_return):
                self.successful()
            elif "1" in str(code_return):
                self.corrupt()
            elif "2" in str(code_return):
                self.corrupt()
            elif "3" in str(code_return):
                self.corrupt()
            elif "4" in str(code_return):
                self.corrupt()
            elif "5" in str(code_return):
                self.incompatible()
            elif "6" in str(code_return):
                self.incompatible()
            elif "7" in str(code_return):
                self.corrupt()
            elif "8" in str(code_return):
                self.corrupt()
            elif "9" in str(code_return):
                self.corrupt()
            elif "10" in str(code_return):
                self.corrupt()
            elif "11" in str(code_return):
                self.corrupt()
            else:
                pass
        else:
            pass

    def test_threading(self):
        """ Call convert_sfark in a thread  """
        Sfark.sfark_root_path()
        if Sfark.sfarkxtc_path == "sfarkxtc found":
            self.convert_sfark()
            t_exe = threading.Thread(target=self.test_convert,
                                     args=(Sfark.exe,))
            t_exe.start()
        else:
            self._popup.dismiss()
            self.sfark_xtc_search()

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
            sfark_file_name = Sfark.cmd_method(sfark_file_name)
            print "sfarkFileName = " + sfark_file_name
            sf2_file_name = sfark_file_name[:-5] + "sf2"
            print "sf2FileName = " + (sf2_file_name)
            cmd_sfark_file_path = Sfark.cmd_method(sfark_file_path)
            print sfark_file_path
            exe = "cd " + (cmd_sfark_file_path) + " && sfarkxtc " + \
                  (sfark_file_name) + " " + (sf2_file_name)
            print exe
            Sfark.exe = exe
        else:
            print "sfarkxtc not found"
            self.file_hello = "sfarkxtc not found, please see Installation"
            self.sfark_xtc_search()

# Others def

    def dismiss_popup(self):
        """ Method: Used for dismiss popup """
        self._popup.dismiss()

    def show_load(self):
        """ Popup window filechooser """
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="sfArk file", content=content,
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
        self.file_selected_is = 'File selected is'
        self.file_selected = ''.join(instance.sfark_path)
        if 'sfArk' in str(instance.sfark_path):
            self.file_hello = "Please, click on convert for decompress the" +\
                              " sfArk file to sf2 file"
        else:
            pass
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
