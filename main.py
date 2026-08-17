import consts
import pygame
import screen
import game_field
import soldier

pygame.init()

pygame.display.set_caption("The flag game")

def main():
    pygame.init()
    window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    board = game_field.create_board()

    flag_row, flag_col = game_field.insert_flag(
        board
    )

    flag_indexes = game_field.get_flag_indexes(
        flag_row,
        flag_col)
    mines=game_field.create_mines(board)
    bushes=screen.random_grass()
    soldier_row,soldier_col=soldier.create_soldier()
    running = True

    mines_visible = False

    reveal_start_time = 0

    game_result = None

    result_start_time = 0
    clock=pygame.time.Clock()



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    if game_result is None:
                        mines_visible = True
                        reveal_start_time = (pygame.time.get_ticks())
                elif not mines_visible and game_result is None:
                    if event.key == pygame.K_UP:
                        soldier_row,soldier_col=soldier.move_soldier(soldier_row,soldier_col,"up")
                    elif event.key == pygame.K_DOWN:
                        soldier_row, soldier_col = soldier.move_soldier(soldier_row, soldier_col, "down")
                    elif event.key == pygame.K_LEFT:
                        soldier_row, soldier_col = soldier.move_soldier(soldier_row, soldier_col, "left")
                    elif event.key == pygame.K_RIGHT:
                        soldier_row, soldier_col = soldier.move_soldier(soldier_row, soldier_col, "right")
            if mines_visible:

                current_time = pygame.time.get_ticks()

                elapsed_time = (current_time- reveal_start_time)
                if elapsed_time >= consts.MINE_REVEAL_TIME:
                    mines_visible = False
                if game_result is None:
                    soldier_legs=soldier.create_soldier_legs(soldier_row,soldier_col)
                    if game_field.leg_touches_mines(mines,soldier_legs):
                        game_result="lose"
                        result_start_time=pygame.time.get_ticks()
                    else:
                        soldier_body=soldier.create_soldier_body(soldier_row,soldier_col)
                        if game_field.body_touches_flag(flag_indexes,soldier_body):
                            game_result="win"
                            result_start_time=pygame.time.get_ticks()
        window.fill(consts.GREEN)
        pygame.display.flip()
        if mines_visible:
            screen.draw_grid(window)
            screen.draw_mines(window,mines)
        else:
            screen.draw_bushes(window,bushes)
            screen.draw_flag(window)
           #THE GAME DOES WORK BUT THE GRAPHICS DONT!









if __name__ == "__main__":
    main()

