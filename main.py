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
	valentinePage = createValentinePage(wiz);
	openPage = createOpenPage(wiz);
	eatcandyPage = createEatCandyPage(wiz);
	sweetPage = createSweetPage(wiz);
	sweetyouPage = createSweetYouPage(wiz);
	sweetPage = createSweetPage(wiz);
	meatPage = createMeatPage(wiz);
	eatmeatPage = createEatMeatPage(wiz);
	eatsaltypage = createEatSaltyPage(wiz);
	saltypage = createSaltyPage(wiz);
	eatsourpage = createEatSourPage(wiz);
	sourpage = createSourPage(wiz);
	eatspicypage = createEatSpicyPage(wiz);
	spicypage = createSpicyPage(wiz);
	chapter2page = createChapter2Page(wiz);
	wantpage = createWantPage(wiz);
	trustpage = createTrustPage(wiz);
	understandpage = createUnderstandPage(wiz);
	lastpage = createLastPage(wiz);

	wiz.addPage(namePage);
	wiz.addPage(secPage);
	wiz.addPage(happyPage);
	wiz.addPage(missPage);
	wiz.addPage(valentinePage);
	wiz.addPage(openPage);
	wiz.addPage(eatcandyPage);
	wiz.addPage(sweetPage);
	wiz.addPage(sweetyouPage);
	wiz.addPage(meatPage);
	wiz.addPage(eatmeatPage);
	wiz.addPage(eatsaltypage);
	wiz.addPage(saltypage);
	wiz.addPage(eatsourpage);
	wiz.addPage(sourpage);
	wiz.addPage(eatspicypage);
	wiz.addPage(spicypage);
	wiz.addPage(chapter2page);
	wiz.addPage(wantpage);
	wiz.addPage(trustpage);
	wiz.addPage(understandpage);
	wiz.addPage(lastpage);
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

def createValentinePage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("哈哈，我们过得第一个七夕节呢，送给宝宝的零食礼包喜欢吗？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不喜欢","utf-8"),unicode("喜欢呀","utf-8"),"");

	return Page;

def createOpenPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("现在可以拆开礼物啦，快去拆吧！",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("粗心大意快递已经丢啦","utf-8"),unicode("力大无比已经拆开啦","utf-8"),"");

	return Page;

def createEatCandyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("现在吃一块糖好不好呀？",'utf-8'),Page,Layout);
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
	Wizard.setButton(Page,unicode("再吃一块肉肉","utf-8"),unicode("我要吃别的","utf-8"),"");

	return Page;

def createEatSaltyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("吃一块咸咸的饼干好不好呀？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不吃不吃不想吃","utf-8"),unicode("好呀好呀我最听话啦","utf-8"),"");

	return Page;

def createSaltyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("老公不喜欢吃甜的东西，咸的好不好吃呀？",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("臭臭也是我的调味剂呀，有你生活很有滋味呢 :) ",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("再吃一块饼干","utf-8"),unicode("开心，我要吃别的啦","utf-8"),
			unicode("七夕快乐呀，大臭臭 :)","utf-8"));

	return Page;

def createEatSourPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("吃了这么多啦，来一块酸酸的梅干消化一下好不好呀？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("等会哈，正在找呢","utf-8"),unicode("找到啦，正在吃呢","utf-8"),"");

	return Page;

def createSourPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("好酸呀好酸呀，眼睛都睁不开啦。",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("酸过了，是不是觉得回甘的感觉还不错,无味也是甜的呢",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("所以呀我们会吵架会不理对方，等过去了会更爱你更甜蜜，别想太多好不好呢 :)",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("可能是两个火象星座，都怕生活变得沉寂如海。虽然最后都会归于平静平凡平庸，但至少在开始的时候是灿若花火:)",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("我爱你，大臭臭 :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("再吃一次梅干","utf-8"),unicode("猜猜看下一个是什么","utf-8"),"");

	return Page;

def createEatSpicyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("吃块豆干？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("等会哈，正在找呢","utf-8"),unicode("找到啦，正在吃呢","utf-8"),"");

	return Page;

def createSpicyPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("辣不辣，好不好吃？",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("老公是不是也觉得，幸福有时候也是辣辣的。懵懵的辣辣的，回想起来暖暖的。",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("老公呀，一直没跟你说：有你真好，谢谢你来了，你来了就够了 :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("哼哼，还要吃豆干","utf-8"),unicode("不用谢啦，有你也很好呀","utf-8"),"");

	return Page;

def createChapter2Page(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("我希望对臭臭来说是什么样子的人？",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("不看不看我不想知道","utf-8"),unicode("点开看看","utf-8"),"");

	return Page;

def createWantPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("明白臭臭身体累了，心里不开心",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("前一个","utf-8"),unicode("下一个","utf-8"),"");

	return Page;

def createTrustPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("信任意味着忍耐克己,总是相信每一个决定每一句话的出发点是为了对方",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("我愿意相信臭臭",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("前一句话","utf-8"),unicode("下一句话","utf-8"),"");

	return Page;

def createUnderstandPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("理解臭臭",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("前一句话","utf-8"),unicode("下一句话","utf-8"),"");

	return Page;

def createLastPage(wiz):
	Page,Layout = Wizard.createPage()
	
	Wizard.setPageLabel(unicode("吵架的时候不可以太僵，彼此都要克制，不可以总想着伤害对方",'utf-8'),Page,Layout);
	Wizard.setPageLabel(unicode("我爱你，mua～ :)",'utf-8'),Page,Layout);
	Wizard.setButton(Page,unicode("想你","utf-8"),unicode("爱你","utf-8"),unicode("情人节快乐","utf-8"));

	return Page;

main();
