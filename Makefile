#!/usr/bin/bash
SHELL=bash
PYTHON=/usr/bin/python3

define makezip =

	@echo -n "Making $(1) zip ... "
	@cd "$(1)"; zip "$(1)".zip -qr ./*
	@mv "$(1)/$(1)".zip .
	@echo Done!
endef

all: clean
	@"$(PYTHON)" generator.py

zip: $(wildcard p?) $(wildcard p??)
	$(foreach folder,$(shell ls p? p?? -d 2>/dev/null),$(call makezip,$(folder));)

clean:
	@rm p? p?? -rf 2>/dev/null
	@rm p?.zip p?.zip -f 2>/dev/null
	@rm *~ -f 2>/dev/null
