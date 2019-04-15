#!/bin/bash

# QGIST WORK BENCH
# QGis 3.6 Icon Theme
# https://github.com/qgist/theme
#
#     apply_theme.sh: Build a QGis source tarball with new icons
#
#     Copyright (C) 2017-2019 QGIST project <info@qgist.org>
#
# <LICENSE_BLOCK>
# The contents of this file are subject to the GNU General Public License
# Version 2 ("GPL" or "License"). You may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# https://github.com/qgist/theme/blob/master/LICENSE
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
# specific language governing rights and limitations under the License.
# </LICENSE_BLOCK>

version=3.6.1

mkdir -p .tmp
if [ ! -f .tmp/qgis-$version.tar.bz2 ]; then
    wget -P .tmp/ https://qgis.org/downloads/qgis-$version.tar.bz2
fi

mkdir -p .tmp/unpacked
touch .tmp/unpacked/empty
rm -r .tmp/unpacked/*
tar -C .tmp/unpacked -xjf .tmp/qgis-$version.tar.bz2

python3 _helper.py $version

touch qgis-$version-themed.tar.bz2
touch qgis-$version-themed.tar.bz2.md5
rm qgis-$version-themed.tar.bz2
rm qgis-$version-themed.tar.bz2.md5

tar -C .tmp/unpacked/ -cjf qgis-$version-themed.tar.bz2 qgis-$version
md5sum qgis-$version-themed.tar.bz2 > qgis-$version-themed.tar.bz2.md5
