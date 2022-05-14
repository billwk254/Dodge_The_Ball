import pygame
import sys
from ball import Ball
from target import Target

def gameover(screen,dodge_settings):
    """A function that gets called when the balls on the screen collide with the player pointer """
    loop = True
    font = pygame.font.SysFont("Agency FB",100)
    font1 = pygame.font.SysFont("Agency FB", 50)
    text = font.render("Game Over!", True, (230,230,230))
    text1 = font1.render("Press R to try again",True,(0,128,155))
    text2 = font1.render("Press Q to quit", True,(255,0,0))
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameloop(dodge_settings,screen)
        screen.fill(dodge_settings.bg_color)
        text_rect = text.get_rect()
        text_rect.x = dodge_settings.screen_width/2 -180
        text_rect.y =dodge_settings.screen_height/2 -100
        screen.blit(text, text_rect)
        screen.blit(text1,(dodge_settings.screen_width/2 -150,dodge_settings.screen_height - 70))
        screen.blit(text2, (380,50))
        displayscore(dodge_settings,screen)
        pygame.display.update()

def displayscore(dodge_settings,screen):
    """A function that displays the games current score on the screen"""
    font = pygame.font.SysFont("Forte",30)
    scoretext = font.render("Score: " +str(dodge_settings.score),True,(230,230,230))
    screen.blit(scoretext,(10,10))

def close():
    """A function that is called whenever the player """
    pygame.quit()
    sys.exit()

def checkcollision(target ,d ,objtarget):
    """Checks for collisions between the player pointer and the target"""
    pos = pygame.mouse.get_pos()
    dist = ((pos[0] -target[0] - objtarget.w)**2 + (pos[1] -target[1] -objtarget.h)**2)**0.5
    if dist <= d + objtarget.w:
        return True
    return False

def drawplayerpointer(pos,r,dodge_settings,screen):
    """Draws the player pointer onto the screen"""
    pygame.draw.ellipse(screen,dodge_settings.playercolor,(pos[0] -r, pos[1] -r,2*r,2*r))

def gameloop(dodge_settings,screen):
    """The main game loop with logic on how the game handles collisions"""
    pause_collide = ""
    font3 = pygame.font.SysFont("Agency FB", 50)
    text = font3.render("II", True, dodge_settings.yellow)
    text_rect = text.get_rect()
    text_rect.x = 990
    text_rect.y = 5
    loop = True
    pradius = 10
    balls = []
    #Reset the score each time the game starts
    dodge_settings.score = 0

    for i in range(1):
        newball = Ball(pradius +2 ,5,dodge_settings,screen)
        newball.createball()
        balls.append(newball)

    target = Target(dodge_settings,screen)
    target.generateNewCoord()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                pause_collide = text_rect.collidepoint(x,y)
                if pause_collide:
                    pause_menu(dodge_settings,screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    close()
                if event.key == pygame.K_r:
                    gameloop(dodge_settings,screen)

        screen.fill(dodge_settings.bg_color)

        if pause_collide:
            pass
        else:
            for i in range(len(balls)):
                balls[i].move()

            for i in range(len(balls)):
                balls[i].draw()

            for i in range(len(balls)):
                balls[i].collision(pradius)

            playerpos = pygame.mouse.get_pos()
            drawplayerpointer((playerpos[0], playerpos[1]),pradius,dodge_settings,screen)

            collide = checkcollision((target.x ,target.y),pradius,target)
            after_collide(dodge_settings, screen, collide, pradius, target, balls)

            screen.blit(text,text_rect)
            target.draw()
            displayscore(dodge_settings,screen)
        if pause_collide:
            pass
        else:
            pauseflag()
        dodge_settings.clock.tick(60)

def pause_menu(dodge_settings,screen):
    """A function that draws the pause menu onto the screen"""
    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Paused",True,dodge_settings.blue)
    text2 = font.render("Instructions",True,dodge_settings.orange)
    text_rect2 = text2.get_rect()
    text_rect2.x = dodge_settings.screen_width / 2 - 170
    text_rect2.y = dodge_settings.screen_height / 2
    screen.blit(text2,text_rect2)
    text_rect =text.get_rect()
    text_rect.x = dodge_settings.screen_width / 2 - 180
    text_rect.y = dodge_settings.screen_height / 2 - 100
    screen.blit(text,text_rect)
    pygame.display.update()



def after_collide(dodge_settings,screen,collide,pradius,target,balls):
    """Function that generates new balls and moves the target to a new position after a collision with
    the players pointer"""
    if collide:
        dodge_settings.score += 1
        target.generateNewCoord()
    elif dodge_settings.score == 2 and len(balls) == 1:
        newball = Ball(pradius + 2, 5, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 5 and len(balls) == 2:
        newball = Ball(pradius + 2, 6, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 10 and len(balls) == 3:
        newball = Ball(pradius + 2, 7, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 15 and len(balls) == 4:
        newball = Ball(pradius + 2, 8, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 20 and len(balls) == 5:
        newball = Ball(pradius + 2, 9, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 25 and len(balls) == 6:
        newball = Ball(pradius + 2, 10, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 30 and len(balls) == 7:
        newball = Ball(pradius + 2, 11, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 35 and len(balls) == 8:
        newball = Ball(pradius + 2, 12, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 40 and len(balls) == 9:
        newball = Ball(pradius + 2, 13, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 45 and len(balls) == 10:
        newball = Ball(pradius + 2, 14, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()
    elif dodge_settings.score == 50 and len(balls) == 11:
        newball = Ball(pradius + 2, 15, dodge_settings, screen)
        newball.createball()
        balls.append(newball)
        target.generateNewCoord()

def pauseflag():
    """A function called to Refresh the contents on the screen"""
    pygame.display.update()












