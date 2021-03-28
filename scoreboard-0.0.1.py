import pygame
import datetime

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Scoreboard')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()
crashed = False

timer_sec = 120
timer_d_min = 10
timer_d_sec = 0

font = pygame.font.Font("alarm_clock.ttf", 200)
font2 = pygame.font.Font(None, 80)
font3 = pygame.font.Font(None, 40)

#create timer text label
font_background = white
mm = font.render("00:00", True, red)
mm_rect = mm.get_rect()
mm_rect.centerx, mm_rect.centery = 400, 140

#create placar label
p = font2.render("PLACAR", True, white)
p_rect = p.get_rect()
p_rect.centerx, p_rect.centery = 400, 280

#create scores text label
s1 = font.render("00", True, blue)
s1_rect = s1.get_rect()
s1_rect.centerx, s1_rect.centery = 200, 420

s2 = font.render("00", True, blue)
s2_rect = s2.get_rect()
s2_rect.centerx, s2_rect.centery = 600, 420

e1 = font3.render("EQUIPE 1", True, white)
e1_rect = e1.get_rect()
e1_rect.centerx, e1_rect.centery = 180, 520

e2 = font3.render("EQUIPE 2", True, white)
e2_rect = e1.get_rect()
e2_rect.centerx, e2_rect.centery = 590, 520

# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1                                                
pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds

gameDisplay.fill(black)

gameDisplay.blit(mm, mm_rect)
gameDisplay.blit(p, p_rect)
gameDisplay.blit(s1, s1_rect)
gameDisplay.blit(s2, s2_rect)
gameDisplay.blit(e1, e1_rect)
gameDisplay.blit(e2, e2_rect)
pygame.display.update()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == timer:    # checks for timer event
            if timer_sec > 0:
                timer_sec -= 1
                formatted = str(datetime.timedelta(seconds=timer_sec))[2:7]
                mm = font.render(formatted, True, red)               
            else:
                pygame.time.set_timer(timer, 0)    # turns off timer event

    gameDisplay.fill(black)

    gameDisplay.blit(mm, mm_rect)
    gameDisplay.blit(p, p_rect)
    gameDisplay.blit(s1, s1_rect)
    gameDisplay.blit(s2, s2_rect)
    gameDisplay.blit(e1, e1_rect)
    gameDisplay.blit(e2, e2_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()