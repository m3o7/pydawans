pydawans
========


<img src="http://octodex.github.com/images/octobiwan.jpg" width="250px;">
<!---
more octocat art: http://octodex.github.com/
-->

## welcome
This page is intented to give people a quick starting guide to the programming language Python. The content is directed to developers trying out Python for the first time, as well as people who are new to programming and try to get up to speed quickly with pratical examples. A quick word of advice especially for the newbies - do not get discouraged - I spend a lot of time on [stackoverflow](http://stackoverflow.com/)(great ressource to check if you are stuck), meaning: programming is like life-long learning; you will never have mastered everything. And always remember: `Fear is the path to the Dark Side`.

## setup
Without further ado lets get you started!

## 1. Install me:
Python was ported to many platforms and might in fact already be running on your system. But we still have to make sure that you are running a compatible version.
Please **do not** download `Python 3.x`, as it is a newer version, which at this point does not provide the learning packages we use in this tutorial.

### Mac, Linux
Here we just need to make sure that you have a relatively new python version. This will make your life a lot easier. Just open the `terminal`-app (e.g.: [mac-os-x](http://en.wikipedia.org/wiki/Terminal_(OS_X)), [linux ubuntu](https://help.ubuntu.com/community/UsingTheTerminal)) and type the following:

```bash
python --version
```

You should get something like `Python 2.7.6`. Everything above `Python 2.6.x` and below `Python 3.x` should be more than enough for this tutorial. If you have a lower version number, please go to the [official python website](http://www.python.org/download/) and download the newest version.

### Windows
 It is not very likely that you have Python installed without your knowledge, so you can just go to the [official python website](http://www.python.org/download/) and download the newest `Python 2.7.x` for windows there. 

## 2. Installing all the other stuff
The teaching tool I am using is called [iPython notebook](http://ipython.org/notebook.html).

### [Mac, Linux](http://ipython.org/ipython-doc/stable/install/install.html#installation-using-easy-install-or-pip)

Open your terminal and type the following
```bash
easy_install ipython zmq mathlib numpy pandas tornado jinja2
```

You might receive a permission error message during your installation. Simply run the same command with a `sudo` in front of it. This will run the command in system administrator mode and install the packages properly.

You can test your setup by running:
```bash
ipython notebook --pylab inline
```

### [Windows](http://ipython.org/ipython-doc/stable/install/install.html#windows)

Install the [setuptools](https://pypi.python.org/pypi/setuptools#windows), if needed.

```bat
cd C:\Python27\Scripts
.\easy_install.exe ipython[zmp]
.\easy_install.exe math­lib
.\easy_install.exe numpy
.\easy_install.exe pandas
.\easy_install.exe tornado
.\easy_install.exe jinja2
```

You can test the server by running:
```bash
ipython notebook --pylab inline
```

## 3. Lets finally get started

[Download](https://github.com/marcopashkov/pydawans/archive/master.zip) the project as a zip(`pydawans-master.zip`) file and unpack it(or if you have experience with github you can also `checkout` this repository).

### Mac, Linux, Windows
```bash
cd <PATH-TO-UNPACKED-FOLDER>
### e.g.: (Mac, Linux)
### cd /Users/marco/Downloads/pydawans-master/
### (Windows)
### cd C:\Downloads\pydawans-master\

ipython notebook --pylab inline
```

The following browser window should open:




