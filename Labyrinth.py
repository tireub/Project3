import pygame
from pygame.locals import *


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
        with open(self.file , "r") as file:
            self.grid = []

            for line in file:
                grid_line = []
                # for loop over the lines to define the sprites values
                for sprite in line:
                    grid_line.append(sprite)

                self.grid.append(grid_line)


level = Labyrinth('Level1')
level.create()

#Pygame part to display
pygame.init()

#Window generation
window = pygame.display.set_mode((600,600))

#import  images
background = pygame.image.load("img/background5.jpg")
wall = pygame.image.load("img/wall2.jpg")
finish = pygame.image.load("img/finish.jpg")

#display the level
y_pos = 0
for lines in level.grid:
    #for each line we set the line position (sprite size = 31*31


    x_pos = 0
    for sprites in lines:
        #for each sprite we calculate the position
        x = x_pos * 31
        y = y_pos * 31
        if sprites == "w" or sprites == "g":
            window.blit(background,(x,y))
        elif sprites == "b":
            window.blit(wall, (x,y))
        elif sprites == "r":
            window.blit(finish, (x,y))
        x_pos += 1

    y_pos += 1


#Screen refresh
pygame.display.flip()

#Infinite loop to keep the window open
loop = 1
while loop:
	for event in pygame.event.get():
		if event.type == QUIT:
			loop = 0

