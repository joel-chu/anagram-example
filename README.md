# Anagram example

> A few examples of anagram guessing program, using several different computer languages.
It's quite a good example to show the different between languages.

In here, you will learn quite few things:

- File access
- JSON
- Recursion ([1](./doc/changelog.md) [2](./doc/python-recursion-error.md))
- Threads
- Process (node.js)
- (List) Array operation
- Type converting (For strict type languages)
- Comprehension (Python)
- Math operation
- [Algorithm](./doc/algorithm.md)
- SQL (using sqlite) _coming soon_

And a few bits here and there.

This was developed on [Pop!_OS (Ubuntu 20.10)](https://pop.system76.com/)
and [Deepin 20.x (Debian 10)](https://www.deepin.org)

## Examples

They all are a command line program, with one liner to execute in the following format:

```sh
$ [lang-ex] [path/to/script] [input]
```

---

## Javascript (node.js)

No dependencies, just need node.js installed (>= 12.x)

Run it like so:

```sh
$ node ./js/anagram.js abort
```

There is also another version call `main.js`. First you need to make the file execuatable:

```sh
$ chmod u+x js/main.js
```

Then just run it like this:

```sh
$ js/main.js
```

---

For developers using Deepin 20.x system, you might want to take a look at this [note about setting up node.js](./doc/deepin-20.md) on your system.

Also, I have written a [development change log](./doc/changelog.md) to explain more in depth about the why and how.  

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

### RecursionError

If you have tried the V.1 of the python version, whenever you provide a 5 or more letters word,
You might run into the **RecursionError**.

You can [read this note](./doc/python-recursion-error.md) about how we fix the **RecursionError: maximum recursion depth exceeded in comparison**

## Java (in the folder call javalang / javalangV2)

**Due to the <abbr title="Pain in your a**">PIA</abbr> nature of Java. You need to install [org.json.simple](https://code.google.com/archive/p/json-simple/) to your `CLASSPATH` before you can do anything with this code.**

Or you can download the source then use `ant` to build it. Put the `org` folder (not the `classes`, one level down) into the `/java` folder. Then it should work (Given that you haven't setup your `CLASSPATH`, it will be just `.`)

```sh
$ cd javalang
$ java Anagram abort
```

Should give you a result.

### Notes about why `javalang` not just `java`

Basically I ran into this error:

```
Exception in thread "main" java.lang.SecurityException: Prohibited package name: java
```

Because I tried this:

```
$ java java/Test
```

And `java` thinks the package name is `java.Test`, and of course, it didn't like it. Also it doesn't really matter what you name your folder.
If you try to execute the program from outside the folder, java will think you are calling a `Package`, and it will fail. Therefore, you must `cd` into that directory before you can do anything.

### Java (lang) V.2

Version 2 is written in a observable pattern using Threads. You can see the structure is very different, and
in fact, closer to what a real world application looks like.

## PHP

It was develop using the latest PHP 8.x. You might have to install / upgrade first.
You can [read this note](./doc/php-installation.md) about what we have tried and tested.

To run the onliner version:

```php
$ php php/anagram.php abort
```

If you want to run the interactive version then you first you need to do:

```php
$ chmod u+x php/main.php
$ php/main.php
```

Then you should see the prompt.

### NOTES ON PHP8 PERFORMANCE

Didn't encounter any stack overflow problem, unlike Java, Javacript (node.js) and Python. And the PHP version
add couple extra counter to show how many tries was happening. Sometime the random string
generator (guessing a word) could calculate up to million times, but still only took a few mil second.
That's really some performance improvement.

__@TODO PHP 8 version__

---

## Kotlin

Coming soon

## Deno (Typescript)

Coming soon 

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
