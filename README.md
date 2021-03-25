# Anagram example

Just a few example of anagram using several different computer languages.
It's quite a good example to show the different between languages.

In there, you will learn quite few things:

- File access
- JSON
- Recursion
- (List) Array operation
- Type converting (For strict type languages)
- Comprehension (Python)

And a few bits here and there.

This was developed on [Pop!_OS (Ubuntu 20.10)](https://pop.system76.com/).

## Examples

They all are a command line program, with one liner to execute in the following format:

```sh
$ [lang-ex] [path/to/script] [input]
```

---

## Javascript

No dependencies, just need node.js installed (>= 12.x)

Run it like so:

```sh
$ node ./js/anagram.js abort
```

## Python

Again no dependencies, just need Python 3.x

```sh
$ python3 ./python/anagram.py abort
```

If you have `python-is-python3` (on Ubuntu / Debian) then just `python`.

You can also call the interactive version `main.py` script in the `/python` folder; first you need to make it an executable file:

```sh
$ chmod u+x python/main.py
```

Then you can just call it directly (at least it works on Linux)

```sh
$ python/main.py
```

It will prompt you for input.

##  Java

**Due to the <abbr title="Pain in your a**">PIA</abbr> nature of Java. You need to install [org.json.simple](https://code.google.com/archive/p/json-simple/) to your `CLASSPATH` before you can do anything with this code.**

Or you can download the source then use `ant` to build it. Put the `org` folder (not the `classes`, one level down) into the `/java` folder. Then it should work (Given that you haven't setup your `CLASSPATH`, it will be just `.`)

```sh
$ java Anagram abort
```

Should give you a result.

## PHP

Coming soon

---

## Using Docker file

There are several `Dockerfile-*` on the root level (that's because we need to copy the `/share` folder, its outside the build context)
Therefore when you build the docker image, you need to do the following:

Well, I am using `podman` ...

```
$ docker build -f Dockerfile-[name-of-the-lang]
```

---

## THANK YOU

The dictionary is borrow from [basicwords.org](https://anagrams.basicwords.org).

---

Joel Chu (c) 2021
