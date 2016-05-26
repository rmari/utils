# load Makefile inputs

makeconfig = config/Makefile_config.mk
gotconfig = 0
ifneq ("$(wildcard $(makeconfig))","")
        include $(makeconfig)
        gotconfig = 1
endif

install:
	cp dict_utils.py $(ANACONDA_DIR)
	chmod u+x gign
	cp gign $(INSTALL_DIR)
	chmod u+x gremadd
	cp gremadd $(INSTALL_DIR)
