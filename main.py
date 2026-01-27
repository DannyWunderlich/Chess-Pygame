import pygame

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

def init_pieces():
    # TODO
    # Initialize all the pieces on black and black side
    black_pawn = pygame.image.load("assets/black_pawn.png")
    shrunk_black_pawn = pygame.transform.smoothscale(black_pawn, (51, 51))
    return shrunk_black_pawn
    
def init_board():
    board = pygame.image.load("assets/board.png")
    shrunk_board = pygame.transform.smoothscale(board, (512, 512))
    return shrunk_board

def main():
    # Example file showing a basic pygame "game loop"

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE

        chess_board = init_board()
        black_pawn = init_pieces()

        screen.blit(chess_board, dest=(0, 0))
        screen.blit(black_pawn, dest=(51, 51))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()