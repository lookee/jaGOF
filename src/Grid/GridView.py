
#------------------------------------------------------------------------
#    Copyright (C) 2011 Luca Amore <luca.amore at gmail.com>
#
#    jaGOF is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jaGOF is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with jaGOF.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------

import pygame
from pygame.locals import *
from sys import exit

class GridView(object):

    def __init__(self, sizex=64, sizey=48, width=640, heigth=480):
        self.sizex = sizex
        self.sizey = sizey
        self.width = width 
        self.heigth = heigth
        self.caption = "John Conway's Game of Life [%dx%d]" % (sizex, sizey)

        self.bgColor    = (255,     255,    255)
        self.lineColor  = (150,     150,    150)
        self.boxColor   = (  0,       0,      0)

        self.stepx = self.width / self.sizex
        self.stepy = self.heigth / self.sizey

        self.marginx = (self.width % self.sizex) / 2
        self.marginy = (self.heigth % self.sizey) / 2
       
        self.__init_screen()
        self.__init_grid()
        self.update()        


    def __init_screen(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width,self.heigth), 0, 32)
        pygame.display.set_caption(self.caption)

        self.screen.fill(self.bgColor)

    def __init_grid(self):
        
        screen = self.screen

        for n in range(0,self.sizex + 1):

            # grid: vertical lines
	        start = (self.stepx * n + self.marginx, 0 + self.marginy)
	        end   = (self.stepx * n + self.marginx, self.sizey * self.stepy + self.marginy)
	        pygame.draw.lines(screen, self.lineColor, False, [start, end], 1)

        for n in range(0,self.sizey + 1):

            # grid: horizontal lines
	        start = (0 + self.marginx, self.stepy * n + self.marginy)
	        end   = (self.sizex * self.stepx + self.marginx, self.stepy * n + self.marginy)
	        pygame.draw.lines(screen, self.lineColor, False, [start, end], 1)

    def update(self):
        pygame.display.update()

    def fillBox(self, bx, by, color):
        rect = Rect(self.stepx * bx + 2 + self.marginx, self.stepy * by + 2 + self.marginy, self.stepx - 3, self.stepy - 3)
        self.screen.fill(color,rect)

    def setBox(self, bx, by):
        self.fillBox(bx, by, self.boxColor)

    def unsetBox(self, bx, by):
        self.fillBox(bx, by, self.bgColor)

    def setPoint(self, x, y):
        (bx, by) = self.point2Box(x, y)
        self.setBox(bx,by)

    def unsetPoint(self, x, y):
        (bx, by) = self.point2Box(x, y)
        self.unsetBox(bx,by)
    
    def point2Box(self, x, y):
        bx = (x - self.marginx) / self.stepx
        by = (y - self.marginy) / self.stepy
        return (bx, by)

