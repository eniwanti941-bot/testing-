%%writefile buildozer.spec
[app]
title = System Update
package.name = sysupdate
package.domain = com.android.system
source.dir = .
source.include_exts = py,png,jpg,kv,xml
version = 0.1
requirements = python3,kivy,pyjnius,requests,plyer,android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE,SYSTEM_ALERT_WINDOW
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
p4a.branch = master
