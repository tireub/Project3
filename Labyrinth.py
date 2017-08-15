import pygame
from pygame.locals import *

'''
Classes
'''

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

#def display the level
    def display(self):

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
class character:

    #def initialisation of the character
    def __init__(self, char_pos):
        self.pos = char_pos
        self.sprite = char_sprite
        self.img = pygame.image.load("img/mcgiver.png").convert()
        print(self.sprite)

    def move(self,direction):

        #while receiving a direction, check if it's a wall or the border, else move
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









'''
MAIN
'''

#Pygame part to display
pygame.init()

#Window generation
window = pygame.display.set_mode((675,675))

#import  images
background = pygame.image.load("img/background5.jpg")
wall = pygame.image.load("img/wall2.jpg")
finish = pygame.image.load("img/finish.jpg")
congrats_message = pygame.image.load("img/winner.jpg")

#Create the level
level = Labyrinth('Level1')
level.create()

#display the level
y_pos = 0
for lines in level.grid:
    #for each line we set the line position (sprite size = 31*31


    x_pos = 0
    for sprites in lines:
        #for each sprite we calculate the position
        x = x_pos * 45
        y = y_pos * 45
        #switch between the different types of sprites
        if sprites == "w" or sprites == "g":
            window.blit(background,(x,y))
            if sprites == "g":
                char_pos = (x + 7,y)
                char_sprite = (x_pos,y_pos)

        elif sprites == "b":
            window.blit(wall, (x,y))
        elif sprites == "r":
            window.blit(finish, (x,y))
        x_pos += 1

    y_pos += 1

#Initialise character
mcgiver = character(char_pos)

#insert character
window.blit(mcgiver.img, (mcgiver.pos[0],mcgiver.pos[1]))


#Screen refresh
pygame.display.flip()

#Infinite loop to keep the window open
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                mcgiver.move("up")
            if event.key == K_DOWN:
                mcgiver.move("down")
            if event.key == K_LEFT:
                mcgiver.move("left")
            if event.key == K_RIGHT:
                mcgiver.move("right")
        if event.type == QUIT:
            loop = 0

    # refresh everything
    level.display()
    window.blit(mcgiver.img, (mcgiver.pos[0], mcgiver.pos[1]))

    # Screen refresh
    pygame.display.flip()

    if level.grid[mcgiver.sprite[0]][mcgiver.sprite[1]] == "r":
        break

while loop:
    window.blit(congrats_message,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0

    pygame.display.flip()