# Kivy GPS App
this school project was made with vivy, a cross-platform python framework, and was deployed on google play store : https://play.google.com/store/apps/details?id=org.doggofarm.doggofarm 

## venv
- create a virtual env (`python3 -m venv venv`)
- activate virtual env (`. venv/bin/activate`)
- install dependencies (`pip3 install requirements.txt`)

## make a .env file
- API_KEY from hereapi

## to run the app
- `python main.py`

## to test the app on android with buildozer
- i highly rec to use a virtual machine (i used a vm on ubuntu)
- follow the installation steps : https://github.com/kivy/buildozer 
- init buildozer + edit buildozer file (very important)
- make sure your android phone is connected
- run `buildozer android debug deploy run logcat`
