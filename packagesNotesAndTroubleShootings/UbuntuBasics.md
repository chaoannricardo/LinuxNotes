# Ubuntu Basics

# Environment variable setup

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

# Revise Hostname

```shell
sudo nano /etc/hostname
sudo nano /etc/hosts
reboot
```

