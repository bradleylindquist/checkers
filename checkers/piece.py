from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, LFC, BLUE, CFC
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
      if self.color == BLUE:
        #CFC
          radius = SQUARE_SIZE//2 - self.PADDING
          pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
          pygame.draw.circle(win, BLUE, (self.x, self.y), radius)
          win.blit(CFC, (self.x - CFC.get_width()//2, self.y - CFC.get_height()//2))
          
          if self.king:
              win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
      else:        
        #LFC
          radius = SQUARE_SIZE//2 - self.PADDING
          pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
          pygame.draw.circle(win, RED, (self.x, self.y), radius)
          win.blit(LFC, (self.x - LFC.get_width()//2, self.y - LFC.get_height()//2))
        
          if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
      