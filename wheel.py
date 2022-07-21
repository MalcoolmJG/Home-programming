from itertools import count
import random
import time
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Spin the wheel")
#variables
    wheel = pygame.image.load('cute.png')
    arrow = pygame.image.load('arrow.png')
    font = pygame.font.SysFont('Roboto', 50)
    button = pygame.Rect(850, 50, 100, 50) #positionx, positiony, width, height
    speed = 20 #set range steps, spin speed
    angle = 0
    change_screen = 1
    spin = False
    screen = 1
#set amount of rotations, math to show what text 
    upper = random.randrange(540, 5400, speed)
    mod_screen = (upper+90)%360 #rotation starts on the "left" so adding 90 has the mod work from the arrow
    if 0 <= mod_screen <= 120:
        change_screen = 2
    elif 121 <= mod_screen <= 240:
        change_screen = 3
    else:
        change_screen = 4
    print (upper,mod_screen, change_screen)


#"game" loop
    while True:
        if screen == 1:
                win.fill("white")
                #render text/ button
                #win.blit(font.render(str(mod_screen), True, ("black")), (0, 50)) #tick rate 
                win.blit(font.render(str(angle), True, ("black")), (0, 100))  #angle  
                pygame.draw.rect(win, ("blue"), button) #window, colour(0,0,0) Spiin button
                win.blit(font.render("SPiiN!", True, ("black")), (850, 60))   #Spiin text
                #start spinning on button press
                if spin == True:
                    if 0 <= angle <= upper-20: 
                        angle += speed
                    else:
                        #angle = 360
                        spin = False
                        time.sleep(2) 
                        screen = change_screen
                #Spinning wheel
                wheel_spin = pygame.transform.rotate(wheel, angle)
                win.blit(wheel_spin, (500 - int(wheel_spin.get_width() / 2), 500 - int(wheel_spin.get_height() / 2)))
                win.blit(arrow, (0, 0))
        elif screen == 2:
            #win.fill("Blue")
            win.blit(font.render("You Cute", True, ("black")), (0, 0))
        elif screen == 3:
            #win.fill("Blue")
            win.blit(font.render("Nah, You cute", True, ("black")), (0, 0))
        elif screen == 4:
            win.blit(font.render("Drink some water, nerd", True, ("black")), (0, 0))

        for event in pygame.event.get() :
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT :
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 850 and pos[0] < 950 and pos[1] > 50 and pos[1] < 100:
                    spin = True
        # Draws the surface object to the screen.  
        pygame.display.flip() 
        clock.tick(60)

if __name__ == '__main__':
    main()