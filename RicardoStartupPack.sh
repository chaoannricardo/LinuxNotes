#!/bin/bash
# Pre-executed Procedure
# * sudo apt-get update
# * sudo apt-get upgrade
# * uname -r 
# * sudo apt-get install linux-headers-<kernal version>

# Shell Script Starts
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
echo "Welcome to Ricardo's Ubuntu Start-up Package!!!"
echo "Maintainer: Ricardo S. Chao;"
echo "https://github.com/chaoannricardo;https://www.linkedin.com/in/chaoannricardo/"
echo "Last Updated: 2019/09/20"
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
echo "Copyright [2019] [Evil Corp]"
echo ""
echo "Licensed under the Apache License, Version 2.0 (the "License");"
echo "you may not use this file except in compliance with the License."
echo "You may obtain a copy of the License at"
echo ""
echo "   http://www.apache.org/licenses/LICENSE-2.0"
echo ""
echo "Unless required by applicable law or agreed to in writing, software"
echo "distributed under the License is distributed on an "AS IS" BASIS,"
echo "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied."
echo "See the License for the specific language governing permissions and"
echo "limitations under the License."
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
echo "Installation Starts======================================================"
echo ""
echo ""
echo ""
sleep 3

# update repository, upgrade packages for the first time
sudo apt-get update

# install open-ssh-server and client other essential packages
sudo apt-get install openssh-server -y
sudo apt-get install dkms -y
sudo apt-get install build-essential -y

# install Java jdk8
sudo apt install openjdk-8-jdk -y

# install pip3, numpy, pandas, scikit-learn
sudo apt-get install python3-pip -y
pip3 install numpy
pip3 install pandas
pip3 install scikit-learn
pip3 install matplotlib

# install git service
sudo apt-get install git -y
sudo apt-get install git-core -y
sudo apt-get install git-gui -y
sudo apt-get install git-doc -y
sudo apt-get install git-svn -y
sudo apt-get install git-cvs -y
sudo apt-get install gitweb -y
sudo apt-get install gitk -y
sudo apt-get install git-email -y
sudo apt-get install git-daemon-run -y
sudo apt-get install git-el -y

# Github service setup
ssh -T git@github.com

# install Chinese Pinyin Method
sudo apt-get install ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4 -y
im-config -s ibus
sudo apt-get install ibus-rime -y

# install gtk (In order to install customized themes)
sudo apt-get install libgtk2.0-dev -y
sudo apt-get install libgtk-3-dev -y

# install mojave theme of ubuntu 
sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf -y

# install Typora (https://support.typora.io/Typora-on-Linux/)
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
sudo apt-get install typora -y

# install notepadqq(https://notepadqq.com/wp/download/)
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq

# install GNOME (In order to customized themes of the system)
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
echo "Installing GNOME.....may require user to restart the system after installing the service"
echo "Within the GNOME Set-Up process, user would be able to select customized display manager, gdm3 or lightDM. (By using tab to change option, and press enter to select.)"
echo "Gdm3 is the default Gnome 3 desktop environment greeter. "
echo "LightDM is a lighter and faster version of the same greeter system."
echo "GNOME Installation Starts..."
sleep 5
sudo apt-get install gnome-shell ubuntu-gnome-desktop -y
sudo apt install gnome-tweak-tool -y
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
echo "Reminder List of Addtional Packages======================================"
echo ""
echo "*  Anaconda (Common Python Packages)"
echo "*  IntelliJ (Java Editor)"
echo "*  Scala (Spark Languange)"
echo "*  Pycharm (Python Editor)"
echo "*  Arduino (Arduino Editor)"
echo "*  Apache-Spark"
echo "*  Apache-Hadoop"
echo "*  Apache-Kafka"
echo "*  idle-python3.6"
echo ""
echo "Reminder List Ended======================================================"
echo "Packages Installed Successfully=========================================="
echo "========================================================================="
echo "========================================================================="
echo "========================================================================="
