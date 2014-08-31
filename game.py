#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import sys
import os
import time
import math

sys.path.append('./package')

from Player import *
from Colour import *
        
def main():
    pygame.init()

    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width,screen_height])

    icon = pygame.Surface((1, 1))
    icon.set_alpha(0)
    pygame.display.set_icon(icon)

    pygame.display.set_caption("Game")

    all_sprites_list = pygame.sprite.Group()

    player = Player()
    all_sprites_list.add(player)

    done = False

    clock = pygame.time.Clock()

    score = 0

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Set the speed based on the key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print "Left"
                    player.changespeed(-3,0)

                if event.key == pygame.K_RIGHT:
                    print "Right"
                    player.changespeed(3,0)

                if event.key == pygame.K_UP:
                    print "Up"
                    player.changespeed(0,-3)

                if event.key == pygame.K_DOWN:
                    print "Down"
                    player.changespeed(0,3)
                     
            # Reset speed when key goes up      
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3,0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-3,0)
                if event.key == pygame.K_UP:
                    player.changespeed(0,3)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0,-3)

        screen.fill(white)

        player.update()

        all_sprites_list.draw(screen)
        
        clock.tick(20)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
