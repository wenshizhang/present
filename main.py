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

	namepage = createNamepage(wiz);
	secpage = createWelcomepage(wiz);
	happypage = createHappypage(wiz);
	misspage = createMisspage(wiz);

	wiz.addPage(namepage);
	wiz.addPage(secpage);
	wiz.addPage(happypage);
	wiz.addPage(misspage);
	Wizard.setwindow(wiz);
	wiz.show();

	sys.exit(app.exec_());


def createNamepage(wiz):
	page,layout = Wizard.createPage()

	Wizard.setPageLabel(unicode("你叫什么名字呀！:)",'utf-8'),page,layout);
	edit = Wizard.setInput(page,layout);
	Wizard.setButton(page,"",unicode("我写好了","utf-8"),"");

	return page;

def createWelcomepage(wiz):
	page,layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("太好了，我就是找你呀！ :)",'utf-8'),page,layout);
	Wizard.setPageLabel(unicode("今天开不开心呀? :)",'utf-8'),page,layout);

	Wizard.setButton(page,unicode("不开心","utf-8"),unicode("当然开心啦","utf-8"),"")

	return page;

def createHappypage(wiz):
	page,layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("今天在干嘛呀 :)",'utf-8'),page,layout);
	Wizard.setButton(page,unicode("当然是工作啦","utf-8"),unicode("在想你呀","utf-8"),
			unicode("七夕快乐呀，大臭臭 :)","utf-8"))

	return page;

def createMisspage(wiz):
	page,layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("在想我呀，我也想你呢 :)",'utf-8'),page,layout);

	return page;


main();
