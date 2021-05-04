import pygame
import random


class Food():
    def __init__(self, width, height):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 600)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def createFood(self, screen):
        pygame.draw.rect(screen, (255, 0, 255),
                         (self.x, self.y, self.width, self.height))

    def getRect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def newPosition(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 600)
        pygame.display.update()
