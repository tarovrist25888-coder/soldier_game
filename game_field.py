import consts
import pygame
import random
def create_board():
    board=[]
    for row in range(consts.FIELD_ROWS):
        board.append([])
        for col in range(consts.FIELD_COLS):
            board[row].append(consts.SAFE)
    return board

def insert_flag(board):
    flag_rows=consts.FIELD_ROWS-consts.FLAG_HEIGHT
    flag_cols=consts.FIELD_COLS-consts.FLAG_WIDTH

    for row in range(flag_rows,consts.FIELD_ROWS):
        for col in range(flag_cols,consts.FIELD_COLS):
            if board[row][col]==consts.SAFE:
                board[row][col]=consts.FLAG
    return flag_rows,flag_cols

def get_flag_indexes(flag_rows,flag_cols):
        flag_indexes = []
        for row in range(flag_rows, flag_rows + consts.FLAG_HEIGHT):
            for col in range(flag_cols, flag_cols + consts.FLAG_WIDTH):
                flag_indexes.append((row, col))
        return flag_indexes
def create_mines(board):
    mines=[]
    while len(mines)<consts.NUM_OF_MINES:

        row=random.randint(0,consts.FIELD_ROWS-1)
        col=random.randint(0,consts.FIELD_COLS-3)
        if board[row][col]==consts.SAFE and\
        board[row][col+1]==consts.SAFE and\
            board[row][col+2]==consts.SAFE:
            board[row][col]=consts.MINE
            board[row][col+1]=consts.MINE
            board[row][col+2]=consts.MINE

            mines.append([(row,col),(row,col+1),(row,col+2)])
    return mines

def get_mine_indexes(mines):
    mine_indexes=[]
    for row in range(consts.FIELD_ROWS):
        for col in range(consts.FIELD_COLS):
            if mines[row][col]==consts.MINE:
                mine_indexes.append((row,col))
    return mine_indexes

def leg_touches_mines(mines,soldier_legs):
    mines_indexes=get_mine_indexes(mines)
    for leg in soldier_legs:
        if leg in mines_indexes:
            return True
    return False

def body_touches_flag(flag_indexes,soldier_body):
    for body_cell in soldier_body:
        if body_cell in flag_indexes:
            return True
    return False
