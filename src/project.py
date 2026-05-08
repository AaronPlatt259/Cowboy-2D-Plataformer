import pygame
import os
import random


class Player:
    def __init__(self ,x_axis=120, y_axis = 100, speed = 5):
        self.index = 0
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.idle_image = pygame.image.load('cowboy.png').convert_alpha()
        self.img = self.idle_image
        self.pos = self.get_rectangle()
        self.speed = speed
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
        rectangle = self.img.get_rect(topleft=(100,250)) 
        return rectangle

    def update(self, keys):
        if keys [pygame.K_LEFT]:
           self.pos.x -= self.speed
           self.animate()
        elif keys [pygame.K_RIGHT]:
            self.pos.x += self.speed
            self.animate()
        else:
            self.img = self.idle_image
            self.index = 0

    def animate(self):
        self.index += 0.5
        if self.index >= 15:
            self.index = 0
        self.img = self.movement[int(self.index)]



    def draw(self, surface):
        surface.blit(self.img, self.pos)

class Enemy:
    def __init__(self ,x_axis=120, y_axis = 100, speed = 5, enemy_update = 'enemy_01.png'):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.enemy = enemy_update
        self.img = self.load_image()
        self.pos = self.get_rectangle()
        self.speed = speed
        
    def load_image(self):
        img = pygame.image.load(self.enemy).convert_alpha()
        #img = pygame.transform.scale(img, (self.x_axis//2, self.y_axis//2))
        return img
    
    def get_rectangle(self):
        rectangle = self.img.get_rect(topleft=(600,360)) 
        return rectangle
    
    def update(self, running):
        if running == True:
            self.pos.x -= self.speed

    def update_variation(self, keys):
        variations = {
          pygame.K_0: 'enemy_01.png',
          pygame.K_1: 'enemy_02.png',
          pygame.K_2: 'enemy_03.png'
        }

        for key, filename in variations.items():
            if keys[key]:
                if self.enemy != filename:
                    self.enemy = filename
                    self.img = self.load_image()
                break

    
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

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    player = Player()
    bg = Background(pos=(0,0))
    enemy = Enemy()
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

     #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        keys = pygame.key.get_pressed()
        bg.update_variation(keys)
        player.update(keys)
        enemy.update(running)
        enemy.update_variation(keys)
     #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        screen.fill('Black')
        bg.draw(screen)
        enemy.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(24)
    pygame.quit()
    
if __name__ == "__main__":
    main()
