# Welcome to pyDevTools

pyDevTools is a module containing tools that I use a lot for development mainly 
in python. Its capabilities are growing. Installing pyDevTools gives you access
to command line utilities that I hope will be usefull for your day to day 
development. 

## Install

You may install pydevutils using your OS python or preferrably use a virtualenv. 
So first step is to create and activate virtualenv. Otherwise if you decide to 
install in your global interpreter, you need to prepend the commands with sudo or 
run them as root. 

### Install from pypi

    pip install pydevutils

### Install from github

    git clone https://github.com/jnvilo/pydevutils.git
    python setup.py install    

## Commands


### Python module development

#### make-python-module

This command creates a python module skeleton for you complete with Makefile 
to build a specific python version, run tests, and upload to pypi. 

#### bump-python-module-version 

Running this command at the root of a python module will open the setup.py 
and increment the version. I wrote this to automate the process of building 
a newer version.


### Git and Github

#### make-github-repo

Everytime I start a project be it just a bunch of scripts or a full module, I want
to be able to quickly push it to a new github repo. It can get tedious after a 
while to have to open web browser and go create a new github repo. **make-github-repo**
makes this process very easy. 




