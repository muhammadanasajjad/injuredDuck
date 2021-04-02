import pygame
import tkinter

pygame.init()

winWidth = 800
winHeight = 500

win = pygame.display.set_mode((winWidth, winHeight))

pygame.display.set_caption("Injured Duck")

DuckStanding_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckStanding1.png")
DuckStepLeft_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckStepLeft1.png")
DuckStepRight_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckStepRight1.png")
DuckStartFlap_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckStartFlap1.png")
DuckFlapGround_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckFlapGround1.png")
DuckFlap_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckFlap1.png")
DuckFloating_1 = pygame.image.load(r"C:\Users\muham\Desktop\Anas\Python\InjuredDuck\DuckFloating1.png")

x = 50
y = 250
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 7

startingY = 3

# Functions

def movement():
    global x
    global y
    global isJump

    # Movement with Arrow keys
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
            x = max(x, 0)
        if keys[pygame.K_RIGHT] and x < winWidth - width:
            x += vel
            x = min(x, winWidth - width)
        if keys[pygame.K_DOWN] and y < winHeight - height:
            y += vel
            y = min(y, winHeight - height)
        if keys[pygame.K_SPACE]:
            isJump = True

    # Movement with WASD
    if keys[pygame.K_a] and x > 0:
        x -= vel
        x = max(x, 0)
            
    if keys[pygame.K_d] and x < winWidth:
        x += vel
        x = min(x, winWidth - width)
        
    if keys[pygame.K_s] and y < winHeight:
        y += vel
        y = min(y, winHeight - height)



def jump():
    global jumpCount
    global y
    global x
    global isJump
    global startingY
    global vel
    
    # Jumping
    if jumpCount >= -7:
        neg = 1
        normal = True
        if jumpCount < 0:
            neg = -1
        if keys[pygame.K_UP] or keys[pygame.K_w] and jumpCount < 0 and y < startingY:
            normal = False
            y -= (jumpCount ** 2) * neg
            jumpCount -= 0.15
            vel = 10
        if normal:
            y -= (jumpCount ** 2) * neg
            jumpCount -= 1
            vel = 7
        if y > startingY:
            y = startingY
    else: 
        jumpCount = 7
        isJump = False
        normal = True
        vel = 5

    # Moving while jumping
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        x = max(x, 0)

    if keys[pygame.K_RIGHT] and x < winWidth - width:
        x += vel
        x = min(x, winWidth - width)

    if keys[pygame.K_a] and x > 0:
        x -= vel
        x = max(x, 0)
        
    if keys[pygame.K_d] and x < winWidth:
        x += vel
        x = min(x, winWidth - width)


# Game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()

    if not isJump:
        movement()

        if keys[pygame.K_SPACE]:
            startingY = y
            isJump = True
        
    else:
        jump()

      
    
    win.fill((0, 0, 0))
    win.blit(DuckStanding_1, (x, y))
    pygame.display.update()

pygame.quit()
