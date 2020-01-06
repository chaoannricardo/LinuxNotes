# Shell Script

This is a repository mainly consists of codes related to packaged installation and other configuration. The script is mainly tested under Ubuntu environment, inside VMware of Windows 10 system.

* [Ubuntu Start-up Package](#ubuntu-startup-package)

* [Other Package Installation](#other-package-installation)
* [Troubleshooting](#troubleshooting)

<br>

# Ubuntu Startup Package

The script aims to accomplish basic packages set-up for users, and to make the environment more friendly to new users of ubuntu Linux environment. 

The script includes package installation such as,

* **Openssh-server**
* **Dkms**
* **Build-essential**
* **Openjdk-8-jdk**
* **python3-pip**
* **Numpy**
* **Pandas**
* **Scikit-learn**
* **Matplotlib**
* **Typora**
* **Notepadqq**
* **Bleachbit**

<br>

# Other Package Installation
* **Chinese Pinyin method** (ibus) setup

```shell
# install Chinese Pinyin Method
sudo apt-get install ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4 -y
im-config -s ibus
sudo apt-get install ibus-rime -y
```

<br>

* **Git** Installation inside Ubuntu

```shell
# install git service
sudo apt-get install git git-core git-gui git-doc git-svn git-cvs gitweb gitk git-email git-daemon-run git-el
```

<br>

* **GitHub** setup inside Ubuntu.

**SSH key set-up for GitHub**

**Reference:** https://wiki.paparazziuav.org/wiki/Github_manual_for_Ubuntu

**Step 1**

```shell
cd ~/.ssh
```

When the terminal displays: ""bash: cd: ./.ssh:No such file or  directory" you should generate a public/private rsa ket pair, continue  with step 2.  If the terminal changes to ~/.ssh directory, continue with step 3.

**Step 2**

```shell
ssh-keygen -t rsa -C "your_email@youremail.com"
```

After hitting Enter, the terminal will say: 'Generating  public/private rsa ket pair. Enter file in which to save the  key(/Home/ubuntu/.ssh/id_rsa):' please press only enter and the terminal will ask to enter a passphrase. Enter a suitable passphrase which is > 4 characters. If this is done, please continue with step 4.

**Step 3**

(Follow this step only if your terminal changed to "~/.ssh") 
 You  already have some SSH-keys, following commands will backup (in folder  "key_backup") and remove the keys. Type in your terminal: 

```shell
mkdir key_backup
cd id_rsa* key backup
rm id_rsa*
```

**Step 4**

```shell
vim id_rsa.pub
```

Ubuntu will open a file, copy it's entire content:

1.  Open the github site and login.
2.  Go to "Account Settings" (in the upper right corner from your page).
3.  Click: "SSH Keys"
4.  Click: "Add another public key" 
5.  Paste the copied content into the "key field" and press "Add key" 

**Step 5**

```shell
ssh-add
```

**GitHub log-in configuration**

```shell
# Github service setup
ssh -T git@github.com
# GitHub configuration
git config --global user.name "user_name"
git config --global user.email "email_id"
```

<be>

* **GNOME** installation inside Ubuntu.

It may require user to restart the system after installing the service. Within the GNOME Set-Up process, user would be able to select customized display manager, gdm3 or lightDM. (By using tab to change option, and press enter to select.) Gdm3 is the default Gnome 3 desktop environment greeter.  LightDM is a lighter and faster version of the same greeter system.

```Shell
sudo apt-get update
sudo apt-get install gnome-shell ubuntu-gnome-desktop gnome-tweak-tool
```
<br>

* **Gtk** setup (For customized themes installation)

```shell
# install gtk (In order to install customized themes)
sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf -y
```

<br>

* **PCMAN** installation inside Ubuntu.

```shell
sudo apt-get update
sudo apt-get install pcmanx-gtk2 -y
```

<br>

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

* **Environment variable setup** for Ubuntu

```shell
# To change the environment variable of Ubuntu (Julia for instance)
sudo nano /etc/profile
# Add following lines
export JULIA_HOME="/home/user/julia-1.2.0"
export PATH=$JULIA_HOME/bin:$PATH
# source the profile file
source /etc/profile
# or log out and log in again to aactivate the changes
```

<br>

* **Window resize issue of ubuntu-VMware system**

```shell
sudo apt-get update
sudo apt-get install open-vm-tools open-vm-tools-desktop -y
sudo vim /lib/systemd/system/open-vm-tools.service
```

​	Add under [Unit] with the following line:

```
After=display-manager.service
```

​	For further reference, please check https://communities.vmware.com/thread/576221

<br>