#!/usr/bin/python
#File Name: wizard.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Mon 21 Aug 2017 11:07:07 AM CST
#Description:
#########################################################################

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

def createPage():
#new pages, new layout
	page = QtGui.QWizardPage();
	layout = QtGui.QVBoxLayout();
	return page,layout;

def setPageLabel(labeltext,page,layout):
	label = QtGui.QLabel(page);
	label.setText(labeltext);

	font = QtGui.QFont('SansSerif', 13);
	font.setBold(True);
	label.setFont(font);

	layout.addWidget(label);
	page.setLayout(layout);

def setInput(page,layout):
	edit = QtGui.QLineEdit(page);
	layout.addWidget(edit);
	page.setLayout(layout);

	return edit;

