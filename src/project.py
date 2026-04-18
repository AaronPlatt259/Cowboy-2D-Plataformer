import pygame
import random


class Player:
    def __init__(self, pos=(0,0),x_axis=120, y_axis = 100):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.pos = pos
        self.img = self.image()
       
    def image(self):
        img = pygame.image.load('cowboy_placeholder.png').convert_alpha()
        #img = pygame.transform.scale(img, (self.x_axis//2, self.y_axis//2))
        return img

    def draw(self, surface):
        surface.blit(self.img, self.pos)

class Background:
        def __init__(self, pos=(0,0),x_axis=120, y_axis = 100):
            self.x_axis = x_axis
            self.y_axis = y_axis
            self.pos = pos
            self.ground = self.image()
       
        def image(self):
            img = pygame.image.load('bg_placeholder.jpg')
            #img = pygame.transform.scale(img, (self.x_axis*100, self.y_axis*100))
            return img

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
    player = Player(pos=(0,0))
    bg = Background(pos=(0,0))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill('Green')
        bg.draw(screen)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()
    
if __name__ == "__main__":
    main()
