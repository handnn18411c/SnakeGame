import pygame
from snake import Snake
from foody import Food

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Trò chơi con rắn")
snake = Snake(50, 100, 20, 20, 10)
food = Food(10, 10)

# Mainloop
while True:
    clock.tick(10)
    screen.fill((155, 155, 155))
    snake.createSnake(screen)
    food.createFood(screen)
    snake.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    collide = snake.getRect().colliderect(food.getRect())
    if collide:
        print("Collide")
        food.createFood(screen)

    pygame.display.flip()
