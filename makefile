pkurunner-target.apk: pkurunner-target
	./apktool empty-framework-dir
	./apktool b pkurunner-target -o pkurunner-target.apk
	@echo "====================================="
	@echo "built pkurunner-target.apk"
	@echo "if you want to get a signed apk, you must execute 'make sign'."
	@echo "if you do not know the password for keystore, you can execute 'make tmp.keystore'."

pkurunner-target: pkurunner-latest
	cp -r pkurunner-latest pkurunner-target
	cd pkurunner-target && patch -p1 < ../pkurunner.patch
	rm -fr pkurunner-target/build

pkurunner-latest: pkurunner-latest.apk
	./apktool d pkurunner-latest.apk -o pkurunner-latest

pkurunner-latest.apk:
	rm pkurunner-latest.apk* -rf
	wget https://pkunewyouth.pku.edu.cn/public/apks/pkurunner-latest.apk

patch: pkurunner-latest pkurunner-target
	rm -fr pkurunner-target/build
	diff -Nuar pkurunner-latest/ pkurunner-target/ > pkurunner.patch

.PHONY : sign
sign:
	@echo "if tmp.keystore does not exist, execute 'make tmp.keystore' to get it."
	jarsigner -keystore tmp.keystore -signedjar pkurunner-target.apk pkurunner-target.apk tmp.keystore

.PHONY : tmp.keystore
tmp.keystore:
	keytool -genkey -alias tmp.keystore -keyalg RSA -validity 20000 -keystore tmp.keystore

.PHONY : clean
clean:
	rm -fr pkurunner-latest.apk pkurunner-latest pkurunner-target pkurunner-target.apk

.PHONY : clear
clear:
	rm -fr pkurunner-latest pkurunner-target

.PHONY : latest
latest : pkurunner-latest.apk

.PHONY : backup
backup:
	rm -fr apps/ apps.tar apps.list apps.ab
	adb backup -nosystem -noapk -f apps.ab cn.edu.pku.pkurunner
	java -jar ./abe.jar unpack apps.ab apps.tar
	tar tf apps.tar | grep -F "cn.edu.pku.pkurunner" | grep -v "wal" | grep -v "shm" > apps.list
	tar xf apps.tar

.PHONY : restore
restore:
	rm -fr apps2.tar apps2.ab
	tar cf apps2.tar -T apps.list
	java -jar ./abe.jar pack apps2.tar apps2.ab
	adb restore apps2.ab

.PHONY : check
check:
	@echo "WARNING: Will Reinstall cn.edu.pku.pkurunner. Backup first."
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]

.PHONY : purge
purge: check
	adb uninstall cn.edu.pku.pkurunner
	adb install pkurunner-latest.apk