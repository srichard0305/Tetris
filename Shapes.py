import pygame

class Shape:

    x,y = (0,0)
    BLOCK_SIZE = 25
        
    def getShape(self, n : int, gameSurface):
        match n:
            case 0:
                self.drawO(gameSurface)
            case 1:
                self.drawI(gameSurface)
            case 2:
                self.drawS(gameSurface)
            case 3:
                self.drawZ(gameSurface)
            case 4:
                self.drawL(gameSurface)
            case 5:
                self.drawJ(gameSurface)
            case 6:
                self.drawT(gameSurface)

    def moveDown(self):
        self.y = self.y + self.BLOCK_SIZE
            
        
    def getNextShape(self, n : int, nextPieceSurface):
        match n:
            case 0:
                self.drawO(nextPieceSurface)
            case 1:
                self.drawI(nextPieceSurface)
            case 2:
                self.drawS(nextPieceSurface)
            case 3:
                self.drawZ(nextPieceSurface)
            case 4:
                self.drawL(nextPieceSurface)
            case 5:
                self.drawJ(nextPieceSurface)
            case 6:
                self.drawT(nextPieceSurface)

    def rotateShape(self, shape: pygame.Rect):
        pass

    def drawO(self, gameSurface):
        #yellow
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(255,255,0), rect1)
        pygame.draw.rect(gameSurface,(255,255,0), rect2)
        pygame.draw.rect(gameSurface,(255,255,0), rect3)
        pygame.draw.rect(gameSurface,(255,255,0), rect4)
        pygame.draw.rect(gameSurface,(200,200,0), rect1, 1)
        pygame.draw.rect(gameSurface,(200,200,0), rect2, 1)
        pygame.draw.rect(gameSurface,(200,200,0), rect3, 1)
        pygame.draw.rect(gameSurface,(200,200,0), rect4, 1)
       
        
    def drawI(self, gameSurface):
        #blue
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + (self.BLOCK_SIZE*2 ), self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x, self.y + + (self.BLOCK_SIZE*3) , self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(0, 0,255), rect1)
        pygame.draw.rect(gameSurface,(0, 0,255), rect2)
        pygame.draw.rect(gameSurface,(0, 0,255), rect3)
        pygame.draw.rect(gameSurface,(0, 0,255), rect4)
        pygame.draw.rect(gameSurface,(0, 0,200), rect1, 1)
        pygame.draw.rect(gameSurface,(0, 0,200), rect2, 1)
        pygame.draw.rect(gameSurface,(0, 0,200), rect3, 1)
        pygame.draw.rect(gameSurface,(0, 0,200), rect4, 1)

    def drawS(self, gameSurface):
        #red
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x - self.BLOCK_SIZE, self.y + + self.BLOCK_SIZE , self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(255, 0,0), rect1)
        pygame.draw.rect(gameSurface,(255, 0,0), rect2)
        pygame.draw.rect(gameSurface,(255, 0,0), rect3)
        pygame.draw.rect(gameSurface,(255, 0,0), rect4)
        pygame.draw.rect(gameSurface,(200, 0,0), rect1, 1)
        pygame.draw.rect(gameSurface,(200, 0,0), rect2, 1)
        pygame.draw.rect(gameSurface,(200, 0,0), rect3, 1)
        pygame.draw.rect(gameSurface,(200, 0,0), rect4, 1)
   

    def drawZ(self, gameSurface):
        #green
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x - self.BLOCK_SIZE, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(0, 255,0), rect1)
        pygame.draw.rect(gameSurface,(0, 255,0), rect2)
        pygame.draw.rect(gameSurface,(0, 255,0), rect3)
        pygame.draw.rect(gameSurface,(0, 255,0), rect4)
        pygame.draw.rect(gameSurface,(0, 200,0), rect1, 1)
        pygame.draw.rect(gameSurface,(0, 200,0), rect2, 1)
        pygame.draw.rect(gameSurface,(0, 200,0), rect3, 1)
        pygame.draw.rect(gameSurface,(0, 200,0), rect4, 1)
        

    def drawL(self, gameSurface):
        #orange
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + (self.BLOCK_SIZE*2), self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y + (self.BLOCK_SIZE*2), self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(255, 165,0), rect1)
        pygame.draw.rect(gameSurface,(255, 165,0), rect2)
        pygame.draw.rect(gameSurface,(255, 165,0), rect3)
        pygame.draw.rect(gameSurface,(255, 165,0), rect4)
        pygame.draw.rect(gameSurface,(200, 110,0), rect1, 1)
        pygame.draw.rect(gameSurface,(200, 110,0), rect2, 1)
        pygame.draw.rect(gameSurface,(200, 110,0), rect3, 1)
        pygame.draw.rect(gameSurface,(200, 110,0), rect4, 1)
        

    def drawJ(self, gameSurface):
        #pink
        rect1 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x, self.y + (self.BLOCK_SIZE*2), self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x - self.BLOCK_SIZE, self.y + (self.BLOCK_SIZE*2), self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(255, 105,180), rect1)
        pygame.draw.rect(gameSurface,(255, 105,180), rect2)
        pygame.draw.rect(gameSurface,(255, 105,180), rect3)
        pygame.draw.rect(gameSurface,(255, 105,180), rect4)
        pygame.draw.rect(gameSurface,(200, 50,125), rect1, 1)
        pygame.draw.rect(gameSurface,(200, 50,125), rect2, 1)
        pygame.draw.rect(gameSurface,(200, 50,125), rect3, 1)
        pygame.draw.rect(gameSurface,(200, 50,125), rect4, 1)


    def drawT(self, gameSurface):
        #purple
        rect1 = pygame.Rect(self.x - self.BLOCK_SIZE, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect2 = pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect3 = pygame.Rect(self.x + self.BLOCK_SIZE, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        rect4 = pygame.Rect(self.x, self.y + self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
        pygame.draw.rect(gameSurface,(138,43,226), rect1)
        pygame.draw.rect(gameSurface,(138,43,226), rect2)
        pygame.draw.rect(gameSurface,(138,43,226), rect3)
        pygame.draw.rect(gameSurface,(138,43,226), rect4)
        pygame.draw.rect(gameSurface,(73, 0,171), rect1, 1)
        pygame.draw.rect(gameSurface,(73, 0,171), rect2, 1)
        pygame.draw.rect(gameSurface,(73, 0,171), rect3, 1)
        pygame.draw.rect(gameSurface,(73, 0,171), rect4, 1)

