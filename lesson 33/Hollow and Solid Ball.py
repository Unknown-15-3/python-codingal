import pygame
pygame.init()

window = pygame.display.set_mode((400,300))
window.fill((225, 225, 225))

GREEN = (0, 225, 0)

pygame.draw.circle(window, GREEN, (200,200), 50)
pygame.draw.circle(window, GREEN, (100,100), 50, 3)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()