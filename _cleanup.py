#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

QGIST WORK BENCH
QGis 3.6 Icon Theme
https://github.com/qgist/theme

    _cleanup: Cleanup icon svg files for distribution

    Copyright (C) 2017-2019 QGIST project <info@qgist.org>

<LICENSE_BLOCK>
The contents of this file are subject to the GNU General Public License
Version 2 ("GPL" or "License"). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
https://github.com/qgist/theme/blob/master/LICENSE

Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>

"""

import os

ICON_FLD = 'icons'

def main():
    fn_list = os.listdir(ICON_FLD)
    for fn in fn_list:
        with open(os.path.join(ICON_FLD, fn), 'r', encoding = 'utf-8') as f:
            lines = [line for line in f]
        lines[6] = '\t xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"\n'
        with open(os.path.join(ICON_FLD, fn), 'w', encoding = 'utf-8') as f:
            f.write(lines[0])
            f.write(''.join(lines[5:]))

if __name__ == '__main__':
    main()
