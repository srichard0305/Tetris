import pygame
import Shapes
import random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('tahoma', 30)

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

score = '0'
textNextPiece = my_font.render('Next Piece', False, (0, 0, 0))
textScoreLabel = my_font.render('Score', False, (0, 0, 0))
textScore = my_font.render(score, False, (0, 0, 0))

rand = random.randint(0, 6)
shape = Shapes.Shape()
shape.x =  SCREEN_WIDTH//4
shape.y = -75
shape.getShape(rand, gameSurface)

randForNext = random.randint(0, 6)
nextShape = Shapes.Shape()
nextShape.x = 85
nextShape.y = 75
nextShape.getNextShape(randForNext, nextPieceSurface)

# control FPS
clock = pygame.time.Clock()

def drawGrid():
    for i in range(ROW):
        for j in range(COL):
            rect = pygame.Rect(j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(gameSurface, (50,50,50), rect, 1)

 # draw screen and surfaces
drawGrid()
screen.fill((150,150,150))
screen.blit(gameSurface, (10,10))
screen.blit(nextPieceSurface, (SCREEN_WIDTH//2 + 100, SCREEN_HEIGHT//2- 75))
screen.blit(textNextPiece, (SCREEN_WIDTH//2 + 128, SCREEN_HEIGHT//2- 125))
screen.blit(textScoreLabel, (SCREEN_WIDTH//2 + 150, SCREEN_HEIGHT//2- 250))
screen.blit(textScore, (SCREEN_WIDTH//2 + 180, SCREEN_HEIGHT//2- 195))
pygame.display.flip()

counter = 0
# game loop
run = True
while run:
    #create event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if(counter == 30):
        shape.moveDown()
        gameSurface.fill((0,0,0,))
        drawGrid()
        shape.getShape(rand, gameSurface)
        screen.blit(gameSurface, (10,10))
        pygame.display.flip()
        counter = 0
    
    counter = counter + 1
    clock.tick(60)

pygame.quit()


           