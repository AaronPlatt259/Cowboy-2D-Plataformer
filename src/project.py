import pygame

vec = pygame.math.Vector2
class Player:
    def __init__(self ,x_axis =100, y_axis = 250, x_speed = 7, jump_height = 22):
        self.index = 0
        self.is_jumping = False
        self.jump = jump_height
        self.jump_speed = 0
        self.x_axis = x_axis
        self.y_axis = 500
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
    

    def update(self, keys, enemy, platforms):
            moving = False
            
            if keys[pygame.K_LEFT]:
                self.pos.x -= self.speed
                self.animate()
                moving = True
            elif keys[pygame.K_RIGHT]:
                self.pos.x += self.speed
                self.animate()
                moving = True
                
            if keys[pygame.K_UP] and not self.is_jumping:
                self.is_jumping = True
                self.jump_speed = self.jump
                self.animate()

            if not moving and not self.is_jumping:
                self.img = self.idle_image
                self.index = 0

            self.jumping(platforms)

    def animate(self):
        self.index += 0.5
        if self.index >= 15:
            self.index = 0
        self.img = self.movement[int(self.index)]

    def jumping(self, platforms):
        gravity = 1
        self.pos.y -= self.jump_speed
        self.jump_speed -= gravity

        on_ground = False

        if self.pos.bottom >= self.y_axis:
            self.pos.bottom = self.y_axis
            self.jump_speed = 0
            self.is_jumping = False
            on_ground = True 
           

        for platform in platforms:
            if self.pos.colliderect(platform.pos):
                if self.jump_speed <= 0 and self.pos.bottom <= platform.pos.top + 15:
                    self.pos.bottom = platform.pos.top
                    self.jump_speed = 0
                    self.is_jumping = False
                    on_ground = True

        if not on_ground:
            self.is_jumping = True

    def draw(self, surface, camera):
        surface.blit(self.img,(self.pos.x - camera.offset.x, self.pos.y))

class Platform:
    def __init__(self, platform_variations = 'plataform_01.png'):

        self.plat = platform_variations
        self.img = pygame.image.load(self.plat).convert_alpha()
        self.pos = self.get_rectangle()
        self.hitbox = self.pos.inflate(0, -20)
        self.hitbox.bottom = self.pos.bottom
    
    def get_rectangle(self):
        rectangle = self.img.get_rect(topleft=(1700,250))

        return rectangle
    
    def update_variation(self, keys):
        variations = {
        pygame.K_3: 'plataform_01.png',
        pygame.K_4: 'plataform_02.png',
        pygame.K_5: 'plataform_03.png'
        }
        
        for key, filename in variations.items():
            if keys[key]:
                if self.plat != filename:
                    self.plat = filename
                    self.img = pygame.image.load(self.plat).convert_alpha()
                    self.pos = self.img.get_rect(topleft=(1700,250))
                    self.hitbox = self.pos.inflate(0, -20) 
                    self.hitbox.bottom = self.pos.bottom
                break

    def draw(self, surface, camera):
        surface.blit(self.img,(self.pos[0] - camera.offset.x, self.pos[1]))    



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
        rectangle = self.img.get_rect(topleft=(800,342)) 
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

    def draw(self, surface, camera):
        surface.blit(self.img,(self.pos.x - camera.offset.x, self.pos.y))

class You_Win_screen:
    def __init__(self ,x_axis =100, y_axis = 250, pos = (0,0)):
        self.img = pygame.image.load('win_screen.jpg')
        self.pos = pos

    def draw(self, surface):
        surface.blit(self.img, self.pos)


    def draw(self, surface):
        surface.blit(self.img, self.pos)

class Game_over_screen:
    def __init__(self ,x_axis =100, y_axis = 250, pos = (0,0)):
        self.img = pygame.image.load('game over screen.png').convert_alpha()
        self.pos = pos

    def draw(self, surface):
        surface.blit(self.img, self.pos)


    def draw(self, surface):
        surface.blit(self.img, self.pos)

class FinishingLine:
    def __init__(self):
        self.pos = pygame.Rect(3100, 250, 10, 600)
    
    def draw(self, surface, camera):
        pygame.draw.rect(surface, (255, 255, 255), (self.pos.x - camera.offset.x, self.pos.y, self.pos.width, self.pos.height))
    
class Camera:
    def __init__(self, player):
        self.player = player
        self.display_width, self.display_height = 800, 600
        self.modify_width = 280
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.constant = vec(self.modify_width, self.display_height / 2)
        

    def set_method(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()


class CameraScroll:
    def __init__(self, camera, player): 
        self.camera = camera
        self.player = player
        self.bg_width = 3200

    def scroll(self):
        player_center = self.player.pos.x + (self.player.img.get_width() / 1)
        self.camera.offset_float.x += (player_center - self.camera.offset_float.x - self.camera.constant.x) / 20

        if self.camera.offset_float.x < 0:
            self.camera.offset_float.x = 0

        max_scroll = self.bg_width - self.camera.display_width
        if self.camera.offset_float.x > max_scroll:
            self.camera.offset_float.x = max_scroll

        self.camera.offset.x = int(self.camera.offset_float.x)

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

        def draw(self, surface, camera):
            surface.blit(self.ground,(self.pos[0] - camera.offset.x, self.pos[1]))

def main():
    pygame.init()
    pygame.display.set_caption("Cowboy Game")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    game_over = False
    game_completed = False
    fullscreen = False
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    player = Player()
    platform = Platform()
    bg = Background(pos=(0,0))
    enemy = Enemy()
    lose_screen = Game_over_screen()
    win_screen = You_Win_screen()
    camera = Camera(player)
    scroll = CameraScroll(camera, player)
    finish = FinishingLine()
    camera.set_method(scroll)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((resolution), pygame.FULLSCREEN | pygame.SCALED)
                    else:
                        screen =  pygame.display.set_mode(resolution)

     #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if not game_over and not game_completed:
            keys = pygame.key.get_pressed()
            bg.update_variation(keys)
            platform.update_variation(keys)
            player.update(keys, enemy, [platform])
            enemy.update(running)
            enemy.update_variation(keys)
            camera.scroll()

            if player.pos.colliderect(finish.pos):
                game_completed = True

            if player.pos.colliderect(enemy.pos):
                print("collision activated")
                game_over = True
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        screen.fill('Black')
        if game_completed:
            screen.fill('Yellow')
            win_screen.draw(screen)
        elif game_over:
            screen.fill('Black')
            lose_screen.draw(screen)
        else:
            bg.draw(screen, camera)
            platform.draw(screen, camera)
            enemy.draw(screen, camera)
            player.draw(screen, camera)
            #finish.draw(screen, camera)

        pygame.display.flip()
        dt = clock.tick(24)
        

        

    pygame.quit()
    
if __name__ == "__main__":
    main()
