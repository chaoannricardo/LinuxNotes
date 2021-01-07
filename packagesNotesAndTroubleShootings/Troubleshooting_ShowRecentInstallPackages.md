https://askubuntu.com/questions/17012/is-it-possible-to-get-a-list-of-most-recently-installed-packages

Command to list recently installed packages that were installed via any method (`apt-get`, Software Center et al.):

```
grep " install " /var/log/dpkg.log
```

**Example output:**

```
2010-12-08 15:48:14 install python-testtools <none> 0.9.2-1
2010-12-08 15:48:16 install quickly-widgets <none> 10.09
2010-12-08 22:21:31 install libobasis3.3-sdk <none> 3.3.0-17
2010-12-09 12:00:24 install mc <none> 3:4.7.0.6-1
2010-12-09 23:32:06 install oggconvert <none> 0.3.3-1ubuntu1
2010-12-09 23:34:50 install mpg123 <none> 1.12.1-3ubuntu1
2010-12-09 23:34:52 install dir2ogg <none> 0.11.8-1
2010-12-09 23:34:53 install faad <none> 2.7-4
2010-12-09 23:34:54 install wavpack <none> 4.60.1-1
2010-12-10 11:53:00 install playonlinux <none> 3.8.6
```

------

You could run this command to list only the recently installed package names,

```
awk '$3~/^install$/ {print $4;}' /var/log/dpkg.log
```

Command to list history of `apt-get` (NOTE: this doesn't list dependencies installed, it simply lists previous `apt-get` commands that were run):

```
grep " install " /var/log/apt/history.log
```

**Example output:**

```
Commandline: apt-get install libindicate-doc
Commandline: apt-get install googlecl
Commandline: apt-get --reinstall install ttf-mscorefonts-installer
Commandline: apt-get install valac libvala-0.10-dev
Commandline: apt-get install libgtksourceview-dev
Commandline: apt-get install python-sphinx
Commandline: apt-get install python-epydoc
Commandline: apt-get install quickly-widgets
Commandline: apt-get install libreoffice3* libobasis3.3*
Commandline: apt-get install mc
```