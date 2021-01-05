# Linux Laptop Overheat Issue Solution

# Reference

* https://itsfoss.com/reduce-overheating-laptops-linux/
* http://www.emreciftci.net/2011/07/ubuntu-and-high-cpu-temperature.html
* http://www.webupd8.org/2014/04/prevent-your-laptop-from-overheating.html

<br>

# Intel Plate

**Reference:** http://www.webupd8.org/2014/04/prevent-your-laptop-from-overheating.html

[intel_pstate](https://www.kernel.org/doc/Documentation/cpu-freq/intel-pstate.txt) is a new power scaling driver for modern Intel CPUs (it supports Intel SandyBridge+ processors). According to Arjan van de Ven from Intel (for more info, see the comments he posted [HERE](https://plus.google.com/+TheodoreTso/posts/2vEekAsG2QT)), *ondemand* shouldn't be used any more and instead, modern Intel processors should use Intel P-state.



```shell
# edit grub file
sudo vim /etc/default/grub

# add following clause within under config
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_pstate=enable"

# after editing grub file, update the setting and reboot
sudo update-grub
reboot
```



After restarting the system, insert following command to see whether **intel_pstate** is enabled.

```shell
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_driver
# the command should return "intel_pstate"

# or by using following command
cpupower frequency-info

# The output should be something as follows:

# analyzing CPU 0:
#   driver: intel_pstate
#   CPUs which run at the same hardware frequency: 0
#   CPUs which need to have their frequency coordinated by software: 0
#   maximum transition latency: 0.97 ms.
#   hardware limits: 800 MHz - 3.10 GHz
#   available cpufreq governors: performance, powersave
#   current policy: frequency should be within 800 MHz and 3.10 GHz.
#                   The governor "performance" may decide which speed to use
#                   within this range.
#   boost state support:
#     Supported: yes
#     Active: yes
#     25500 MHz max turbo 4 active cores
#     25500 MHz max turbo 3 active cores
#     25500 MHz max turbo 2 active cores
#     25500 MHz max turbo 1 active cores
```



To be able to use the "cpupower" commands below, you'll need to install "linux-tools-common" and "linux-tools-generic":

```shell
sudo apt-get update
sudo apt-get install linux-tools-common linux-tools-generic
```



**- use the "powersave" intel_pstate cpufreq governor:**

```shell
sudo cpupower frequency-set -g powersave
```



**- use the "performance" cpufreq intel_pstate governor:**

```shell
sudo cpupower frequency-set -g performance
```



You can see the currently active cpufreq governor by using the following command:

```shell
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```



**If you want to make the "powersave" governor default in Ubuntu** (using the commands above commands, the settings are lost after a reboot), firstly install cpufrequtils:

```shell
sudo apt-get install cpufrequtils
```



And then edit the */etc/init.d/cpufrequtils* file and change *GOVERNOR* to "powersave" (GOVERNOR="powersave"). You can do this automatically by using the following command:

```shell
sudo sed -i 's/^GOVERNOR=.*/GOVERNOR="powersave"/' /etc/init.d/cpufrequtils
```



**To revert this change and set the governor back to default** (which is "ondemand" and that's not available for Intel P-State, but I'm adding this info in case you don't want to use Intel P-State any more), use the command below:

```shell
sudo sed -i 's/^GOVERNOR=.*/GOVERNOR="ondemand"/' /etc/init.d/cpufrequtils
```



<br>

# Install thermald

```shell
sudo apt-get install thermald
```

Thermald should then start automatically.



<br>



# lm-sensors

```shell
sudo apt-get install lm-sensors
sensors-detect 
```



<br>



# TLP 

TLP’s a daemon that is pre-configured to reduce overheating as well as improve battery life.



To install TLP:

```shell
sudo add-apt-repository ppa:linrunner/tlp
sudo apt-get update
sudo apt-get install tlp tlp-rdw
```

Additional step for ThinkPad:

```shell
sudo apt-get install tp-smapi-dkms acpi-call-dkms
```

To remove TLP:

```shell
sudo apt-get remove tlp
sudo add-apt-repository --remove ppa:linrunner/tlp
```



<br>



# CPUfreq

With CPUfreq, you can choose the mode you want the laptop to run in. 

```shell
sudo apt-get install indicator-cpufreq
```

