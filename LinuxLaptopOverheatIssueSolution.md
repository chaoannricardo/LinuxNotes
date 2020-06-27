# Linux Laptop Overheat Issue Solution

# Reference

* https://itsfoss.com/reduce-overheating-laptops-linux/
* http://www.emreciftci.net/2011/07/ubuntu-and-high-cpu-temperature.html



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

