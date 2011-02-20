
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

from Grid.GridModel import GridModel

class LifeModel(GridModel):

    def __init__(self, sizex, sizey):
        super(self.__class__ , self).__init__(sizex, sizey)
        self.epochCounter = 0 

    def epoch(self):
    
        target = [[0 for row in range(self.sizey)] for col in range(self.sizex)]

        for y in range(self.sizey):
            for x in range(self.sizex):

                neighbours = 0

                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):

                        if dy == dx == 0:
                            continue
                        
                        if self.matrix[( x + dx + self.sizex) % self.sizex][( y + dy + self.sizey ) % self.sizey] == 1:
                            neighbours += 1

                if (neighbours == 3) or (neighbours == 2 and self.matrix[x][y] == 1):
                    target[x][y] = 1
                else:                
                    target[x][y] = 0 
 
        self.matrix = target
        self.epochCounter += 1

    def read_seed_file(self, seed_file):
        try:
            file_obj = open(seed_file, 'r')
        except IOError:
            raise IOError("Unable to open file '%s'" % (seed_file))

        seed = [[0 for row in range(self.sizey)] for col in range(self.sizex)]

        xx = 0
        yy = 0

        for line in file_obj:
            # Signals 'comment' line to be skipped
            if line[0] != "!":
                if yy > self.sizey:
                    raise IOError("File height (%d) too large for game " \
                                    "table height (%d)" % (yy, self.sizey))
                xx = 0
                for char in line:
                    if xx > self.sizex:
                        raise IOError("File width (%d) too wide for game" \
                                        "table width (%d)" % (xx, self.sizex))
                    if char == "O":
                        seed[xx][yy] = 1
                    else:
                        seed[xx][yy] = 0 
                    xx += 1
                yy += 1
        
        sx = (self.sizex - xx) / 2
        sy = (self.sizey - yy) / 2

        for y in range(yy):
            for x in range(xx):
                self.matrix[x + sx][y + sy] = seed[x][y]

        print "seed size: %d x %d" % (xx, yy)

    def get_epoch_counter(self):
        return self.epochCounter
