import random
import game_field
import pygame
from pygame import draw
from pygame.constants import QUIT
import consts
from consts import TILE_SIZE
import soldier
from game_field import get_flag_indexes
from soldier import create_soldier

pygame.init()

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

pygame.display.set_caption('SOLDIER GAME')

soldier = pygame.image.load("bin\\soldier.png").convert()
soldier = pygame.transform.scale(soldier,(TILE_SIZE*2,TILE_SIZE*4))

flag = pygame.image.load("bin\\flag.png").convert()
flag = pygame.transform.scale(flag,(TILE_SIZE*3,TILE_SIZE*4))

grass = pygame.image.load("bin\\grass.png").convert()
grass = pygame.transform.scale(grass, (3*TILE_SIZE, 2*TILE_SIZE))

mine = pygame.image.load("bin\\mine.png").convert()
mine = pygame.transform.scale(mine,(TILE_SIZE*3,TILE_SIZE))

def fill_screen():
    screen.fill(consts.LIGHT_GREEN)
    return screen


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

def draw_bushes(grass_positions):
    for i in grass_positions:
        screen.blit(grass, i)

def visualize_board(board, mines):
    rects = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = (col*consts.TILE_SIZE)
            y = (row*consts.TILE_SIZE)
            draw.rect(screen, consts.GREEN, (x, y, consts.TILE_SIZE, consts.TILE_SIZE), 1)
            rects.append((x, y))
    
    for i in range(len(mines)):
        screen.blit(mine, (mines[i][0]*TILE_SIZE, mines[i][1]*TILE_SIZE))

def draw_soldier():
    soldier_pos = create_soldier()
    screen.blit(soldier, soldier_pos)

def draw_flag():
    flag_pos = (47*TILE_SIZE, 21*TILE_SIZE)
    screen.blit(flag, flag_pos)






