import pygame
from snake_head import SnakeHead
from snake_body import Body
from foody import Food

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Trò chơi con rắn")
snake = SnakeHead(50, 100, 20, 20, 10)
body = Body(snake)
food = Food(10, 10)

# Mainloop
while True:
    clock.tick(10)
    screen.fill((155, 155, 155))
    snake.createSnake(screen)
    body.createBody(screen)
    food.createFood(screen)
    snake.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    collide = snake.getRect().colliderect(food.getRect())
    if collide == True:
        # print("Snake Length: ", body.width)
        body.setLength()
        food.newPosition()
        print("Food postion", food.x, food.y)

    pygame.display.flip()
