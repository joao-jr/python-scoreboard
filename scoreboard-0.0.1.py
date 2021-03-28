import pygame
import datetime

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()
crashed = False

timer_sec = 120
timer_d_min = 10
timer_d_sec = 0


#create timer text label
font = pygame.font.Font("alarm_clock.ttf", 150)
font_background = white
mm = font.render("00", True, red)
mm_rect = mm.get_rect()
mm_rect.centerx, mm_rect.centery = 260, 160

ss = font.render(":00", True, red)
ss_rect = ss.get_rect()
ss_rect.centerx, ss_rect.centery = 540, 160

#create placar label
font2 = pygame.font.Font(None, 80)
p = font2.render("PLACAR", True, white)
p_rect = p.get_rect()
p_rect.centerx, p_rect.centery = 400, 310

#create scores text label
s1 = font.render("00", True, blue)
s1_rect = s1.get_rect()
s1_rect.centerx, s1_rect.centery = 200, 440

s2 = font.render("00", True, blue)
s2_rect = s2.get_rect()
s2_rect.centerx, s2_rect.centery = 600, 440

# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1                                                
pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds

gameDisplay.fill(black)

gameDisplay.blit(mm, mm_rect)
gameDisplay.blit(ss, ss_rect)
gameDisplay.blit(p, p_rect)
gameDisplay.blit(s1, s1_rect)
gameDisplay.blit(s2, s2_rect)
pygame.display.update()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == timer:    # checks for timer event
            print(timer_sec)
            # if timer_sec > 0 and timer_sec > 60:
            #     print("Entrei aqui > 60")
            #     timer_sec -= 1
            #     timer_d_min = timer_sec / 60
            #     timer_d_sec = 60 % timer_sec
            #     print(timer_d_sec)
            #     mm = font.render("%02d" % timer_d_min, True, red)
            #     ss = font.render(":%02d" % timer_d_sec, True, red)
            # elif timer_sec > 0:
            #     print("Entrei aqui > 0")
            #     timer_sec -= 1
            #     mm = font.render("00", True, red)
            #     ss = font.render(":%02d" % timer_sec, True, red)
            if timer_sec > 0:
                timer_sec -= 1
                formatted = str(datetime.timedelta(seconds=timer_sec))[2:7]
                mm = font.render(formatted, True, red)               
            else:
                pygame.time.set_timer(timer, 0)    # turns off timer event

    gameDisplay.fill(black)

    gameDisplay.blit(mm, mm_rect)
    # gameDisplay.blit(ss, ss_rect)
    gameDisplay.blit(p, p_rect)
    gameDisplay.blit(s1, s1_rect)
    gameDisplay.blit(s2, s2_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()