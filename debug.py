import pygame

pygame.init()
font = pygame.font.Font(None, size= 36)

def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surface = font.render(str(info),True,'white')
    debug_rect = debug_surface.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface,'black',debug_rect)
    display_surface.blit(display_surface,debug_rect)