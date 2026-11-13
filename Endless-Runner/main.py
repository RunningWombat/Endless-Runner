# Car-dodge game with sprites inspiried by the Plants Vs Zombies series
# Controls are the arrow keys to move left and right
# - Resources -

# This video helped with .rect transparency: https://www.youtube.com/watch?v=8_HVdxBqJmE

# Pygame's site helped with many things: https://www.pygame.org/docs/index.html

# Stack overflow was great for learning how to use certain commands, particularly https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

# Mr Bawa and his resources on brightspace helped too :)

# Menu music: https://youtu.be/V9QV9PFVCs8 by Laura Shigihara

# Help menu music: https://youtu.be/GDStetE7aTI by Laura Shigihara

# Play music: https://youtu.be/lr4vi_XAjQQ by Laura Shigihara

# Score sound: https://www.myinstants.com/en/instant/plants-vs-zombies-gulp-85655/

# All visuals are made by me in google drawings

import pygame
import sys
import time
import random
pygame.init()
pygame.mixer.init

music = 1
    
window = pygame.display.set_mode((640, 720))
# Surface is used to make hitboxes transparent
surface = pygame.Surface((640, 720), pygame.SRCALPHA) 

def menu():
    global music
    if music != 0:
        music = 1
    if music == 1:
        pygame.mixer.music.load("Crazy Dave (Intro Theme).mp3")
        pygame.mixer.music.play(loops=10000, start=0.0, fade_ms=0)
    pygame.display.set_caption("- Menu -") 
    back = pygame.image.load("mainmenu.png").convert_alpha() # Main menu background, made by me in Google Drawings

    window.blit(back, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 540 > rat[0] > 355 and 242 > rat[1] > 180:
                    pygame.mixer.music.pause()
                    play()
                    sys.exit()
                    # Starts gameplay 
                elif 520 > rat[0] > 375 and 365 > rat[1] > 295:
                    pygame.mixer.music.pause()
                    help1()
                    sys.exit()
                    # Moves player to help menu
                elif 500 > rat[0] > 365 and 475 > rat[1] > 400:
                    pygame.quit()
                    sys.exit()
                    # Exits the game

# --------------------------------------------------------------------------------------------------------------------

def help1():
    global music
    if music == 1:
        pygame.mixer.music.load("Choose Your Seeds.mp3")
        pygame.mixer.music.play(loops=10000, start=0.0, fade_ms=0)
    pygame.display.set_caption("- Help -") 
    helpback = pygame.image.load("helpmenu.png").convert_alpha() # Help menu background, made by me in Google Drawings

    window.blit(helpback, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Press on the respective plant to learn about it
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 225 > rat[0] > 170 and 430 > rat[1] > 375:
                    warn1()
                    sys.exit()
                elif 330 > rat[0] > 250 and 430 > rat[1] > 375:
                    warn2()
                    sys.exit()
                elif 385 > rat[0] > 330 and 430 > rat[1] > 375:
                    warn3()
                    sys.exit()
                elif 460 > rat[0] > 400 and 430 > rat[1] > 375:
                    warn4()
                    sys.exit()
                elif 320 > rat[0] > 228 and 570 > rat[1] > 507:
                    pygame.mixer.music.load("Choose Your Seeds.mp3")
                    pygame.mixer.music.play(loops=10000, start=0.0, fade_ms=0)
                    music = 1
                    # When music is 1 all sound that would usually play does

                elif 412 > rat[0] > 321 and 570 > rat[1] > 507:
                    pygame.mixer.music.pause()
                    music = 0
                    # When music is 0 all sound that would usually play doesn't

                elif 415 > rat[0] > 225 and 660 > rat[1] > 630:
                    pygame.mixer.music.pause()
                    menu()
                    # Returns to menu

# --------------------------------------------------------------------------------------------------------------------              

def warn1():
    global music
    if music != 0:
        music = 2
    pygame.display.set_caption("- Potatomine Tips -") 
    warnP = pygame.image.load("warnP.png").convert_alpha() # Plant tip page, made by me in Google Drawings

    window.blit(warnP, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 640 > rat[0] > 0 and 720 > rat[1] > 0:
                    help1()
                    sys.exit()
                    # Press anywhere to escape

# --------------------------------------------------------------------------------------------------------------------

def warn2():
    global music
    if music != 0:
        music = 2
    pygame.display.set_caption("- Wallnut Tips -") 
    warnW = pygame.image.load("warnW.png").convert_alpha() # Plant tip page, made by me in Google Drawings

    window.blit(warnW, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 640 > rat[0] > 0 and 720 > rat[1] > 0:
                    help1()
                    sys.exit()
                    # Press anywhere to escape

# --------------------------------------------------------------------------------------------------------------------

def warn3():
    global music
    if music != 0:
        music = 2
    pygame.display.set_caption("- Pepper Tips -") 
    warnPPR = pygame.image.load("warnPPR.png").convert_alpha() # Plant tip page, made by me in Google Drawings

    window.blit(warnPPR, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 640 > rat[0] > 0 and 720 > rat[1] > 0:
                    help1()
                    sys.exit()
                    # Press anywhere to escape

# --------------------------------------------------------------------------------------------------------------------

def warn4():
    global music
    if music != 0:
        music = 2
    pygame.display.set_caption("- Chomper Tips -") 
    warnC = pygame.image.load("warnC.png").convert_alpha() # Plant tip page, made by me in Google Drawings

    window.blit(warnC, (0, 0))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 640 > rat[0] > 0 and 720 > rat[1] > 0:
                    help1()
                    sys.exit()
                    # Press anywhere to escape
        
# --------------------------------------------------------------------------------------------------------------------

def play():
    global music
    global Score
    global Distance
    if music == 1:
        pygame.mixer.music.load("Loonboon.mp3")
        pygame.mixer.music.play(loops=10000, start=0.0, fade_ms=0)
    yp = 230
    y = 0
    y2 = 720
    x = 0
    y3 = -750
    y4 = -1050
    y5 = -1350
    Score = 0
    Distance = 0
    multi = 1
    # List used for randomly picking a lane for obstacles to spawn in
    lanes = [-115, 0, 115]
    # List used for randomly picking an obstacle to spawn in each row
    obstacles = ["potato", "potato", "potato", "potato", "potato" "walnut", "walnut", "walnut", "walnut", "pepper", "chomp", "chomp", "brain"] 
    scoresound = pygame.mixer.Sound("eat.mp3")

    pygame.display.set_caption("- Playing -")
    lawn = pygame.image.load("lawn.png").convert_alpha()  # Playing background, made by me in Google Drawings
    road = pygame.image.load("road.png").convert_alpha()  # Road lines, made by me in Google Drawings
    side1 = pygame.image.load("sidewalkL.png").convert_alpha()  # Left side sidewalk details, made by me in Google Drawings
    side2 = pygame.image.load("sidewalkR.png").convert_alpha()  # Right side sidewalk details, made by me in Google Drawings
    grass1 = pygame.image.load("grassL.png").convert_alpha()  # Left side grass details, made by me in Google Drawings
    grass2 = pygame.image.load("grassR.png").convert_alpha()  # Right side grass details, made by me in Google Drawings
    player = pygame.image.load("zombieS.png").convert_alpha() # Player model, made by me in Google Drawings
    potato = pygame.image.load("potatoS.png").convert_alpha() # Road obstacle, made by me in Google Drawings
    walnut = pygame.image.load("walnutS.png").convert_alpha() # Road obstacle, made by me in Google Drawings
    pepper = pygame.image.load("pepperS.png").convert_alpha() # Road obstacle, made by me in Google Drawings
    chomper = pygame.image.load("chompS.png").convert_alpha() # Road obstacle, made by me in Google Drawings
    brain = pygame.image.load("brain.png") # Death effect, made by me in Google Drawings
    fire = pygame.image.load("fireS.png").convert_alpha() # Road obstacle, made by me in Google Drawings
    flower = pygame.image.load("flowerS.png").convert_alpha() # background decoration, made by me in Google Drawings
    score = pygame.image.load("score.png").convert_alpha() # Score tracker and distance tracker, made by me in Google Drawings 
    
    clock = pygame.time.Clock()
    
    while True:
        Score = int(Score)
        if y3 == -750:
            # Assigns the first row of obstacles the randomly chosen sprite + lane when they leave the screen
            laneC = random.choice(lanes) 
            obstacleC = random.choice(obstacles)
        if y4 == -1050:
             # Assigns the second row of obstacles the randomly chosen sprite + lane when they leave the screen
            laneC2 = random.choice(lanes)
            obstacleC2 = random.choice(obstacles)
        if y5 == -1350:
            # Assigns the third row of obstacles the randomly chosen sprite + lane when they leave the screen
            laneC3 = random.choice(lanes) 
            obstacleC3 = random.choice(obstacles)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        playerhit = pygame.draw.rect(surface, (255, 0, 0), (x+283, yp+435, 75, 20))
        
        window.fill((0, 0, 0)) # These window.fill / blit are the background elements that move down
        
        window.blit(lawn, (0, 0))
        
        window.blit(road, (0, y))
        window.blit(road, (0, y2))
        
        window.blit(side1, (-195, y))
        window.blit(side1, (-195, y2))
        window.blit(side2, (195, y))
        window.blit(side2, (195, y2))
        
        window.blit(grass1, (-272, y))
        window.blit(grass1, (-272, y2))
        window.blit(grass2, (272, y))
        window.blit(grass2, (272, y2))
        
        window.blit(flower, (-272, y))
        window.blit(flower, (-272, y2))
        window.blit(flower, (272, y))
        window.blit(flower, (272, y2))

        window.blit(score, (-244, -329))

        # All these obstacle thingies below use the randomly chosen sprite and lane lists to pick what to spawn
        # All of them have invisible rectangles for hitboxes
        # When the hitboxes interact the player goes to the loss screen (unless they run into the brain)
        
        if obstacleC == "potato":
            window.blit(potato, (laneC, y3))
            potatohit1 = pygame.draw.rect(surface, (255, 0, 0), (laneC+283, y3+370, 75, 40))
            if potatohit1.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
                
        elif obstacleC == "walnut":
            window.blit(walnut, (laneC, y3))
            walnuthit1 = pygame.draw.rect(surface, (255, 0, 0), (laneC+283, y3+350, 75, 150))
            if walnuthit1.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
                
        elif obstacleC == "pepper":
            window.blit(pepper, (laneC, y3))
            if y3 >= 215 and y3 <= 450:
                window.blit(fire, (laneC, 425))
                firehit1 = pygame.draw.rect(surface, (255, 0, 0), (laneC+283, 425, 75, 450))
                if firehit1.colliderect(playerhit):
                    pygame.mixer.music.pause()
                    loss()
                    sys.exit()
                    
        elif obstacleC == "chomp":
            window.blit(chomper, (laneC, y3))
            chomphit1 = pygame.draw.rect(surface, (255, 0, 0), (laneC+283, y3+325, 75, 250))
            if chomphit1.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
                
        elif obstacleC == "brain":
            window.blit(brain, (laneC, y3))
            brainhit1 = pygame.draw.rect(surface, (255, 0, 0), (laneC+283, y3+350, 75, 150))
            if brainhit1.colliderect(playerhit):
                Score += 1 # Increases score amount
                laneC += 1000 # Gets the brain off the screen when collected
                if music == 1:
                    scoresound.play() # Plays sound effect over the music

# Too much text seperator --------------------------------------------------------------------------------------------
            
        if obstacleC2 == "potato":
            window.blit(potato, (laneC2, y4))
            potatohit2 = pygame.draw.rect(surface, (255, 0, 0), (laneC2+283, y4+370, 75, 40))
            if potatohit2.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
                    
        elif obstacleC2 == "walnut":
            window.blit(walnut, (laneC2, y4))
            walnuthit2 = pygame.draw.rect(surface, (255, 0, 0), (laneC2+283, y4+350, 75, 150))
            if walnuthit2.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
                    
        elif obstacleC2 == "pepper":
            window.blit(pepper, (laneC2, y4))
            if y4 >= 215 and y4 <= 450:
                window.blit(fire, (laneC2, 425))
                firehit2 = pygame.draw.rect(surface, (255, 0, 0), (laneC2+283, 425, 75, 450))
                if firehit2.colliderect(playerhit):
                    pygame.mixer.music.pause()
                    loss()
                    sys.exit()
                
        elif obstacleC2 == "chomp":
            window.blit(chomper, (laneC2, y4))
            chomphit2 = pygame.draw.rect(surface, (255, 0, 0), (laneC2+283, y4+325, 75, 250))
            if chomphit2.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()
            
        elif obstacleC2 == "brain":
            window.blit(brain, (laneC2, y4))
            brainhit2 = pygame.draw.rect(surface, (255, 0, 0), (laneC2+283, y4+350, 75, 150))
            if brainhit2.colliderect(playerhit):
                Score += 1 # Increases score amount
                laneC2 += 1000 # Gets the brain off the screen when collected
                if music == 1:
                    scoresound.play() # Plays sound effect over the music

# Too much text seperator --------------------------------------------------------------------------------------------

        if obstacleC3 == "potato": 
            window.blit(potato, (laneC3, y5))
            potatohit3 = pygame.draw.rect(surface, (255, 0, 0), (laneC3+283, y5+370, 75, 40))
            if potatohit3.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()

        elif obstacleC3 == "walnut":
            window.blit(walnut, (laneC3, y5))
            walnuthit3 = pygame.draw.rect(surface, (255, 0, 0), (laneC3+283, y5+350, 75, 150))
            if walnuthit3.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()

        elif obstacleC3 == "pepper":
            window.blit(pepper, (laneC3, y5))
            if y5 >= 215 and y5 <= 450:
                window.blit(fire, (laneC3, 425))
                firehit3 = pygame.draw.rect(surface, (255, 0, 0), (laneC3+283, 425, 75, 450))
                if firehit3.colliderect(playerhit):
                    pygame.mixer.music.pause()
                    loss()
                    sys.exit()

        elif obstacleC3 == "chomp":
            window.blit(chomper, (laneC3, y5))
            chomphit3 = pygame.draw.rect(surface, (255, 0, 0), (laneC3+283, y5+325, 75, 250))
            if chomphit3.colliderect(playerhit):
                pygame.mixer.music.pause()
                loss()
                sys.exit()

        elif obstacleC3 == "brain":
            window.blit(brain, (laneC3, y5))
            brainhit3 = pygame.draw.rect(surface, (255, 0, 0), (laneC3+283, y5+350, 75, 150))
            if brainhit3.colliderect(playerhit):
                Score += 1 # Increases score amount
                laneC3 += 1000 # Gets the brain off the screen when collected
                if music == 1:
                    scoresound.play() # Plays sound effect over the music
                    
        # Moves sprites down, speeds up over time         
        y += 8 * multi 
        y2 += 8 * multi 
        y3 += 8 * multi 
        y4 += 8 * multi 
        y5 += 8 * multi 
        Distance = float(Distance)
        Distance += 0.04 # raises time by 1 about every second (my guess)
                     
        if y >= 720:
            y = -720
        if y2 >= 720:
            y2 = -720
        if y3 >= 450:
            y3 = -450
            # Assigns the first row of obstacles the randomly chosen sprite + lane
            laneC = random.choice(lanes) 
            obstacleC = random.choice(obstacles)
        if y4 >= 450:
            y4 = -450
             # Assigns the second row of obstacles the randomly chosen sprite + lane
            laneC2 = random.choice(lanes)
            obstacleC2 = random.choice(obstacles)
        if y5 >= 450:
            y5 = -450
            # Assigns the third row of obstacles the randomly chosen sprite + lane
            laneC3 = random.choice(lanes) 
            obstacleC3 = random.choice(obstacles)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        button = pygame.key.get_pressed()
        
        if button[pygame.K_LEFT]:
            # Keeps moving the player left while the left key is held down
            x -= 16
                
        if button[pygame.K_RIGHT]:
            # Keeps moving the player right while the right key is held down        
            x += 16

        if x < -115: # Stops player from escaping the leftmost part of the road
            x = -115
        if x > 115: # Stops player from escaping the rightmost part of the road
            x = 115
                
        window.blit(player, (x, yp))
        Score = str(Score) # Converted back to string so it can be put into text
        Distance = round(Distance, 2)
        Distance = str(Distance) # Converted back to string so it can be put into text
        global text1
        global text2
        global font1
        # Scoring and distance numbers in the top left 
        font1 = pygame.font.SysFont("Bevan", 24, bold = True) 
        text1 = font1.render(Score, True, (36, 38, 37))
        text2 = font1.render(Distance, True, (36, 38, 37))
        window.blit(text1,(90, 10))
        window.blit(text2,(90, 40))
        # Multi is applied to the speed of the plants and the background, slowly increasing them
        multi += 0.0002 
        pygame.display.update()
        clock.tick(40)

# --------------------------------------------------------------------------------------------------------------------

def loss():
    global music
    global text2
    global text1
    global Score
    global Distance
    if music == 1:
        pygame.mixer.music.load("lossScream.mp3")
        pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
    pygame.display.set_caption("- Game Over -") 
    loss = pygame.image.load("loss.png").convert_alpha() # Loss screen, made by me in Google Drawings

    # Converted back to string so it can be put into text
    Score = str(Score)
    Distance = float(Distance)
    Distance = round(Distance, 2)
    # Converted back to string so it can be put into text
    Distance = str(Distance)
    font1 = pygame.font.SysFont("Bevan", 38, bold = True)
    text1 = font1.render(Score, True, (36, 38, 37))
    text2 = font1.render(Distance, True, (36, 38, 37))

    window.blit(loss, (0, 0))
    window.blit(text1,(360, 305))
    window.blit(text2,(340, 345))
    pygame.display.flip()

    while True:
        rat = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 410 > rat[0] > 237 and 439 > rat[1] > 420:
                    play()
                    sys.exit()
                    # Starts playing again
                elif 369 > rat[0] > 280 and 489 > rat[1] > 469:
                    menu()
                    sys.exit()
                    # Returns to menu
                elif 360 > rat[0] > 289 and 535 > rat[1] > 515:
                    pygame.quit()
                    sys.exit()
                    # Exits the game

        
menu()
