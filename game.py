import pygame


# Must be in every pygame
pygame.init()

# Screen Width and Height
screen_width = 500
screen_height = 480

# game Speed in MilliSeconds
clock = pygame.time.Clock()
frame_rate = 27

# boots window 
win = pygame.display.set_mode((screen_height, screen_height))

# Sets title of Window
pygame.display.set_caption("First Game")


# loads char sprites to use and defines them to vars (They are lists)
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
bg = pygame.image.load('bg.jpg')

# Character Class
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing  = True

    def draw(self, win):

        # Drawing the char (Window "Surface", Color, Rect(position/dimentions))(Cycles every 3 frames to a new sprite)
        if self.walkCount + 1 >= frame_rate:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                man.walkCount += 1
                pygame.display.update()
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                pygame.display.update()

        # When "Standing still" we are updating our sprite to be the first image of the animation in the direction we left off in
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
                pygame.display.update()
            else:
                win.blit(walkLeft[0], (self.x, self.y))
                pygame.display.update()

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    # Draws a Circle
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



def reDrawDisplay():
    global walkCount

    # Draws picture bg at position (0,0) .blit((image), (x,y))
    win.blit(bg, (0,0))

    # method of man to draw object
    man.draw(win)

    #Draws each bullet in array
    for bullet in bullets:
        bullet.draw(win)
    
    # updates display 
    pygame.display.update()

# Making an object 
man = player(300, 410, 64, 64)
bullets = []
# Main Loop
run = True
while run:
    # game clock (frame_rate)
    clock.tick(frame_rate)
    
    # checking for events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    # Checks for a key pressed and adds it to a list every loop  
    keys = pygame.key.get_pressed()

    #On Space Press, if < 5 bullets then make a new object(bullet) and append on to array of bullets
    if keys[pygame.K_SPACE]:
        
        #Will set where the bullet will travel too in the x-Direction.
        if man.left:
            facing = -1
        else:
            facing = 1

        # Creates Projectile at center mass of man with a limit of 5
        if len(bullets) < 5:
            bullets.append(projectile((round(man.x + man.width // 2)), round(man.y + man.height // 2), 6, (0,0,0),facing))
    
    # +/- to x/y determined buy key press and scaled by Vel/ and makes sure the character can not move off the screen.
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.left = False
        man.right = True
        man.standing = False
        man.x += man.vel

    else:
        man.standing = True
        man.walkCount = 0

    # checks for jump, if jump then isJump will be true
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    # jumpcount is the frame at which the player will preform a jump.
    # At 10 that means an inital jump is made.
    # As jumpCount lowers so does the speed at witch the player moves
    # If jumpCount goes below zero, then are neg var will switch to a negative number
    #       Moving the player back down to the starting y value at witch the event occured.
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    reDrawDisplay()



pygame.quit()

