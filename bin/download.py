#!/usr/bin/env python

""" Installation script for sfArk-convertor: It make you the possibility
to download and install sfArkLib and sfarkxtc.
You must enter your root password, after the installation please run main.py
for launch sfark-convertor """

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

import zipfile
import requests
import urllib
import os
import threading
import subprocess


class XBoxLayout(BoxLayout):
    """ Kivy default BoxLayout """
    cancel = ObjectProperty(None)


class LoadingPopup(BoxLayout):
    """ Kivy loading popup """


class Download(BoxLayout):
    """ Main Kivy BoxLayout """
# Kivy property
    _popup = ObjectProperty(None)
# Start page string
    file_hello = StringProperty('Hello')
#
    name = StringProperty(None)
# url file to download
    first_dl = "https://github.com/raboof/sfArkLib/archive/master.zip"
    second_dl = "https://github.com/raboof/sfarkxtc/archive/master.zip"
# get the current dir of the application
    current_dir = os.getcwd()
# should removed !!!
    test_dl = "https://github.com/maltouzes/sfark-convertor/archive/master.zip"

    @staticmethod
    def rm_zip(zip_file):
        """ Revove downloaded zip file """
        rm_file = Download.current_dir + "/" + str(zip_file)
        if os.path.exists(rm_file) is True:
            os.remove(zip_file)
            print zip_file + " removed"

    def test_threading(self):
        """ Call installation in a thread """
        t_exe = threading.Thread(target=self.installation)
        t_exe.start()

    def installation(self):
        """ Installation process  """
        print Download.name
        print Download.current_dir
        # Download.sfark_dl(Download.test_dl)
        # Download.unzip(Download.name)
        # Download.rm_zip(Download.name)

        try:
            Download.sfark_dl(Download.first_dl)
            Download.unzip(Download.name)
            Download.rm_zip(Download.name)
        except KeyError:
            Download.sfark_dl(Download.first_dl)
            Download.unzip(Download.name)
            Download.rm_zip(Download.name)

        try:
            Download.sfark_dl(Download.second_dl)
            Download.unzip(Download.name)
            Download.rm_zip(Download.name)
        except KeyError:
            Download.sfark_dl(Download.second_dl)
            Download.unzip(Download.name)
            Download.rm_zip(Download.name)
        self.make_sfarklib()

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

    def make_sfarklib(self):
        """ Installation of sfarklib  """
        print "make_sfarklib"
# make sfArkLib-master
        exe = "cd " + Download.current_dir + "/sfArkLib-master" + " && make"
        print exe
        subprocess.check_call(exe, shell=True)
        libsfark = Download.current_dir + "/sfArkLib-master/libsfark.so"
        sfarklib = Download.current_dir + "/sfArkLib-master/sfArkLib.h"
# sudo make install sfArklib-master
        if os.path.isfile(libsfark) and os.path.isfile(sfarklib):
            exe = "cd && cd " + Download.current_dir + "/sfArkLib-master" +\
                  " && sudo make install"
            print exe
            subprocess.check_call(exe, shell=True)
# sudo ldconfig sfArkLib-master
            ldconfig = "sudo ldconfig"
            print ldconfig
            subprocess.check_call(ldconfig, shell=True)
# where files downloaded should be installed
            sfarklib_so = "/usr/local/lib/libsfark.so"
            sfarklib_h = "/usr/local/include/sfArkLib.h"
            sfarkxtc = "/usr/local/bin/sfarkxtc"
# Check if sfarkLib installed successfully
            if os.path.isfile(sfarklib_so) and os.path.isfile(sfarklib_h):
                print "sfArkLib ok"
                exe = "cd && cd " + Download.current_dir + "/sfarkxtc-master\
                   && sudo make"
                print exe
                subprocess.check_call(exe, shell=True)
# Check if sfarkxtc installed successfully
                if os.path.isfile(sfarkxtc):
                    print "sfarkxtc ok"
                    self.dismiss_popup()
                    self.finish()
                else:
                    self.dismiss_popup()
                    self.abort()
        else:
            self.dismiss_popup()
            self.abort()

    def dismiss_popup(self):
        """ Method: Used for dismiss popup """
        self._popup.dismiss()

    def about(self):
        """ About popup """
        XBoxLayout.text = "This script will download and install" +\
                          " sfArkLib and sfarkxtc.\nNeed root privileges."
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="About", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def finish(self):
        """ Popup installation finish  """
        XBoxLayout.text = "Installation successful you can now run main.py"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Insastallation Successful", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def abort(self):
        """ Popup installation aborted """
        XBoxLayout.text = "Installation aborted, please try again"
        content = XBoxLayout(cancel=self.dismiss_popup)
        self._popup = Popup(title="Installation Aborted",
                            content=content,
                            size_hint=(0.9, 0.9))

    def loading(self):
        """ Loading popup """
        LoadingPopup.text = "Loading, please wait"
        content = LoadingPopup()
        self._popup = Popup(title="Loading",
                            content=content,
                            size_hint=(1, 1))
        self._popup.open()


class DownloadApp(App):
    """ Main class  """
    title = "sfArk convertor installation"

if __name__ == '__main__':
    PROG = DownloadApp()
    PROG.run()
