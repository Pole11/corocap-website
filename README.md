> If you have any issues then open an issue on the GitHub repo (if you have access to it) or write to the maintainer: riccardo.polelli02@gmail.com

# Website Generator for CAP

## Setup build environment

First of all install Python, this depends on your OS, please refer to official documentation. The guide suppose you are running Linux and you have basic understanding of the command line.

Run the `dependency.sh` script. 

```
$ chmod +x ./dependency.sh # make it executable
$ ./dependency.sh # execute it
```

As for every other file, you are invited to look at the content of this file but the only thing it does is to install the python virtual environment and the necessary package with `pip`.

The next step is to build the website.

```
$ chmod +x ./build.sh # make it executable
$ ./build.sh # execute it
```

The result will be inside the `build` folder. You can then use the *Live Server* extension for VSCode (ritwickdey.LiveServer). Other methods are currently being tested to avoid using such extension.

That's it.

## How the website works

It will create files inside the `build` folder. Those files will be the html cousins of the files inside `content` folder files. Those files **must** be written in markdown syntax. They will then be converted to html thanks to a library.

The final html file will be composed of also the files inside the `static` folder. Inside this folder there is the content common to all files. We can have up to 100 (from 0 to 99, those are hardcoded values) files inside this folder. They are ordered so that they are inserted inside the final html file in such order. The actual content (the one converted from markdown to html) is always placed at position 50 (hardcoded value).

Since I suck at explaining stuff, here is a visual representation:

- 00 is topbar (inside the `static` folder)
- ...
- 50 is **content** (inside the `content` folder, it is the one converted from markdown to html)
- ...
- 99 is footer (inside the `static` folder)

Note that everything is deleted everytime you run `build`. Only the name of the dirs inside the `BUILD_PERSISTENT_DIRS` list are not deleted.

## How to add something

### Article

### Images

