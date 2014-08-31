# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
import time
import math

from Colour import *

class Player(pygame.sprite.Sprite):
    
    # Set speed vector
    change_x = 0
    change_y = 0    
    
    frame = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        # List that the player images will be saved in.
        self.images = []

        # Number of sprite + 1 = 13
        for i in range(1, 13):
            img = pygame.image.load("sprite/player/player" + str(i) + ".png").convert_alpha()
            img.set_colorkey(white)
            self.images.append(img)
        
        # By default, use image 0
        self.image = self.images[0]

        # Fetch the rectangle object that has the dimensions of the image image.
        self.rect = self.image.get_rect()
        
    # Change the speed of the player
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
         
    # Find a new position for the player
    def update(self):
        # Update position based on speed
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        
        # If we are moving bottom to up
        if self.change_y < 0:
            # Update our frame counter
            self.frame += 1
            
            # We go from 0...2. If we are above image 2, reset to 0
            # Multiply by 3 because we flip the image every 3 frames
            if self.frame > 2 * 3:
                self.frame = 0 
                
            # Grab the image, do floor division by 3 because we flip every 3 frames. 
            # Frames 0...2 -> image[0]
            # Frames 3...5 -> image[1]
            self.image = self.images[self.frame//3]

        # Move left to right. About the same as before, but use
        # images 3...5 instead of 0...2. Note that we add 3 in the last line to do this.
        if self.change_x > 0:
            self.frame += 1
            if self.frame > 2 * 3:
                self.frame = 0
            self.image = self.images[self.frame//3+3]

        # Move right to left
        if self.change_y > 0:
            self.frame += 1
            if self.frame > 2 * 3:
                self.frame = 0
            self.image = self.images[self.frame//3+3+3]

        # Move
        if self.change_x < 0:
            self.frame += 1
            if self.frame > 2 * 3:
                self.frame = 0
            self.image = self.images[self.frame//3+3+3+3]
