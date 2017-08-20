#!/usr/bin/python
#-*-coding:utf-8 -*-
#File Name: main.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Sat 19 Aug 2017 09:47:08 AM CST
#Description:
#########################################################################

import sys
from windows import AppWindow
from PyQt4 import QtGui,QtCore
from functools import partial

app = QtGui.QApplication(sys.argv);

def main():
#	app = QtGui.QApplication(sys.argv)
	aw = AppWindow()
	aw.resize(500,150);
	aw.center()

	text = unicode("你是谁呀？",'utf-8');
	text, ok = QtGui.QInputDialog.getText(aw,"Input Dialog",text);

	if ok:
		lb = aw.text(text + unicode(" 太好了我就是找你呀！ :) " , 'utf-8'));

	btn = aw.button("start","Click for start");
#	aw.connect(btn,	QtCore.SIGNAL('clicked()'),startClicked);
	btn.clicked.connect(partial(startClicked,aw));
	aw.setWindowTitle("Present for Yanfei");
	aw.show();
	sys.exit(app.exec_())

def startClicked(aw):
	aw.close()
	app.quit()
	app = QtGui.QApplication(sys.argv)
	aw = AppWindow()
	aw.resize(500,150)
	aw.center();
	aw.text("this is second windows");
	aw.show()
	sys.exit(app.exec_())


main();
