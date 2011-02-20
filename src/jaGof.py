#!/usr/bin/env python

#------------------------------------------------------------------------
#    Copyright (C) 2011 Luca Amore <luca.amore at gmail.com>
#
#    jaGof is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jaGof is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with jaGof.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------

import sys
import ConfigParser

from Life.LifeControl import LifeControl

print """
+------------------------------+
|GOF v. 0.1.0                  |
|John Conway's Game of Life    |
+------------------------------+
|mouse buttons                 | 
+--------------+---------------+
|left to born | right to kill  |
+--------------+---------------+
|keys                          |
+------------------------------+
| e : evolve single generation |
| m : start/stop evolution     |
| + : increase evolution speed |
| - : decrease evolution speed |
| q : quit                     |
+------------------------------+
"""

# read seed file
if len(sys.argv) > 1:
    filename = sys.argv[1]
    print "reading seed: %s" % filename
else:
    filename = None

# read configuration file
config = ConfigParser.ConfigParser()
config.read("jaGof.conf")

# start life
control = LifeControl(config, filename)

exit(0)
