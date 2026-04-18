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
        #img = pygame.transform.scale(img, (self.x_axis*2, self.y_axis*2))
        return img

    def draw(self, surface):
        surface.blit(self.img, self.pos)

def main():
    pygame.init()

if __name__ == "__main__":
    main()
