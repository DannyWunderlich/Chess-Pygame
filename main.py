import pygame

#DIMENSIONS

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

SQUARE_WIDTH = 64
SQUARE_HEIGHT = 64

#COLORS

PINK = (211, 187, 227)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def init_pieces():
    # TODO
    # Initialize all the pieces on white and black side
    # ==== Need to fix sizing and placement issue with the pieces ====
    black_pawn = pygame.image.load("assets/black_pawn.png")
    shrunk_black_pawn = pygame.transform.smoothscale(black_pawn, (51, 51))

    return shrunk_black_pawn

def init_board():
    squares_created = 0

    for x_pos in range(0, SCREEN_WIDTH, SQUARE_WIDTH):
        for y_pos in range(SCREEN_HEIGHT, -1, -1 * SQUARE_HEIGHT):
            if(squares_created % 2):
                game_board = pygame.Rect(x_pos, y_pos, 64, 64) #create rectangle object and display it to the screen
                pygame.draw.rect(screen, PINK, game_board)
            else:
                game_board = pygame.Rect(x_pos, y_pos, 64, 64) #create rectangle object and display it to the screen
                pygame.draw.rect(screen, WHITE, game_board)

                squares_created += 1

def main():
    # Example file showing a basic pygame "game loop"

    # pygame setup
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                

        # RENDER YOUR GAME HERE
        init_board()

        # print(pygame.mouse.get_pos())

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()