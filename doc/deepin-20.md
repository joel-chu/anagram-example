# A few things about setting things up on Deepin 20.x (Debian 10)

## Node.js 

Basically, the method describe on nodejs.org are useless, because they rely on the `lsb_release` 
to show the version name of the system; that's for checking if they support that OS or not.

In Deepin, when you run the `lsb_release` it just return `n/a`. Apparently that's useless.

And here is how you can install the latest vesrion of node.js on your Deepin system.

```
$ sudo su - 
```

Run yourself as root. Next add the PGP key;
Otherwise when you run `apt update` will throw unable to confirm PGP key error.

```
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1655A0AB68576280
```

You should able to see this PGP key is from nodesource.com  
Now add node source to your source.list file.

```
$ echo "deb https://deb.nodesource.com/node_15.x buster main" | tee -a /etc/apt/sources.list.d/nodesource.list
$ echo "deb-src https://deb.nodesource.com/node_15.x buster main" | tee -a /etc/apt/sources.list.d/nodesource.list
```

And lastly run update then install 

```
$ apt update && apt install nodejs -y 
```

Check what version of node you got 

```
$ node -v 
```

Mine show the following:

```
$ v15.12.0
```

---

March 2021s

