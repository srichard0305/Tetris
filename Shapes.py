import pygame

x,y = (0,0)
BLOCK_SIZE = 25

O = [(x,y), (x+(BLOCK_SIZE*2), y), (x+(BLOCK_SIZE*2), y+(BLOCK_SIZE*2)), (x, y+(BLOCK_SIZE*2))] 
I = [(x,y), (x+BLOCK_SIZE, y), (x+BLOCK_SIZE, y+(BLOCK_SIZE*4)), (x, y+(BLOCK_SIZE*4)) ]
S = [(x,y), (x+BLOCK_SIZE,y),  (x+BLOCK_SIZE,y+BLOCK_SIZE), (x+(BLOCK_SIZE*2),y+BLOCK_SIZE), (x+(BLOCK_SIZE*2),y+(BLOCK_SIZE*3))
     ,(x+BLOCK_SIZE,y+(BLOCK_SIZE*3)), (x+BLOCK_SIZE,y+(BLOCK_SIZE*2)), (x,y+(BLOCK_SIZE*2)), (x,y+BLOCK_SIZE)  ]
Z = [(x+BLOCK_SIZE,y), (x+(BLOCK_SIZE*2),y), (x+(BLOCK_SIZE*2),y+(BLOCK_SIZE*2)),  (x+BLOCK_SIZE,y+(BLOCK_SIZE*2)), (x+BLOCK_SIZE,y+(BLOCK_SIZE*3)), 
     (x,y+(BLOCK_SIZE*3)), (x,y+BLOCK_SIZE), (x + BLOCK_SIZE,y+BLOCK_SIZE)  ]
L = [(x,y),(x+BLOCK_SIZE,y), (x+BLOCK_SIZE,y+(BLOCK_SIZE*2)), (x+(BLOCK_SIZE*2),y+(BLOCK_SIZE*2)), (x+(BLOCK_SIZE*2),y+(BLOCK_SIZE*3)), 
     (x, y +(BLOCK_SIZE*3)) ]
J = [(x+BLOCK_SIZE,y), (x+(BLOCK_SIZE*2),y), (x+(BLOCK_SIZE*2),y+(BLOCK_SIZE*3)),(x,y+(BLOCK_SIZE*3)), (x,y+(BLOCK_SIZE*2)), (x + BLOCK_SIZE,y+(BLOCK_SIZE*2)) ]
T = [(x,y), (x+(BLOCK_SIZE*3), y), (x+(BLOCK_SIZE*3), y + BLOCK_SIZE), (x+(BLOCK_SIZE*2), y + BLOCK_SIZE), (x+(BLOCK_SIZE*2), y + (BLOCK_SIZE*2)),
    (x+BLOCK_SIZE, y + (BLOCK_SIZE*2)), (x+BLOCK_SIZE, y + BLOCK_SIZE), (x, y + BLOCK_SIZE)  ]

def getShape(n : int, gameSurface):
    drawT(gameSurface)
    
def getNextShape(n : int, nextPieceSurface):
    pass

def rotateShape(shape: pygame.Rect):
    pass

def drawO(gameSurface):
    #yellow
    pygame.draw.polygon(gameSurface, (255,255,0), O)
    
def drawI(gameSurface):
    #blue
    pygame.draw.polygon(gameSurface, (0, 0,255), I)

def drawS(gameSurface):
    #red
    pygame.draw.polygon(gameSurface, (255, 0,0), S)

def drawZ(gameSurface):
    #green
    pygame.draw.polygon(gameSurface, (0, 255,0), Z)

def drawL(gameSurface):
    #orange
    pygame.draw.polygon(gameSurface, (255, 165,0), L)

def drawJ(gameSurface):
    #pink
    pygame.draw.polygon(gameSurface, (255, 105,180), J)

def drawT(gameSurface):
    #purple
    pygame.draw.polygon(gameSurface, (138,43,226), T)
