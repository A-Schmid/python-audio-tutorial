#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# based on PyTunes: https://github.com/chaNcharge/PyTunes
#
# MIT License
# 
# Copyright (c) 2018 chaNcharge
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

# empty Qt window that plays an audio file
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.title = 'Qt Media Player'

        if len(sys.argv) > 1:
            self.song_path = sys.argv[1]
        else:
            print("please pass an audio file as the first command line parameter")
            sys.exit(0)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(500, 500, 500, 300)
        self.show()
        self.play_file(self.song_path)

    def play_file(self, filename):
        # https://stackoverflow.com/questions/50309257/playing-audio-with-qtmultimedia

        # QMediaPlayer wants absolute paths in the QUrl format
        fullpath = QDir.current().absoluteFilePath(self.song_path) 
        url = QUrl.fromLocalFile(fullpath)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
