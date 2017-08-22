#!/usr/bin/python
#File Name: wizard.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Mon 21 Aug 2017 11:07:07 AM CST
#Description:
#########################################################################

import sys
from PyQt4 import QtGui,QtCore
#from PyQt4.QtCore import Qt

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

def setwindow(wiz):
	wiz.setWindowTitle("Present for Yanfei");
	wiz.setWizardStyle(QtGui.QWizard.ModernStyle);

#	layout = [QtGui.QWizard.Stretch,QtGui.QWizard.NextButton,QtGui.QWizard.NextButton]
#	wiz.setButtonLayout(layout);

	wiz.setOption(QtGui.QWizard.NoBackButtonOnStartPage);
	wiz.setOption(QtGui.QWizard.NoCancelButton);

def setButton(page,Back,Next,Finish):
	if Back.strip():
		page.setButtonText(QtGui.QWizard.BackButton,Back);
	if Next.strip():
		page.setButtonText(QtGui.QWizard.NextButton,Next);
	if Finish.strip():
		page.setButtonText(QtGui.QWizard.FinishButton,Finish);


