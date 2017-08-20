#!/usr/bin/python
#File Name: windows.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Sat 19 Aug 2017 09:30:56 AM CST
#Description:
#########################################################################

import sys
from PyQt4 import QtGui

class AppWindow(QtGui.QWidget):

	def __init__(self):
		super(AppWindow,self).__init__();

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def text(self,lineMessage):
		lb = QtGui.QLabel(lineMessage,self);
		lb.move(50,50);
		return lb;

	def button(self,buttonName,buttonTooltip):
		btn = QtGui.QPushButton(buttonName,self);
		btn.setToolTip(buttonTooltip);
		btn.resize(btn.sizeHint());
		btn.move(50,100);
		return btn;

