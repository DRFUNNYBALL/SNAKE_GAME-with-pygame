import pygame, sys , random
from tkinter import messagebox
from pygame.math import Vector2
class snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(3, 10), Vector2(4, 10)]
        self.direction =  Vector2(1, 0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
            
            
    def move_snake(self):
        if self.new_block == True : #for + snake, if you want snake dont be big : new block = add_block
            body = self.body [:]
            body.insert(0, body[0] + self.direction)
            self.body = body[:]
            self.new_block = False # for stoping from big snake 
        else :
            body = self.body[:-1]
            body.insert(0, body[0] + self.direction)
            self.body = body[:]

    def add_block(self): 
        self.new_block = True
        
class FRUIT():
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)
          
class Main():
    def __init__(self):
        self.snake = snake()
        self.fruit = FRUIT()
    def up(self) : 
        self.snake.move_snake()  
        self.check()
        self.fail()
        
    def draw_el(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check(self) :
        if self.fruit.pos == self.snake.body [0] :
            self.fruit.randomize()
            self.snake.add_block()
    def fail (self) :
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_ove()
    def game_ove (self):
        pygame.quit()
        sys.exit()        
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('image//12345.png').convert_alpha()#add your pic for apple

SCREEN_UP = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UP, 150)

main_game = Main()

while True:
    for event in pygame.event.get() :
        if  event.type == pygame.QUIT :
           pygame.quit()
           sys.exit()
        if event.type == SCREEN_UP :
            main_game.up()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                if main_game.snake.direction != 1:
                    main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN :
                if main_game.snake.direction != -1:
                    main_game.snake.direction = Vector2(0, +1)
            elif event.key == pygame.K_RIGHT :
                if main_game.snake.direction != -1:
                    main_game.snake.direction = Vector2(+1, 0)
            elif event.key == pygame.K_LEFT :
                if main_game.snake.direction != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                 
    screen.fill((175, 215, 70)) #for color
    main_game.draw_el()
    pygame.display.update()
    clock.tick(60) #for framerate    
    
    
