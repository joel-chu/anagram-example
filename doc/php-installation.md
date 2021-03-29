# PHP Ubuntu / Debian Installation note 

### For Ubuntu

```sh
$ sudo add-apt-repository ppa:ondrej/php
$ sudo apt-get update
```

### For Debian

```sh
$ sudo apt install apt-transport-https lsb-release ca-certificates wget -y
$ sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
$ sudo sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list'
$ sudo apt update
```
For those using Deepin system, the `$(lsb_release -sc)` will return empty and make it not working.
So you need to this instead (Assume your are running the latest Deepin 20 system)

```shell script
$ sudo sh -c 'echo "deb https://packages.sury.org/php/ buster main" > /etc/apt/sources.list.d/php.list'
```

Then both system are the same:

```shell script
$ sudo apt install php8.0-common php8.0-cli -y
$ php -v
$ php -m
```

