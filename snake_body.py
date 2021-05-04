import pygame


class Body():
    def __init__(self, snakeHead):
        self.snakeHead = snakeHead

    def createBody(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.snakeHead.x+20, self.snakeHead.y,
                          self.snakeHead.width, self.snakeHead.height))

    def move(self):
        keys = pygame.key.get_pressed()
        # Lập trình quẹo
        if keys[pygame.K_LEFT]:
            self.snakeHead.turn = "LEFT"
        if keys[pygame.K_RIGHT]:
            self.snakeHead.turn = "RIGHT"
        if keys[pygame.K_UP]:
            self.snakeHead.turn = "UP"
        if keys[pygame.K_DOWN]:
            self.snakeHead.turn = "DOWN"
     # Lập trình hướng
        if self.snakeHead.turn == "LEFT" and self.snakeHead.direction != "RIGHT":
            self.snakeHead.direction = "LEFT"
        if self.snakeHead.turn == "RIGHT" and self.snakeHead.direction != "LEFT":
            self.snakeHead.direction = "RIGHT"
        if self.snakeHead.turn == "UP" and self.snakeHead.direction != "DOWN":
            self.snakeHead.direction = "UP"
        if self.snakeHead.turn == "DOWN" and self.snakeHead.direction != "UP":
            self.snakeHead.direction = "DOWN"
     # Lập trình di chuyển
        if self.snakeHead.direction == "LEFT" and self.snakeHead.x > 0:
            self.snakeHead.x -= self.snakeHead.vel
        if self.snakeHead.direction == "RIGHT" and self.snakeHead.x < (500 - self.snakeHead.width):
            self.snakeHead.x += self.snakeHead.vel
        if self.snakeHead.direction == "UP" and self.snakeHead.y > 0:
            self.snakeHead.y -= self.snakeHead.vel
        if self.snakeHead.direction == "DOWN" and self.snakeHead.y < (600 - self.snakeHead.height):
            self.snakeHead.y += self.snakeHead.vel

    def setLength(self):
        self.snakeHead.height += 5
