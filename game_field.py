import consts
import random as rd
import pygame
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
    return board
def create_mines():

