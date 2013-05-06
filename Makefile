PREFIX = /usr
DATADIR = $(PREFIX)/share/ssu
CONFDIR = /etc/ssu

CONF = etc/*
DATA = share_ssu/*

all:
	@echo "No build needed"

install:
	@echo "Installing ssu data...";
	mkdir -p $(DESTDIR)$(DATADIR)
	mkdir -p $(DESTDIR)$(CONFDIR)
	cp -r $(CONF) $(DESTDIR)$(CONFDIR)
	cp -r $(DATA) $(DESTDIR)$(DATADIR)

.PHONY: all install
