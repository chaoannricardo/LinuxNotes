# Shell Script

This is a repository mainly consists of codes related to packaged installation and other configuration. The script is mainly tested under Ubuntu environment, inside VMware of Windows 10 system.

* [Ubuntu Start-up Package](#ubuntu-startup-package)

* [Other Install Commands](#other-install-commands)
* [Troubleshooting](#troubleshooting)

<br>

# Ubuntu Startup Package

<br>

# Other Install Commands

* **GNOME** installation inside Ubuntu.

It may require user to restart the system after installing the service. Within the GNOME Set-Up process, user would be able to select customized display manager, gdm3 or lightDM. (By using tab to change option, and press enter to select.) Gdm3 is the default Gnome 3 desktop environment greeter.  LightDM is a lighter and faster version of the same greeter system.

```Shell
sudo apt-get update
sudo apt-get install gnome-shell ubuntu-gnome-desktop -y
sudo apt install gnome-tweak-tool -y
```
* **PCMAN** installation inside Ubuntu.

```shell
sudo apt-get update
sudo apt-get install pcmanx-gtk2 -y
```

* **ZSH** installation inside Ubuntu.
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

<br>

# Trouble Shooting

* **Window resize issue of ubuntu-VMware system**

```shell
sudo vim /lib/systemd/system/open-vm-tools.service
```

​	Add under [Unit] with the following line:

```
After=display-manager.service
```

​	For further reference, please check https://communities.vmware.com/thread/576221