import pygame
from pygame.locals import *

import random

#Definition of Labyrinth
class Labyrinth:
#Game level class

#def Initialisation of the level
    def __init__(self , file):
        self.file = file
        self.grid = []


#def Read the file Level1 to import the level structure
    def create(self):
        # save into list within a list (main list for lines, secondary list for columns
        with open(self.file, "r") as file:
            self.grid = []

            for line in file:
                grid_line = []
                # for loop over the lines to define the sprites values
                for sprite in line:
                    grid_line.append(sprite)

                self.grid.append(grid_line)

#def display the level
    def display(self, level, window):

        background = pygame.image.load("img/background5.jpg")
        wall = pygame.image.load("img/wall2.jpg")
        finish = pygame.image.load("img/finish.jpg")
        y_pos = 0
        for lines in level.grid:
            # for each line we set the line position (sprite size = 31*31

            x_pos = 0
            for sprites in lines:
                # for each sprite we calculate the position
                x = x_pos * 45
                y = y_pos * 45
                # switch between the different types of sprites
                if sprites == "w" or sprites == "g":
                    window.blit(background, (x, y))
                if sprites == "b":
                    window.blit(wall, (x, y))
                if sprites == "r":
                    window.blit(finish, (x, y))
                x_pos += 1

            y_pos += 1


#Definition of our hero
class Character:

    #def initialisation of the character
    def __init__(self, char_pos, char_sprite):
        self.pos = char_pos
        self.sprite = char_sprite
        self.img = pygame.image.load("img/mcgiver.png").convert()


    def move(self, direction, level):

        #while receiving a direction, check if it's not a wall or the border, then move and update position
        if direction == "up":
            if self.sprite[0] > 0:
                if level.grid[self.sprite[0] - 1][self.sprite[1]] != "b":
                    self.pos = [(self.pos[0]),(self.pos[1] - 45)]
                    self.sprite = [(self.sprite[0] - 1), (self.sprite[1])]
        if direction == "down":
            if self.sprite[0] < 14:
                if level.grid[self.sprite[0] + 1][self.sprite[1]] != "b":
                    self.pos = [(self.pos[0]), (self.pos[1] + 45)]
                    self.sprite = [(self.sprite[0] + 1), (self.sprite[1])]
        if direction == "right":
            if self.sprite[1] < 14:
                if level.grid[self.sprite[0]][self.sprite[1] + 1] != "b":
                    self.pos = [(self.pos[0] + 45), (self.pos[1])]
                    self.sprite = [(self.sprite[0]), (self.sprite[1] + 1)]
        if direction == "left":
            if self.sprite[1] > 0:
                if level.grid[self.sprite[0]][self.sprite[1] - 1] != "b":
                    self.pos = [(self.pos[0] - 45), (self.pos[1])]
                    self.sprite = [(self.sprite[0]), (self.sprite[1] - 1)]


#Definition of the objects
class Object:

    #initialisation
    def __init__(self, type):
        self.name = type
        self.img = pygame.image.load("img/" + type + ".png").convert()
        self.location = "labyrinth"
        self.sprite = (0, 0)

    #Object generation randomly on a w sprite
    def generate(self, level):
        x = random.randint(0, 14)
        y = random.randint(0, 14)

        while level.grid[x][y] != "w":
            x = random.randint(0, 14)
            y = random.randint(0, 14)


        self.sprite = (x, y)


    #Display the object
    def display(self, window):
        x_pos = self.sprite[0] * 45 + 5
        y_pos = self.sprite[1] * 45 + 5
        window.blit(self.img, (y_pos, x_pos))

