#!/bin/bash

# Before Installation
# It is recommended to execute this script inside the directory where GitHun repositories store.
# You are required to activate git service inside your environment before executing the installation script.

# Shell Script Starts
echo "=========================================================================
=========================================================================
=========================================================================
Welcome to Ricardo's Installation Package of zsh!!!
Maintainer: Ricardo S. Chao;
https://github.com/chaoannricardo;https://www.linkedin.com/in/chaoannricardo/
Last Updated: 2020/01/05"
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
sudo apt-get update
# Install zsh
sudo apt-get install zsh -y
# Install powerline and the font style. 
sudo apt-get install powerline fonts-powerline -y
# Set up configuration file of zsh
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s /bin/zsh
