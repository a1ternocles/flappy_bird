import pygame,sys,time
import random

#init
pygame.init()

#screen
screen = pygame.display.set_mode(size=(1280,720))
clock = pygame.time.Clock()

#class
class TestObject(pygame.sprite.Sprite):
    
    # init method
    def __init__(self,type = None):
        super().__init__()

        #ATTRIBUTES

        # animation
        if type == 'plane': 
            self.frames = [pygame.image.load(f'graphics\\plane\\red{i}.png').convert_alpha() for i in range(0,3)]
        elif type == 'fly': 
            self.frames  = [pygame.image.load(f'graphics\\Fly\\Fly{i}.png').convert_alpha() for i in range(1,3)]
        
        self.frame_index = 0

        # image & rect
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midleft = (0,360))

        # movement
        self.rotation = 0
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.x_pos = 1
        self.y_pos = 1
        self.move_speed = 200
        self.animation_speed = 5

    
    # regular methods
    def animate(self,dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def move(self,dt):
        self.pos.x += self.x_pos * self.move_speed * dt
        self.pos.y += self.y_pos * self.move_speed * dt

        self.rect.x = random.randint(1,2) + round(self.pos.x)
        self.rect.y = random.randint(1,2) + round(self.pos.y)

        if self.rect.right >= 1280 or self.rect.left <= 0: 
            self.x_pos *= -1   #backward movement

        if self.rect.top >= 630 or self.rect.bottom <= 60:
            self.y_pos *= -1
    
    def rotate(self,dt):
        self.rotation += 50 * dt
        self.image = pygame.transform.rotozoom(surface= self.image, angle= self.rotation, scale=2)

    def update(self,dt):
        self.animate(dt)
        self.move(dt)
        self.rotate(dt)

#class groups
test_group = pygame.sprite.Group()
test_group.add(TestObject(random.choice(['fly','plane'])))
test_group.add(TestObject(random.choice(['fly','plane'])))


prev_time = time.time()

while True:
    dt =  time.time() - prev_time
    prev_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    screen.fill('grey')
    test_group.update(dt)
    test_group.draw(surface=screen)

    pygame.display.update()
    clock.tick(60)