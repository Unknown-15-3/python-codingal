import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGING_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGING_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('Blue')
LIGHTBLUE = pygame.Color('LightBlue')
DARKBLUE = pygame.Color('Darkblue')

YELLOW = pygame.Color('Yellow')
MAGENTA = pygame.Color('Magenta')
ORANGE = pygame.Color('Orange')
WHITE = pygame.Color('White')

class Sprite(pygame.sprite.Sprite):
    def __init__ (self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True 
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1] =  -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGING_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGING_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE,LIGHTBLUE,DARKBLUE])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("boundary sprite")
bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGING_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGING_EVENT:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()