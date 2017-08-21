#!/usr/bin/python
## -*- coding: UTF-8 -*-
#File Name: main.py
#Author: echo zhang
#mail: shi.safari@gmail.com
#Created Time: Mon 21 Aug 2017 11:06:09 AM CST
#Description:
#########################################################################

import sys
from PyQt4 import QtGui
import Wizard


def main():
	app = QtGui.QApplication(sys.argv);
	wiz = QtGui.QWizard();
	welcomepage,layout = Wizard.createPage()

	#welcome page
	Wizard.setPageLabel(unicode("你叫什么名字呀！:)",'utf-8'),welcomepage,layout);
	edit = Wizard.setInput(welcomepage,layout);

	secpage,layout = Wizard.createPage();
	Wizard.setPageLabel(unicode("太好了，我就是找你呀！ :)",'utf-8'),secpage,layout);
#	name = str(edit.text());

	wiz.addPage(welcomepage);
	wiz.addPage(secpage);
	wiz.setWindowTitle("Present for Yanfei");
	wiz.setWizardStyle(QtGui.QWizard.ModernStyle);
	wiz.show();

	sys.exit(app.exec_());

main();
