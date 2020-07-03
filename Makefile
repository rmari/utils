# load Makefile inputs

makeconfig = config/Makefile_config.mk
gotconfig = 0
ifneq ("$(wildcard $(makeconfig))","")
        include $(makeconfig)
        gotconfig = 1
endif

IPYTHON_DIR = $(shell ipython locate)
PYTHON_SITE_PACKAGES = $(shell env python -c "import site;print(site.getsitepackages()[0])")

install:
	cp dict_utils.py $(PYTHON_SITE_PACKAGES)
	cp ipython_startup.ipy $(IPYTHON_DIR)/profile_default/startup/
	chmod u+x gign
	cp gign $(INSTALL_DIR)
	chmod u+x gremadd
	cp gremadd $(INSTALL_DIR)
