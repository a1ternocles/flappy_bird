import pygame, sys, time
from debug import debug
#display & timer

screen = pygame.display.set_mode(size= (1280, 720))
clock = pygame.time.Clock()

#rectangle
test_rect = pygame.Rect(0,310,100,100)
rect_pos = test_rect.x
test_speed = 800

previous_time = time.time()

while True:

    #delta time
    dt = time.time() - previous_time
    previous_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
    
    screen.fill(color='black')

    rect_pos += test_speed*dt
    test_rect.x = round(rect_pos)

    pygame.draw.rect(surface= screen, color='white', rect= test_rect)
    if test_rect.x >= 1280: rect_pos = -100
    pygame.display.update()







    