# ZSH Installation

**ZSH** installation inside Ubuntu.

**Official site:** https://ohmyz.sh/

**Before Installation**

* It is recommended to execute this script inside the directory where GitHub repositories store.
* You are required to activate git service inside your environment before executing the installation script.

You would also have to reboot the system after the installation to activate the new settings.

```Shell
sudo apt-get update
# Install zsh
sudo apt-get install zsh -y
# Install powerline and the font style. 
sudo apt-get install powerline fonts-powerline -y
# Set up configuration file of zsh
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s /bin/zsh
```