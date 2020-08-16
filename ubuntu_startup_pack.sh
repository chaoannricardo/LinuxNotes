#!/bin/bash

# Pre-executed Procedure
# * sudo apt-get update
# * sudo apt-get upgrade
# * uname -r
# * sudo apt-get install linux-headers-<kernal version>
# * sudo apt-get install open-vm-tools
# * sudo apt-get install open-vm-tools-desktop
# * reboot

# Shell Script Starts
echo "=========================================================================
=========================================================================
=========================================================================
Welcome to Ricardo's Ubuntu Start-up Package!!!
Maintainer: Ricardo S. Chao;
https://github.com/chaoannricardo;https://www.linkedin.com/in/chaoannricardo/
Last Updated: 2020/08/09"
sleep 3
echo "=========================================================================
=========================================================================
=========================================================================
Copyright [2020] [Ricardo S. Chao]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=========================================================================
=========================================================================
=========================================================================
Installation Starts======================================================

"
sleep 5

echo 'Installing foundamental packages...'

# update repository, upgrade packages for the first time
sudo apt-get update
# installing essential packages, including openssh-sever
sudo apt-get install openssh-server -y
sudo apt-get install dkms -y
sudo apt-get install build-essential -y
sudo apt-get install open-vm-tools open-vm-tools-desktop -y

echo 'Installing other packages, in alphabetical order..'

# install bleachbit (Disk cleaner for Ubuntu)
# official site: https://www.bleachbit.org/
sudo apt-get install bleachbit -y
# install boomaga (fineprint of linux)

# git service initialize
sudo apt-get install git git-core git-gui git-doc git-svn git-cvs gitweb gitk git-email git-daemon-run git-el
echo "git service installed, however, further configuraion of your own git profile is still needed."
# install gparted (Disk Management Service in linux)
# Official Site: https://gparted.org/
# To activate the package: sudo gparted
sudo apt-get install gparted
# install htop (advanced monitoring service, replacing 'top')
sudo apt-get install htop
# install Java jdk8
sudo apt install openjdk-8-jdk -y
# install snap (advanced package management service in linux)
# Official Documentation: https://snapcraft.io/docs/installing-snap-on-ubuntu
sudo apt install snapd
# install pip3
sudo apt-get install python3-pip -y
# install Typora (https://support.typora.io/Typora-on-Linux/)
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
sudo apt-get install typora -y
# Install zsh, powerline and the font style, and configuration files of zsh
# official site: https://ohmyz.sh/
sudo apt-get install zsh -y
sudo apt-get install powerline fonts-powerline -y
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s /bin/zsh

echo "Stable version of Notepadqq in ubuntu has not been released yet, please refer to its official site for further information."

# Installation ended
echo "
=========================================================================
=========================================================================
=========================================================================
Reminder List of Addtional Packages======================================
*  Anaconda (Common Python Packages)
*  Apache-Spark
*  Apache-Hadoop
*  Apache-Kafka
*  Arduino (Arduino Editor)
*  IntelliJ (Java Editor)
*  Notepadqq (Notepad++ like editor in linux) (Official Site: https://notepadqq.com/wp/download/)
*  Playonlinux (Official Site: https://www.playonlinux.com/en/download.html)
*  Pycharm (Python Editor)
*  Scala (Spark Languange)
*  Sublime Text
*  Wine
Reminder List Ended======================================================
Packages Installed Successfully==========================================
=========================================================================
=========================================================================
========================================================================="

sleep 5