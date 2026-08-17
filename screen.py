import random
import game_field
import pygame
from pygame import draw
from pygame.constants import QUIT
import consts
from consts import TILE_SIZE

pygame.init()

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

pygame.display.set_caption('SOLDIER GAME')

soldier = pygame.image.load("bin\\soldier.png").convert()

flag = pygame.image.load("bin\\flag.png").convert()

grass = pygame.image.load("bin\\grass.png").convert()

mine = pygame.image.load("bin\\mine.png").convert()


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
        screen.blit(grass, (x*TILE_SIZE, y*TILE_SIZE))

def visualize_board(board, mines):
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = (col*consts.TILE_SIZE)
            y = (row*consts.TILE_SIZE)
            draw.rect(screen, consts.GREEN, (x, y, consts.TILE_SIZE, consts.TILE_SIZE), 1)
    for i in range(len(mines)):
        screen.blit(mine, (mines[i][0]*TILE_SIZE, mines[i][1]*TILE_SIZE))


def draw_details(object, matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == object:
                screen.blit(object, (x, y))

running = True

while running:
    pygame.init()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    fill_screen()
    random_grass()
    board = game_field.create_board()
    mines = game_field.get_mine_indexes
    visualize_board(board, mines)

    pygame.display.update()

    FPS = pygame.time.Clock()
    FPS.tick(60)
