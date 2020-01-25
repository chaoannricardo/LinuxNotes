# MySQL Setup Guide of Ubuntu

* [Installation of MySQL](#Installation-of-MySQL)
* [Install ODBC for MySQL](#Install-ODBC-for-MySQL)
* [Uninstallation](#Uninstallation)

<br>

# Installation of MySQL

```shell
# install packages needed
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev

# test whether database is installed successfully
sudo apt-get install net-tools
sudo netstat -tap | grep mysql

# grant remote access of database
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
## comment the following line to enable remote access feature
#bind address              = 127.0.0.1

# check default user and password of MySQL database
sudo vim /etc/mysql/debian.cnf

# log in the database
mysql -u root -p # remember 'root' is the user name
```

To grant remote access from other computers

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' IDENTIFIED BY 'yourpassword' WITH GRANT OPTION;

-- enable new configuration
flush privileges;  
-- exit database
exit
-- restart mysql service
service mysql restart
```

<br>

# Install ODBC for MySQL

Reference: https://medium.com/@joelzhang/install-mysql-odbc-drivers-in-ubuntu-18-04-39241072326a

* Download file from https://dev.mysql.com/downloads/connector/odbc/

  (Do check the version of ODBC connector you've downloaded is in correct version.)

* Extract the file.

* Copy the file to destination.

```shell
sudo cp bin/* /usr/local/bin
sudo cp lib/* /usr/local/lib
sudo chmod 777 /usr/local/lib/libmy*
```

* Install libodbc1 and odbcinst1debian2

```shell
sudo apt-get install libodbc1
sudo apt-get install odbcinst1debian2
```

* Register Unicode driver and ANSI driver

```shell
# Registers the Unicode driver:
sudo myodbc-installer -a -d -n "MySQL ODBC 8.0 Driver" -t "Driver=/usr/local/lib/libmyodbc8w.so"
# Registers the ANSI driver
sudo myodbc-installer -a -d -n "MySQL ODBC 8.0" -t "Driver=/usr/local/lib/libmyodbc8a.so"
```

* Verify that the driver is installed and registered using the ODBC manager, or the myodbc-installer utility: 

```shell
myodbc-installer -d -l
python -c "import pyodbc; conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Driver};SERVER=localhost;DATABASE=sys;UID=ricardo;PWD=anshi840809;')"
```

<br>

# Uninstallation

```Shell
sudo apt-get remove --purge 'mysql*'
sudo apt-get autoremove
sudo rm /etc/init.d/mysql
sudo systemctl daemon-reload 
```

```shell
# test whether mysql database is uninstalled correctly
sudo systemctl start mysql
# Failed to start mysql.service: Unit mysql.service not found.
```

