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

	namePage = createNamePage(wiz);
	secPage = createWelcomePage(wiz);
	happyPage = createHappyPage(wiz);
	missPage = createMissPage(wiz);
	candyPage = createCandyPage(wiz);
	eatcandyPage = createEatCandyPage(wiz);
	sweetPage = createSweetPage(wiz);
	sweetyouPage = createSweetYouPage(wiz);
	sweetPage = createSweetPage(wiz);
	meatPage = createMeatPage(wiz);
	eatmeatPage = createEatMeatPage(wiz);

	wiz.addPage(namePage);
	wiz.addPage(secPage);
	wiz.addPage(happyPage);
	wiz.addPage(missPage);
	wiz.addPage(candyPage);
	wiz.addPage(eatcandyPage);
	wiz.addPage(sweetPage);
	wiz.addPage(sweetyouPage);
	wiz.addPage(meatPage);
	wiz.addPage(eatmeatPage);
	Wizard.setwindow(wiz);
	wiz.show();

	sys.exit(app.exec_());


def createNamePage(wiz):
	Page,Layout = Wizard.createPage()

	Wizard.setPageLabel(unicode("你叫什么名字呀！:)",'utf-8'),Page,Layout);
	edit = Wizard.setInput(Page,Layout);
	Wizard.setButton(Page,"",unicode("我写好了","utf-8"),"");

	return Page;

def createWelcomePage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("太好了，我就是找你呀！ :)",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("今天开不开心呀? :)",'utf-8'),Page,Layout);

	Wizard.setButton(Page,unicode("不开心","utf-8"),unicode("当然开心啦","utf-8"),"")

	return Page;

def createHappyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("今天在干嘛呀 :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("当然是工作啦","utf-8"),unicode("在想你呀","utf-8"),
			"")

	return Page;

def createMissPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("在想我呀，我也想你呢 :)",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("对呀，超级超级想你呢！ :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("哼，我才不信呢","utf-8"),unicode("我相信啦","utf-8"),
			unicode("七夕快乐呀，大臭臭 :)","utf-8"));

	return Page;

def createCandyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("哈哈，我们过得第一个七夕节呢，送给宝宝的零食礼包喜欢吗？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不喜欢","utf-8"),unicode("喜欢呀","utf-8"),"");

	return Page;

def createEatCandyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("好了，吃一块糖好不好呀？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不想吃，心情不好","utf-8"),unicode("正在吃呢","utf-8"),"");

	return Page;

def createSweetPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("甜不甜呀？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不甜","utf-8"),unicode("甜呀","utf-8"),"");

	return Page;

def createSweetYouPage(wiz):

	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("那是因为老公很甜呀，甜甜蜜蜜的呢! :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("我还要听一遍","utf-8"),unicode("我要看下一页","utf-8"),
			unicode("七夕快乐呀，大臭臭 :)","utf-8"));

	return Page;

def createMeatPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("饿不饿呀，要不要吃一块肉肉？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("哼，不吃","utf-8"),unicode("要吃要吃","utf-8"),"");

	return Page;

def createEatMeatPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("多吃一点，老公这么好看，吃什么都不会胖的！:)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("再吃一块肉肉","utf-8"),unicode("我要吃别的","utf-8"),
			unicode("七夕快乐呀，大臭臭 :)","utf-8"));

	return Page;

main();
