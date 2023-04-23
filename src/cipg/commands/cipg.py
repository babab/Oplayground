# file: src/cipg/commands/cipg.py

# Copyright (c) 2023 Benjamin Althues <benjamin@babab.nl>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from this
# software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# SPDX-License-Identifier: BSD-3-Clause

import sys

import pycommand

from cipg import versionStr
import cipg.core


def main():
    try:
        cmd = Command(sys.argv[1:])
        if cmd.error:
            print('error: {0}'.format(cmd.error))
            return 1
        else:
            return cmd.run()
    except KeyboardInterrupt:
        print('\ncipg successfully exited.')
        return 0


class Command(pycommand.CommandBase):
    '''Argument handler based on pycommand'''
    usagestr = 'Usage: cipg <options>'
    description = __doc__
    optionList = (
        ('help', ('h', False, 'show this help information')),
        ('version', ('', False, 'show version information')),
    )

    def run(self):
        '''Run from shell; main application program flow.'''

        # Flags that will print and exit
        if self.flags['help']:
            print(self.usage)
            return
        elif self.flags['version']:
            print(versionStr)
            return

        # Regular behaviour
        files = cipg.core.Files.walkdir('.')
        for fn in files:
            print(fn)


if __name__ == '__main__':
    sys.exit(main())
