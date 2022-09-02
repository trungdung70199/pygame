import pygame
pygame.init()
screen = pygame.display.set_mode((500,600))
GREY = (120,120,120)
WHITE = (255,255,255)
running = True
while running:
    screen.fill(GREY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()

