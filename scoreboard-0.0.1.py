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
# dark shade of the button
color_dark = (100,100,100)

clock = pygame.time.Clock()
crashed = False
playing = False

timer_sec = 0

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

start_btn_text = font3.render("Iniciar", True, white)
pause_btn_text = font3.render("Parar", True, white)


# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1                                                
pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds

def handle_add_time(seconds):
    print(seconds)
    global timer_sec, mm
    timer_sec += seconds
    formatted = str(datetime.timedelta(seconds=timer_sec))[2:7]
    mm = font.render(formatted, True, red)
    timer = pygame.USEREVENT + 1                                                
    pygame.time.set_timer(timer, 1000)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == timer:    # checks for timer event
            print(playing)
            if timer_sec > 0:
                if playing:
                    timer_sec -= 1
                    formatted = str(datetime.timedelta(seconds=timer_sec))[2:7]
                    mm = font.render(formatted, True, red)               
            else:
                pygame.time.set_timer(timer, 0)    # turns off timer event
                playing = False
        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
            if 670 <= mouse[0] <= 670+140 and 120 <= mouse[1] <= 120+40 and timer_sec > 0:
                if playing == False:
                    playing = True
                else:
                    playing = False
            #if the mouse is clicked on the -1 button
            if 52 <= mouse[0] <= 52+40 and 63 <= mouse[1] <= 63+50 and timer_sec > 60 and playing == False:
                handle_add_time(-60)
            #if the mouse is clicked on the +1 button
            if 52 <= mouse[0] <= 52+40 and 113 <= mouse[1] <= 113+50 and playing == False:
                handle_add_time(60)
            #if the mouse is clicked on the +1 button
            if 52 <= mouse[0] <= 52+40 and 163 <= mouse[1] <= 163+50 and playing == False:
                handle_add_time(300)

    gameDisplay.fill(black)
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(gameDisplay,color_dark,[52,63,50,40])
    gameDisplay.blit(font3.render("-1", True, white) , (65,70))
    pygame.draw.rect(gameDisplay,color_dark,[52,113,50,40])
    gameDisplay.blit(font3.render("+1", True, white) , (60,120))
    pygame.draw.rect(gameDisplay,color_dark,[52,163,50,40])
    gameDisplay.blit(font3.render("+5", True, white) , (60,170))

    # Play / Pause button
    pygame.draw.rect(gameDisplay,color_dark,[670,120,100,40])
    # superimposing the text onto our button
    if playing:
        gameDisplay.blit(pause_btn_text , (670+15,126))
    else:
        gameDisplay.blit(start_btn_text , (670+9,126))

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