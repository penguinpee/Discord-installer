build:
	@echo 'Nothing to build'

install:
	mkdir -p ${DESTDIR}/$(shell rpm --eval='%{_unitdir}')
	mkdir -p ${DESTDIR}/$(shell rpm --eval='%{_libexecdir}')/discord-installer
	mkdir -p ${DESTDIR}/$(shell rpm --eval='%{_datadir}')/discord-installer
	install -m 644 discord-installer.{service,timer} ${DESTDIR}/$(shell rpm --eval='%{_unitdir}')
	install -m 644 discord-canary-installer.{service,timer} ${DESTDIR}/$(shell rpm --eval='%{_unitdir}')
	install -m 755 build.sh ${DESTDIR}/$(shell rpm --eval='%{_libexecdir}')/discord-installer
	mv -v template.specfile template.spec
	install -m 644 template.spec ${DESTDIR}/$(shell rpm --eval='%{_datadir}')/discord-installer

clean:
	rm -rf ${DESTDIR}/*

.PHONY: build install clean
