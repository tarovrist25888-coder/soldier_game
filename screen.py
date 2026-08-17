import random
import game_field
import pygame
from pygame import draw
from pygame.constants import QUIT
import consts
from consts import TILE_SIZE
import soldier





window = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption('SOLDIER GAME')

soldier_img = pygame.image.load("bin\\soldier.png").convert()
soldier_resized=pygame.transform.scale(soldier_img,(TILE_SIZE*2,TILE_SIZE*4))
flag = pygame.image.load("bin\\flag.png").convert()
flag_resized=pygame.transform.scale(flag,(TILE_SIZE*4,TILE_SIZE*3))
grass = pygame.image.load("bin\\grass.png").convert()
grass_resized=pygame.transform.scale(grass,(TILE_SIZE,TILE_SIZE))
mine = pygame.image.load("bin\\mine.png").convert()
mine_resized=pygame.transform.scale(mine,(TILE_SIZE*3,TILE_SIZE))

def create_screen():
    screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    return screen
def fill_screen(screen):
    screen.fill(consts.GREEN)




def random_grass():
    grass_positions = []
    for i in range(consts.NUM_BUSHES):
        x = random.randint(0, consts.WINDOW_WIDTH)
        y = random.randint(0, consts.WINDOW_HEIGHT)
        if (x, y) in grass_positions:
            x = random.randint(0, consts.WINDOW_WIDTH)
            y = random.randint(0, consts.WINDOW_HEIGHT)
        grass_positions.append((x, y))

    return grass_positions
def draw_bushes(screen,grass_positions):
    for i in grass_positions:
        screen.blit(grass_resized,i)


def draw_grid(screen):
    # Horizontal lines
    for row in range(consts.FIELD_ROWS + 1):

        y = row * TILE_SIZE

        pygame.draw.line(
            screen,
            consts.BLACK,
            (0, y),
            (consts.WINDOW_WIDTH, y)
        )
     # Vertical lines
    for col in range(consts.FIELD_COLS + 1):

        x = col * TILE_SIZE

        pygame.draw.line(
            screen,
            consts.BLACK,
            (x, 0),
            (x, consts.WINDOW_HEIGHT)
        )

def draw_mines(screen,mines):
    for mine in mines():
        for row,col in mine:
            x=row*TILE_SIZE
            y=col*TILE_SIZE
            screen.blit(mine_resized,(x,y))
def draw_soldier(screen):
    soldier_pos = soldier.create_soldier()
    screen.blit(soldier, soldier_pos)


def draw_flag(screen):
    flag_pos = (47 * TILE_SIZE, 21 * TILE_SIZE)
    screen.blit(flag, flag_pos)
def draw_message(message):
    font = pygame.font.SysFont("Calibri", 5)
    text_img = font.render(message, True, "black")
    window.blit(text_img, (10, 10))
