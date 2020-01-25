# Ubuntu PPPOE & Static IP Setup

**1. Static IP Setup**

```shell
sudo vim /etc/network/interfaces
```

Edit configuration file with **static ip, netmask, gateway, and dns-nameserver**

If you are not sure the name of  your network interface card, type "ip addr show" to get the information.

```shell
# interfaces(5) file used by ifup(8) and ifdown(8)
auto lo
iface lo inet loopback

# The primary network interfaces
auto enp1s0
iface enp1s0 inet static
address 220.135.181.17
netmask 255.255.255.0
gateway 220.135.181.254
dns-nameserver 168.95.1.1,168.95.192.1,168.95.192.2
```

<br>

**2. Restart internet service**

```shell
sudo /etc/init.d/networking restart
```

<br>

**3. Configure PPPOE setting**

To set up PPPOE service within your computer, be sure that the computer is connected to your PPPOE concentrator (modem).

```shell
# Complete the setting within the following command:
sudo pppoeconf
```

<br>

**4. Restart internet service**

```shell
sudo /etc/init.d/networking restart
```

