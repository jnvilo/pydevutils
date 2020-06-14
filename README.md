Python Dev Utils
===

A collection of commands and functions used for building modules and developing python code.

Provides the following commands: 

* bump_package_patch_version - when run inside a module with setup.py, it will update the VERSION. 
* make-github-repo - Automate the creation of github repo. This command will create a local repo or if you already have an existing repo, it will connect to your github account and create a remote repo to push your code to. 

How to Install:
---

The simplest way to install is via pip:

     pip install pydevutils
     
However you are probably here because you want to install the latest version or develop it. The best way to do this is to set it up as if for development. 

Installing it and using a virtualenv is as follows:

     git clone https://github.com/jnvilo/pydevutils.git
     cd  pydevutils
     virtualenv venv 
     source venv/bin/activate
     python setup.py install 
     
How to Install for Development

pydevutils comes with a makefile that will build a version of python and install it into a virtualenv inside the pydevutils. In order for this to work, there are some requirements:

Fedora/Centos/RHEL

    yum -y install npm gcc sqlite-devel openssl-devel libtiff-devel openjpeg-devel \
    openjpeg2-devel libjpeg-turbo-devel  zlib-devel  freetype-devel lcms-devel \
    lcms2-devel libexif-devel libffi-devel

With the requirements installed do:

     git clone https://github.com/jnvilo/pydevutils.git
     cd  pydevutils  
     
     
And with your favourite text editor edit configuration.mk

     # Paths
    GIT ?= /usr/bin/git
    FIND ?= /usr/bin/find

    # Python
    PYTHON_VERSION ?= 3.6.1
    VENV_VERSION ?= 15.1.0

Now run make, and it will chug along building the specified python version and at the end of it you have a virtualenv. 

     make
     
At this point , inside the pydevutils directory should exist a virtualenv symlink. We can activate and use this as follows:

     source venv/bin/activate

Install pydevutils as a develop symlink.

     python setup.py develop
     
At this point you can modify the sources and develop pydevutils further to your hearts content.
     

Test
---

The test suit will build its own python version using the makefile. 




    make test

You can also test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test
