import pygame
import os
import random


class Player:
    def __init__(self ,x_axis =100, y_axis = 250, x_speed = 7, jump_height = 20, y_speed = 20):
        self.index = 0
        self.is_jumping = False
        self.jump = jump_height
        self.jump_speed = y_speed
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.idle_image = pygame.image.load('cowboy.png').convert_alpha()
        self.img = self.idle_image
        self.pos = self.get_rectangle()
        self.speed = x_speed
        self.movement = [pygame.image.load('Timeline 1_0000.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0001.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0002.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0003.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0004.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0005.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0006.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0007.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0008.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0009.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0010.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0011.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0012.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0013.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0014.png').convert_alpha(),
                         pygame.image.load('Timeline 1_0015.png').convert_alpha(),
                         
                         ]
       

    def get_rectangle(self):
        rectangle = self.img.get_rect(topleft=(self.x_axis,self.y_axis)) 
        return rectangle
    

    def update(self, keys, enemy):
        moving = False
        #if self.pos.colliderect(enemy.pos):
            #print("collision activated")


        if keys [pygame.K_LEFT]:
           self.pos.x -= self.speed
           self.animate()
           moving = True
        elif keys [pygame.K_RIGHT]:
            self.pos.x += self.speed
            self.animate()
            moving = True
        if keys [pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.animate()

        if not moving and not self.is_jumping:
            self.img = self.idle_image
            self.index = 0
        self.jumping()

    def animate(self):
        self.index += 0.5
        if self.index >= 15:
            self.index = 0
        self.img = self.movement[int(self.index)]

    def jumping(self):
        gravity = 1
        if self.is_jumping:
            self.pos.y -= self.jump_speed
            self.jump_speed -= gravity
            if self.jump_speed <- self.jump:
                self.is_jumping = False
                self.jump_speed = self.jump

    def draw(self, surface):
        surface.blit(self.img, self.pos)

class Enemy:
    def __init__(self ,x_axis=120, y_axis = 100, speed = 5, enemy_update = 'enemy_01.png'):
        self.index = 0
        self.enemy_number = 2
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.idle_image = pygame.image.load('enemy_01.png').convert_alpha()
        self.enemy = enemy_update
        self.img = self.idle_image
        self.pos = self.get_rectangle()
        self.speed = speed
        self.movement = [pygame.image.load(f'Timeline {self.enemy_number}_0000.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0000.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0001.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0003.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0004.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0005.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0006.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0007.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0008.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0009.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0010.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0011.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0012.png').convert_alpha(),
                    pygame.image.load(f'Timeline {self.enemy_number}_0013.png').convert_alpha(),
                    ]
        
    
    def get_rectangle(self):
        rectangle = self.img.get_rect(topleft=(600,342)) 
        return rectangle.inflate(-55, -55)
    
    def update(self, running):
        if running == True:
            self.pos.x -= self.speed
            self.animate()

    def update_variation(self, keys):
        variations = {
          pygame.K_0: 2,
          pygame.K_1: 3,
          pygame.K_2: 4
        }
        

        for key, filename in variations.items():
            if keys[key]:
                if self.enemy_number != filename:
                    self.enemy_number = filename
                    self.movement = [
                        pygame.image.load(f'Timeline {self.enemy_number}_{i:04d}.png').convert_alpha()
                        for i in range(13)
                    ]
                break

    def animate(self):
        self.index += 0.5
        if self.index >= 13:
            self.index = 0
        self.img = self.movement[int(self.index)]

    def draw(self, surface):
        surface.blit(self.img, self.pos)

class Game_over_screen:
    def __init__(self ,x_axis =100, y_axis = 250, pos = (0,0)):
        self.img = pygame.image.load('game over screen.png').convert_alpha()
        self.pos = pos

    def draw(self, surface):
        surface.blit(self.img, self.pos)

    

class Background:
        def __init__(self, pos=(0,0),x_axis=120, y_axis = 100, bg_update = 'bg_01.jpg'):
            self.x_axis = x_axis
            self.y_axis = y_axis
            self.bg = bg_update
            self.pos = pos
            self.ground = self.image()
       
        def image(self):
            img = pygame.image.load(self.bg)
            #img = pygame.transform.scale(img, (self.x_axis*100, self.y_axis*100))
            return img
        
        def update_variation(self, keys):
            variations = {
            pygame.K_3: 'bg_01.jpg',
            pygame.K_4: 'bg_02.jpg',
            pygame.K_5: 'bg_03.jpg'
        }
            
            for key, filename in variations.items():
                if keys[key]:
                    if self.bg != filename:
                        self.bg = filename
                        self.ground = self.image()
                    break

        def draw(self, surface):
            surface.blit(self.ground, self.pos)
def main():
    pygame.init()
    pygame.display.set_caption("Cowboy Game")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    game_over = False
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    player = Player()
    bg = Background(pos=(0,0))
    enemy = Enemy()
    lose_screen = Game_over_screen()
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

     #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if not game_over:
            keys = pygame.key.get_pressed()
            bg.update_variation(keys)
            player.update(keys, enemy)
            enemy.update(running)
            enemy.update_variation(keys)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        if game_over:
            screen.fill('Black')
            lose_screen.draw(screen)

        else:
            screen.fill('Black')
            bg.draw(screen)
            enemy.draw(screen)
            player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(24)

        if player.pos.colliderect(enemy.pos):
            print("collision activated")
            game_over = True
        

    pygame.quit()
    
if __name__ == "__main__":
    main()
