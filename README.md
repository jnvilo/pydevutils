Python Dev Utils
===

A collection of commands and functions used for building modules and developing python code.

Provides the following commands: 

* bump_package_patch_version - when run inside a module with setup.py, it will update the VERSION. 
* make-github-repo - Automate the creation of github repo. This command will create a local repo or if you already have an existing repo, it will connect to your github account and create a remote repo to push your code to. 



Test
---

The test suit will build its own python version using the makefile. 

Building the development python virtualenv requires that you have(Fedora/Centos/Redhat): 
###

    yum -y install npm gcc sqlite-devel openssl-devel libtiff-devel openjpeg-devel \
    openjpeg2-devel libjpeg-turbo-devel  zlib-devel  freetype-devel lcms-devel \
    lcms2-devel libexif-devel libffi-devel



    make test

You can also test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test
