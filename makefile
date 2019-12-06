pkurunner-v1.2.5_res.apk: pkurunner-v1.2.5_res
	./apktool empty-framework-dir
	./apktool b pkurunner-v1.2.5_res -o pkurunner-v1.2.5_res.apk
	@echo "====================================="
	@echo "built pkurunner-v1.2.5_res.apk"
	@echo "if you want to get a signed apk, you must execute 'make sign'."
	@echo "if you do not know the password for keystore, you can execute 'make tmp.keystore'."

pkurunner-v1.2.5_res: pkurunner-v1.2.5_origin
	cp -r pkurunner-v1.2.5_origin pkurunner-v1.2.5_res
	cd pkurunner-v1.2.5_res && patch -p1 < ../pkurunner.patch

pkurunner-v1.2.5_origin: pkurunner-latest.apk
	./apktool d pkurunner-latest.apk -o pkurunner-v1.2.5_origin

pkurunner-latest.apk:
	rm pkurunner-latest.apk* -rf
	wget https://pkunewyouth.pku.edu.cn/public/apks/pkurunner-latest.apk

patch: pkurunner-v1.2.5_origin pkurunner-v1.2.5_res
	diff -Nuar pkurunner-v1.2.5_origin/ pkurunner-v1.2.5_res/ > pkurunner.patch

.PHONY : sign
sign:
	@echo "if tmp.keystore does not exist, execute 'make tmp.keystore' to get it."
	jarsigner -keystore tmp.keystore -signedjar pkurunner-v1.2.5_res.apk pkurunner-v1.2.5_res.apk tmp.keystore

.PHONY : tmp.keystore
tmp.keystore:
	keytool -genkey -alias tmp.keystore -keyalg RSA -validity 20000 -keystore tmp.keystore

.PHONY : clean
clean:
	rm -fr pkurunner-latest.apk pkurunner-v1.2.5_origin pkurunner-v1.2.5_res pkurunner-v1.2.5_res.apk

.PHONY : clear
clear:
	rm -fr pkurunner-v1.2.5_origin pkurunner-v1.2.5_res

