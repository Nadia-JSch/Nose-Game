# import pygame and random modules

import pygame
import random

# initialize the screen to dimensions
pygame.init()

# screen will be 1040 x 680
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Nose Game')

# create the player, enemy and prize with images
playerNose = pygame.image.load("playerNose.png")
enemyBac = pygame.image.load("enemyBac.png")
enemyPink = pygame.image.load("enemyPink.png")
enemyGreen = pygame.image.load("enemyGreen.png")
enemyYellow = pygame.image.load("enemyYellow.png")
prize = pygame.image.load("prizeTissue.png")


# get width and height of the 5 images 
# player
image_height = playerNose.get_height()
image_width = playerNose.get_width()

# enemy bacteria
enemyBac_height = enemyBac.get_height()
enemyBac_width = enemyBac.get_width()

# enemy pink
enemyPink_height = enemyPink.get_height()
enemyPink_width = enemyPink.get_width()

# enemy green
enemyGreen_height = enemyGreen.get_height()
enemyGreen_width = enemyGreen.get_width()

# enemy yellow
enemyYellow_height = enemyYellow.get_height()
enemyYellow_width = enemyYellow.get_width()

# the prize
prize_height = prize.get_height()
prize_width = prize.get_width()

# use a variable for the positions of the player, enemies and prize for later
playerXPosition = 100
playerYPosition = 50

# make the enemy (bacteria) start off the screem at a random position
enemyBacXPosition =  screen_width
enemyBacYPosition =  random.randint(0, screen_height - enemyBac_height)

# make the enemy (pink) start off the screem at a random position
enemyPinkXPosition =  screen_width
enemyPinkYPosition =  random.randint(0, screen_height - enemyPink_height)

# make the enemy (green) start off the screem at a random position
enemyGreenXPosition =  screen_width
enemyGreenYPosition =  random.randint(0, screen_height - enemyGreen_height)

# make the enemy (yellow) start off the screem at a random position
enemyYellowXPosition =  screen_width
enemyYellowYPosition =  random.randint(0, screen_height - enemyYellow_height)

# make the prize start off the screem at a random position
prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - prize_height)


# set up down and left right keys
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# the main game loop, first clear screen then render images with .blit
while 1:
    # clear the screen
    screen.fill(0)
    # draw image to screen at position x, y
    screen.blit(playerNose, (playerXPosition, playerYPosition))
    screen.blit(enemyBac, (enemyBacXPosition, enemyBacYPosition))
    screen.blit(enemyPink, (enemyPinkXPosition, enemyPinkYPosition))
    screen.blit(enemyGreen, (enemyGreenXPosition, enemyGreenYPosition))
    screen.blit(enemyYellow, (enemyYellowXPosition, enemyYellowYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # update the screen
    pygame.display.flip()

    # loops through in game events
    for event in pygame.event.get():

        # check if user exited the game, if so the exit program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # check if user preses a key down
        if event.type == pygame.KEYDOWN:
            #check which key pressed
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # check if user stops pressing a key
        if event.type == pygame.KEYUP:
            # check which key released
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # change player position depending on key pressed
    if keyUp == True:
        # stop player moving out of screen
        if playerYPosition > 0:
            # move up (Y axis and in negative direction)
            playerYPosition -= 1

    if keyRight == True:
        # Keep player on the screen
        if playerXPosition  < screen_width - image_width:
            # move right (X axis in negative direction)
            playerXPosition += 1

    if keyDown == True:
        # stop player moving out of screen
        if playerYPosition < screen_height - image_height:
            # move down (Y axis and positive direction)
            playerYPosition += 1

    if keyLeft == True:
        #keep player on the screen
        if playerXPosition > 0:
            # move left (X axis and positive direction
            playerXPosition -= 1

    # create bounding box for player to check for collisions
    playerBox = pygame.Rect(playerNose.get_rect())
    # update playerBox position to match the player's position
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # create a bounding box for enemy BAC to detect collision
    enemyBacBox = pygame.Rect(enemyBac.get_rect())
    enemyBacBox.top = enemyBacYPosition
    enemyBacBox.left = enemyBacXPosition

    # create a bounding box for PINK enemy to detect collision
    enemyPinkBox = pygame.Rect(enemyPink.get_rect())
    enemyPinkBox.top = enemyPinkYPosition
    enemyPinkBox.left = enemyPinkXPosition

    # create a bounding box for GREEN enemy to detect collision
    enemyGreenBox = pygame.Rect(enemyGreen.get_rect())
    enemyGreenBox.top = enemyGreenYPosition
    enemyGreenBox.left = enemyGreenXPosition

    # create a bounding box for YELLOW enemy to detect collision
    enemyYellowBox = pygame.Rect(enemyYellow.get_rect())
    enemyYellowBox.top = enemyYellowYPosition
    enemyYellowBox.left = enemyYellowXPosition

    # create a bounding box for the PRIZE to detect collision
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # check if there's a collision of boxes
    if playerBox.colliderect(enemyBacBox) or playerBox.colliderect(enemyPinkBox):
        print("Oh no! That's not good for your nose....")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyGreenBox) or playerBox.colliderect(enemyYellowBox):
        print("Oh no! Protect your nose next time!")
        pygame.quit()
        exit(0)

    # if the prize passes the screen the player loses too
    if prizeXPosition < 0 - prize_width:
        print("Oh no! Try get the loo paper for your nose next time!")
        pygame.quit()
        exit(0)
    
    # if playerBox collides with the prize the user wins
    if playerBox.colliderect(prizeBox):
        print("Yay! With loo paper comes victory!")
        pygame.quit()
        exit(0)

    # enemies and prize approaches player at different speeds
    enemyBacXPosition -= 0.27
    enemyPinkXPosition -= 0.32
    enemyGreenXPosition -= 0.40
    enemyYellowXPosition -= 0.50
    prizeXPosition -= 0.25


# ---END---

