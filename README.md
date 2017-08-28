
# INTRO

First of all, **Happy Valentine's Day, Yanfei! This is a present for you.**

Well, this "present" was made in PyQt4 which is a very useful libary. The work is did by me was simple. If you are interested in this repo or PyQt4, feel free to contact me. :)

Oh, this is the shortest README I believe.

# Structure

There are only two module for now, main and wizard. Main module control all logic, wizard module define wizard related functions. 

#TODO List

For now, present version1.0 is done, yeah! But there are some features maybe can be done in furture version. Here are the list:

* Redesign those pages, make it pretty
* Wizard back event, when user press back button, new windows should be opened
* Label text format doesn't look pretty at all, it can be adjust use html but I don't know how
 
# How to use

Just compilation main.py, very simple.

# NOTE

The present requirs PyQt4, which is toooooo diffcult to install. In Linux, it costs one command if you want to support PyQt4, quite simple. But on Windows, it took me 2 days. Finally, I know the fatal because of pyqt is not one of python standroid lib, if you get same error maybe you want to check pyqt installed, pyqt version. 

##Check whether PyQt4 is installed

There are 2 ways to do it:

* run PyQt4 hello world, just run the simplest code you will see
* go to python root directory find pyqt

##Check PyQt4 version

```
>>> import pip

>>> print(pip.pep425tags.get_support())
```
This func will show you the version list of PyQt4 are supported.

Good Luck! Any question or advice, feel free to contect me. :)
