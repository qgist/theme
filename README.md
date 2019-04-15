# QGIST icon theme for QGis 3.6

## Synopsis

A first attempt at building a clear, tasteful and simple QGis icon theme, primarily for dark user interface backgrounds. Enjoy!

## Caveats

In their current form, QGis's icons are not supposed to be themed or customized. They are scattered across QGis' source code repository, without any form of coherent naming scheme or pattern or [comprehensive documentation](https://docs.qgis.org/testing/en/docs/documentation_guidelines/substitutions.html#toolbar-button-icons). Icon names as well as the names of corresponding actions randomly change from one version of QGis to the next, therefore **this theme currently only works with QGis 3.6**. Unfortunately, it also means that **applying this theme requires to build QGis from source** - with changed icons.

## Requirements

The method for applying changes to the QGis source tree, which is described below, requires a Bash shell and Python 3. It is tested on Linux and should work on other Unix-like systems just as flawlessly. The produced result, a customized source tarball, can be compiled on any operating system that is supported by QGis, including Windows.

## Install

Clone this git repository and change into the directory:

```bash
git clone https://github.com/qgist/theme.git
cd theme/
```

Now apply the theme:

```bash
./apply_theme.sh
```

The above script will:

- download a source tarball of QGis 3.6.1
- unpack it into a temporary folder below the current working directory
- copy the themed icons to the appropriate locations within the source tree, overwriting the originals
- fix references to svg files which previously were png files
- pack a new source tarball into the current working directory

You will find two new files in the current working directory:

```bash
qgis-3.6.1-themed.tar.bz2
qgis-3.6.1-themed.tar.bz2.md5
```

Now you can use the [build method of your choice](https://raw.githubusercontent.com/qgis/QGIS/master/INSTALL) to compile QGis from the generated source tarball.
