#
# Main makefile for DYMOmyte
#

# Installs necessary python packages
macinstall: easy_install
	sudo easy_install pyusb

# Must have easy_install to install on mac
easy_install:
ifeq ($(shell which easy_install),)
	$(error You need to install easy_install https://pypi.python.org/pypi/setuptools)
endif

# Run tests
test:
	python read.py
