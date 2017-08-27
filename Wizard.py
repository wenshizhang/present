#!/usr/bin/python
#File Name: wizard.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Mon 21 Aug 2017 11:07:07 AM CST
#Description:
#########################################################################

import sys
from PyQt4 import QtGui,QtCore

def backEvent():
	wiz = QtGui.QWizard();
	page = QtGui.QWizardPage();

	label = QtGui.QLabel(page);
	label.setText("this message just for show");

	wiz.addPage(page);
	wiz.show();

def printmessage(wiz):
	print "this message just for show";

def createPage():
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
	edit.resize(50,50);
	edit.setFixedWidth(200);
	layout.addWidget(edit);
	page.setLayout(layout);

	return edit;

def setwindow(wiz):
	wiz.setWindowTitle("Present for Yanfei");
	wiz.setGeometry(300,100,900,300);
	wiz.setWizardStyle(QtGui.QWizard.ModernStyle);

	wiz.setOption(QtGui.QWizard.NoBackButtonOnStartPage);
	wiz.setOption(QtGui.QWizard.NoCancelButton);

def setButton(page,Back,Next,Finish):
	if Back.strip():
		page.setButtonText(QtGui.QWizard.BackButton,Back);
	if Next.strip():
		page.setButtonText(QtGui.QWizard.NextButton,Next);
	if Finish.strip():
		page.setButtonText(QtGui.QWizard.FinishButton,Finish);


