import pygame
import time


class SnakeHead():
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.direction = "RIGHT"
        self.turn = self.direction
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def createSnake(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

    def getRect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def move(self):
        keys = pygame.key.get_pressed()
        # Lập trình quẹo
        if keys[pygame.K_LEFT]:
            self.turn = "LEFT"
        if keys[pygame.K_RIGHT]:
            self.turn = "RIGHT"
        if keys[pygame.K_UP]:
            self.turn = "UP"
        if keys[pygame.K_DOWN]:
            self.turn = "DOWN"
     # Lập trình hướng
        if self.turn == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.turn == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if self.turn == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.turn == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
     # Lập trình di chuyển
        if self.direction == "LEFT" and self.x > 0:
            self.x -= self.vel
        if self.direction == "RIGHT" and self.x < (500 - self.width):
            self.x += self.vel
        if self.direction == "UP" and self.y > 0:
            self.y -= self.vel
        if self.direction == "DOWN" and self.y < (600 - self.height):
            self.y += self.vel
