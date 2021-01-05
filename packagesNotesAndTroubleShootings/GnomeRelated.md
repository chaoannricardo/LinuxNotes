# Gnome Related



**GNOME** installation inside Ubuntu.

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

**Mac-alike theme (Mojave)** (https://github.com/vinceliuice/Mojave-gtk-theme)