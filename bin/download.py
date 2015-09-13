#!/usr/bin/env python

""" Installation script for sfArk-convertor: It make you the possibility
to download and install sfArkLib and sfarkxtc.
You must enter your root password, after the installation please run main.py
for launch sfark-convertor """

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import zipfile
import requests
import urllib
import os


class XBoxLayout(BoxLayout):
    """ Kivy default BoxLayout """
    cancel = ObjectProperty(None)


class Download(BoxLayout):
    """ Main Kivy BoxLayout """
    _popup = ObjectProperty(None)
    file_hello = StringProperty('Hello')
    name = StringProperty(None)
    first_dl = "https://github.com/raboof/sfArkLib/archive/master.zip"
    second_dl = "https://github.com/raboof/sfarkxtc/archive/master.zip"
    current_dir = os.getcwd()

    def about(self):
        """ About popup """
        XBoxLayout.text = "This script will download and install\nsfArkLib and sfarkxtc.\nNeed root privileges."
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="About", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    @staticmethod
    def rm_zip(zip_file):
        """ Clean up method """
        rm_file = Download.current_dir + "/" + str(zip_file)
        if os.path.exists(rm_file) is True:
            os.remove(zip_file)
            print zip_file + " removed"

    @staticmethod
    def installation():
        """ Installation process  """
        print Download.first_dl
        print Download.second_dl
        print Download.name
        Download.sfark_dl(Download.first_dl)
        print Download.name
        print Download.current_dir
        Download.unzip(Download.name)
        Download.rm_zip(Download.name)
        Download.sfark_dl(Download.second_dl)
        Download.unzip(Download.name)
        Download.rm_zip(Download.name)

    @staticmethod
    def sfark_dl(file_dl):
        """ Download library """
        url_work = requests.get(file_dl)
        length = int(url_work.headers['content-length'])/1000
        name = url_work.headers['content-disposition'].split('=')[-1]
        print "You wil download %s, the file size is %sKo." % (name, length) +\
              " Please be patient."
        urllib.urlretrieve(file_dl, name)
        Download.name = name

    @staticmethod
    def unzip(file_unzip):
        """ Unzip a file """
        print "file_unzip"
        zfile = zipfile.ZipFile(file_unzip)
        zfile.extractall("")

    @staticmethod
    def make_sfarklib():
        """ Installation of sfarklib  """
        print "make_sfarklib"

    def dismiss_popup(self):
        """ Method: Used for dismiss popup """
        self._popup.dismiss()


class DownloadApp(App):
    """ Main class  """
    title = "sfArk convertor installation"

if __name__ == '__main__':
    PROG = DownloadApp()
    PROG.run()
