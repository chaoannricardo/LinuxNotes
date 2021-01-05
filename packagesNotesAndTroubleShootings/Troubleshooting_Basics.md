# Troubleshooting Basics

* **Ubuntu File manager missing (20.04)**

Reinstall nautilus

* **Ubuntu desktop** 

sudo apt install gnome-shell-extension-desktop-icons

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

	Add under [Unit] with the following line:

```
After=display-manager.service
```

	For further reference, please check https://communities.vmware.com/thread/576221

<br>