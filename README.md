# Shell Script

This is a repository mainly consists of codes related to packaged installation and other configuration. The script is mainly tested under Ubuntu environment, inside VMware of Windows 10 system.

* [Ubuntu Start-up Package](#ubuntu-startup-package)


<br>

# Ubuntu Startup Package

The script aims to accomplish basic packages set-up for users, and to make the environment more friendly to new users of ubuntu Linux environment. 

To clone the repository to your system, you may have to first activate git service on your system, as well as several install some required packages.

```shell
# update repository list, and upgrade
sudo apt-get update
sudo apt-get upgrade
# to install git service
sudo apt-get install git git-core git-gui git-doc git-svn git-cvs gitweb gitk git-email git-daemon-run git-el
# Pre-executed Procedure
uname -r
sudo apt-get install linux-headers-<kernal version>
reboot
```
After that,  clone this repository by typing following command:

```shell
# to clone the repository
git clone https://github.com/chaoannricardo/LinuxNotes.git
```

Finally, you could finish the remain set-ups by activating the script:

```shell
./ubuntu_startup_pack.sh
```