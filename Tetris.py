import pygame

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
ROW = 23
COL = 16
BLOCK_SIZE = 25

#create game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

#game surface where the shapes will be drawn and the game will be played
gameSurface = pygame.Surface((SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT-25))
gameSurface.fill((0,0,0))

# a window to show the next piece 
nextPieceSurface = pygame.Surface((200, 200))
nextPieceSurface.fill((0,0,0))

# control FPS
clock = pygame.time.Clock()

def drawGrid():
    for i in range(ROW):
        for j in range(COL):
            rect = pygame.Rect(j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(gameSurface, (50,50,50), rect, 1)

# game loop
run = True
while run:
    #create event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw screen and surfaces
    screen.fill((150,150,150))
    drawGrid()
    screen.blit(gameSurface, (10,10))
    screen.blit(nextPieceSurface, (SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/2 - 50))
    pygame.display.flip()
    clock.tick(24)

pygame.quit()


           