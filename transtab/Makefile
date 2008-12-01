TARGETS=transtab transtab.repertoire transtab.missing-MES-2 transtab.changes

all: $(TARGETS)

# transtab.utf is the file that should be edited

transtab: transtab.utf
	format=iso    ./transcomp $< >$@
	format=isoutf ./transcomp transtab >transtab.utf

transtab.repertoire: transtab
	format=utf    ./transcomp transtab >$@

transtab.missing-MES-2: transtab.repertoire
	uniset + ../MES-2 - transtab.repertoire - 0000-007f clean table | \
	format=isoutf ./transcomp - >$@

transtab.missing-TARGET1: transtab.repertoire
	uniset + ../../font/ucs-fonts/TARGET1 - transtab.repertoire \
	- 0000-007f clean table | \
	format=isoutf ./transcomp - >$@

transtab.changes: transtab.utf
	rlog $< >$@

distribution: $(TARGETS)
	ci -l transtab.utf
	cd .. ; tar cvf transtab.tar \
	transtab/README transtab/REFERENCES transtab/Makefile \
	transtab/transcomp \
	transtab/transtab.utf $(TARGETS:%=transtab/%) ; \
	gzip -9f transtab.tar ; \
	mv transtab.tar.gz $(HOME)/.www/download/

clean:
	rm -f *~
