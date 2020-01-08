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
Last Updated: 2020/01/06"
sleep 3
echo "=========================================================================
=========================================================================
=========================================================================
Copyright [2019] [Ricardo S. Chao]

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

# update repository, upgrade packages for the first time
sudo apt-get update

# install open-ssh-server and client other essential packages
sudo apt-get install openssh-server -y
sudo apt-get install dkms -y
sudo apt-get install build-essential -y
sudo apt-get install open-vm-tools open-vm-tools-desktop -y

# install Java jdk8
sudo apt install openjdk-8-jdk -y

# install pip3, numpy, pandas, scikit-learn
sudo apt-get install python3-pip -y
pip3 install numpy
pip3 install pandas
pip3 install scikit-learn
pip3 install matplotlib

# install Typora (https://support.typora.io/Typora-on-Linux/)
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
sudo apt-get install typora -y

# install notepadqq(https://notepadqq.com/wp/download/)
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq

# install bleachbit(CCleaner for Ubuntu)
sudo apt-get install bleachbit -y

sleep 5

# Create Installation log
echo " # Pre-executed Procedure
* sudo apt-get update
* sudo apt-get upgrade
* uname -r 
* sudo apt-get install linux-headers-<kernal version>
* sudo apt-get install open-vm-tools
* sudo apt-get install open-vm-tools-desktop
* reboot


# Packages Installed:
* open-vm-tools
* openssh-server
* dkms
* build-essential
* openjdk-8-jdk
* python3-pip
* numpy
* pandas
* scikit-learn
* matplotlib
* typora
* notepadqq
* bleachbit
" > ~/RicardoInstallationLog.md

# Installation ended, create reminder list
echo "=========================================================================
=========================================================================
=========================================================================
Reminder List of Addtional Packages======================================
*  Anaconda (Common Python Packages)
*  IntelliJ (Java Editor)
*  Scala (Spark Languange)
*  Pycharm (Python Editor)
*  Arduino (Arduino Editor)
*  Apache-Spark
*  Apache-Hadoop
*  Apache-Kafka
*  idle-python3.6
Reminder List Ended======================================================
Packages Installed Successfully==========================================
=========================================================================
=========================================================================
========================================================================="

echo "
# Other Guide

## To change the environment variable of Ubuntu (Julia for instance)
* sudo nano /etc/profile
* [Add following lines]
    export JULIA_HOME="/home/user/julia-1.2.0"
    export PATH=$JULIA_HOME/bin:$PATH
* source /etc/profile [or log out and log in again to aactivate the changes]

" > ~/RicardoOtherGuide.md


