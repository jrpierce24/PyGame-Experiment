import pygame


# Must be in every pygame
pygame.init()

# boots window 
win = pygame.display.set_mode((500, 500))

# Sets title of Window
pygame.display.set_caption("First Game")

# char attributes, Coult be replaced by a class
x = 50
y = 50
width = 40
height = 60 
vel = 5

run = True
while run:
    # game clock (milisecond)
    pygame.time.delay(100)
    
    # checking for events
    for event in pygame.get():
        if event.type==pygame.QUIT:
            run = False

pygame.quit()

