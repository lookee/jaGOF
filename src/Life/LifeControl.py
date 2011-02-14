
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

from Grid.GridControl import GridControl
from Grid.GridView import GridView
from LifeModel import LifeModel

class LifeControl(GridControl):

    def __init__(self, config, filename):

        self.sizex = config.getint('life','sizex')
        self.sizey = config.getint('life','sizey')
        self.width = config.getint('screen','width')
        self.heigth = config.getint('screen','heigth')

        self.waitTime = config.getint('animation','waitTime_ms') 
        self.waitTimeMin = config.getint('animation','waitTimeMin_ms')
        self.waitTimeMax = config.getint('animation','waitTimeMax_ms')
        self.waitTimeStep = config.getint('animation','waitTimeStep_ms')

        self.view = GridView(self.sizex,self.sizey,self.width,self.heigth)
        self.model = LifeModel(self.sizex,self.sizey)
 
        self.movie = False
        self.doEpoch = False
        self.keyPressed = False

        if filename is not None:
            self.readFile(filename)

        self.action()

    def afterAction(self):

        if self.doEpoch:
            self.epoch()
            self.doEpoch = self.movie
            if self.movie:
                pygame.time.wait(self.waitTime)

    def handleKeyEvents(self, event):

        super(self.__class__,self).handleKeyEvents(event)
        
        if event.key == pygame.K_e:
            self.doEpoch = True
            self.movie = False

        if event.key == pygame.K_m:
            self.movie = not self.movie
            self.doEpoch = True

        if event.key == pygame.K_PLUS:
            self.waitTime -= self.waitTimeStep
            if self.waitTime < self.waitTimeMin:
                self.waitTime = self.waitTimeMin

        if event.key == pygame.K_MINUS:
            self.waitTime += self.waitTimeStep
            if self.waitTime > self.waitTimeMax:
                self.waitTime = self.waitTimeMax

    def triggerEnd(self):
        print "epoch: %d" % self.model.get_epoch_counter()
        print "bye!"
        super(self.__class__,self).triggerEnd()

    def epoch(self):
        self.model.epoch()
        self.renderModel()

    def readFile(self, filename):
            self.model.read_seed_file(filename)
            self.renderModel()
