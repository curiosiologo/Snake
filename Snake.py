import pygame
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CELL_SIZE = 20


RED = (255,0,0)
GREEN_BK = (0,255,0)
GREEN_LIGHT = (0,25,180)

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

class Morfar:
    def __init__(self):
        self.x = random.randint(0,50)
        self.y = random.randint(0,50)
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Snake_head:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.next = None
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_LIGHT, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if self.next != None:
            self.next.draw(screen)

    def move(self, x, y):
        if self.next != None: 
            self.next.move(self.x, self.y)
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.direction = RIGHT
        self.head = Snake_head()
    
    def draw(self, screen):
        self.head.draw(screen)
    
    def move(self):
        new_x = self.head.x + self.direction[0]
        new_y = self.head.y + self.direction[1]
        if new_x >= 50:
            new_x = 50
        self.head.move(new_x, new_y)
        

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
food = Morfar()
snake = Snake()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_a and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_d and snake.direction != LEFT:
                snake.direction = RIGHT
            elif event.key == pygame.K_w and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_s and snake.direction != UP:
                snake.direction = DOWN


    
    prox_x = snake.head.x + snake.direction[0]
    prox_y = snake.head.y + snake.direction[1]

    if food.x == prox_x and food.y == prox_y:
        new_head = Snake_head(prox_x, prox_y)
        new_head.next = snake.head
        snake.head = new_head
        food = Morfar()
    else:
        snake.move()

    screen.fill(GREEN_BK)
    food.draw(screen)
    snake.draw(screen)
    pygame.display.flip()
    clock.tick(10)