# Anagram example

Just a few example of anagram using several different computer languages.
It's quite a good example to show the different between languages.

This was developed on Pop-os (Ubuntu 20.10).

## Examples

They will all be one liner to execute in the following format

```sh
$ [lang-ex] [path/to/script] [input]
```

## Using Docker file

There are several `Dockerfile-*` on the root level (that's due to when we need to copy the `/share` folder, its outside the build context)
Therefore when you build the docker image, you need to do the following:

(Well, I am using podman ...)

```
$ docker build -f Dockerfile-[name-of-the-lang]
```

---

## Javascript

No dependencies, just need node.js installed (>= 12.x)

Run it from the command line, the first following word will be the input.

```sh
$ node ./js/anagram.js abort
```

## Python

```sh
$ python3 ./python/anagram.py abort
```

If you have `python-is-python3` (on Ubuntu / Debian) then just `python`.

You can also call the other script within the folder, after you make it an executable file:

```sh
$ chmod u+x python/main.py
```

Then you can just call it directly

```sh
$ python/main.py
```

It will ask you for input. 

##  Java

Coming soon.

---

The dictionary is borrow from [basicwords.org](https://anagrams.basicwords.org)

Joel Chu (c) 2021
