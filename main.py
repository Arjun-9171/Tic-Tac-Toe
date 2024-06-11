import pygame
from pygame.locals import *

# from pygame.event import post


pygame.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
line_width = 6
clicked = False
player = 1
pos = (0, 0)
markers = []
game_over = False
winner = 0

for x in range(3):
  row = [0] * 3
  markers.append(row)
  
def draw_board():
  screen.fill("white")
  grid = 'black'
  for x in range(1, 3):
    pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), 3)
    pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), 3)


def draw_markers():
  x_pos = 0
  for x in markers:
    y_pos = 0
    for y in x:
      if y == 1:
        pygame.draw.line(screen, "red", (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
        pygame.draw.line(screen, "red", (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
      if y == -1:
        pygame.draw.circle(screen, "green", (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
      y_pos += 1
    x_pos += 1	
    
again_rectangle = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)
def draw_gameover(winner):
  if winner != 0:
    win_text = "Player " + str(winner) + " wins!"
  else:
    win_text = "The game is a Tie!"
  font = pygame.font.Font(None, 30)
  text = font.render(win_text, True, "black")
  pygame.draw.rect(screen, "blue" , (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
  screen.blit(text, (screen_width // 2 - 75, screen_height // 2 - 50))

  again_text = "Play Again?"
  again_image = font.render(again_text, True, "black")
  pygame.draw.rect(screen, "blue", again_rectangle)
  screen.blit(again_image, (screen_width // 2 - 60, screen_height // 2 + 10))

def check_gameover():
  global game_over
  global winner
  x_pos = 0

  for x in markers:
    #First two if blocks are checking for colums
    if sum(x) == 3:
      game_over = True
      winner = 1
    
    if sum(x) == -3:
      game_over = True
      winner = 2
    #Second set of if blocks are checking for rows
    if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
      game_over = True
      winner = 1

    if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
      game_over = True
      winner = 2
      
    x_pos += 1
    #Third set of if blocks are checking for diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
      game_over = True
      winner = 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
      game_over = True
      winner = 2
    #Checking for Tie
    if game_over == False:
      tie = True
      for x in markers:
        if 0 in x:
          tie = False
      if tie:
        game_over = True
        winner = 0
    
  
  
run = True
while run:
  draw_board()
  draw_markers()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if game_over == False:
      if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
      if event.type == pygame.MOUSEBUTTONUP and clicked == True:
        clicked = False
        pos = pygame.mouse.get_pos()
        cell_x = pos[0] // 100
        cell_y = pos[1] // 100
        if markers[cell_x][cell_y] == 0:
          markers[cell_x][cell_y] = player
          player *= -1
          check_gameover()

  if game_over == True:
    draw_gameover(winner)
    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
      clicked = True
    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
      clicked = False
      pos = pygame.mouse.get_pos()
      if again_rectangle.collidepoint(pos):
        game_over = False
        player = 1
        pos = (0, 0)
        markers = []
        winner = 0
        for x in range(3):
          row = [0] * 3
          markers.append(row)
        
          
          
  pygame.display.update()
pygame.quit()