#setup file
#Jack Dauphars

echo 'Installing python related packages'
#python packages
#pip3 is needed first:
sudo apt install python3=3.5.3-1
sudo apt install python3-pip

#pillow for image manipulation:
pip3 install pillow==5.1.0

#pyvirtualdisplay to let us use a bigger display than we have, to take screenshots:
pip3 install EasyProcess==0.2.3
pip3 install pyvirtualdisplay==0.2.1

#selenium to let us use webdriver
pip3 install selenium==3.11.0

echo 'installing file transfer packages'
#regular packages
#cifs to mount the samba server
sudo apt install cifs-utils=2:6.7-1

#rsync to copy to samba server
sudo apt install rsync=3.1.2-1+deb9u1

#crontab to set hourly task to run the script
sudo apt install cron=3.0pl1-128+deb9u1

#geckodriver for headless firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
sudo tar -xvzf geckodriver-v0.18.0-linux64.tar.gz geckodriver
sudo chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
sudo rm geckodriver-v0.18.0-linux64.tar.gz

echo 'ALL PACKAGES INSTALLED'
echo 'SETUP COMPLETE'

