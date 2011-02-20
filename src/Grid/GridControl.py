
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

import pygame
from pygame.locals import *

from GridView import GridView
from GridModel import GridModel

class GridControl(object):

    def __init__(self, sizex, sizey):

        self.sizex = sizex
        self.sizey = sizey
        self.view = GridView(sizex,sizey,800,480)
        self.model = GridModel(sizex,sizey)

        self.keyPressed = False
        self.action()

    def action(self):

        while True:
 
            self.beforeAction()

            for event in pygame.event.get():
                self.handleEvent(event)

            self.afterAction()
    
    def beforeAction(self):
        pass

    def afterAction(self):
        pass

    def handleEvent(self, event):

        if event.type == QUIT:
            self.triggerEnd()

        if event.type == MOUSEBUTTONDOWN:
            self.handleMouseButtonEvents(event)

        if event.type == KEYUP:
            self.keyPressed = False

        if event.type == KEYDOWN and not self.keyPressed:
            self.keyPressed = True
            self.handleKeyEvents(event)

    def handleKeyEvents(self, event):

        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            self.triggerEnd()

    def triggerEnd(self):
        exit()

    def handleMouseButtonEvents(self, event):

        (x,y) = event.pos
        (bx,by) = self.view.point2Box(x,y)

        if bx in range(self.sizex) and by in range(self.sizey):

            if event.button == 1:
                self.setBox(bx,by)

            elif event.button == 3:
                self.unsetBox(bx,by)

    def renderModel(self):

        for x in range(self.sizex):
            for y in range(self.sizey):
                if self.model.getPoint(x,y) == 1:
                    self.view.setBox(x,y)
                else:
                    self.view.unsetBox(x,y)

        self.view.update()

    def setBox(self,bx,by):
        self.view.setBox(bx,by)
        self.model.setPoint(bx,by)
        self.view.update()

    def unsetBox(self,bx,by):
        self.view.unsetBox(bx,by)
        self.model.unsetPoint(bx,by)                        
        self.view.update()

    def invertBox(self,bx,by):

        pointStatus = self.model.getPoint(bx,by)

        if pointStatus == 0:
            self.setBox(bx,by)
        elif pointStatus ==1:
            self.unsetBox(bx,by)
