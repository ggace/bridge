import pygame
import random
import pyautogui

pygame.init()

count = 0
obstacles = []

limit = 5

def gameStart():
    global count
    global obstacles
    global limit
    print("----- new game -----")

    

    done = False

    size  = [800,600]
    screen= pygame.display.set_mode(size)


    start = [0, 100, 140, 400]
    end =   [650, 100, 140, 400]

    

    user = [70, 300]
    userLocation = 0

    ispressed = False

    pause = False
    successPause = False

    myFont = pygame.font.SysFont( "arial", 30, True, False)
    fail = myFont.render("Fail (SPACE BAR: newgame, ESC : exit)", False, (255,0,0))
    success = myFont.render("Success (SPACE BAR: newgame, ESC : exit)", False, (0,255,0))
    

    
    if count == limit:
        obstacles = []
        count = 0

    if count == 0:
        for i in range(10):
            oneIsReal = random.choice([True, False])
            
            obstacles.append({'location' : [50*i + 150,250,40,40], 'isReal' : oneIsReal, 'color' : (255,255,255)})
            obstacles.append({'location' : [50*i + 150,310,40,40], 'isReal' : not oneIsReal, 'color' : (255,255,255)})
    
    countFont = myFont.render(f"COUNT : {count}", False, (255,255,255))
    while not done:
        screen.fill((20,20,20))
        
        for event in pygame.event.get():# User did something
            if event.type == pygame.QUIT:# If user clicked close
                done=True
            elif event.type == pygame.KEYDOWN:# If user release what he pressed.
                ispressed = True
                if event.key == pygame.K_ESCAPE:
                    a = pyautogui.confirm('Do you want to exit from this game?', buttons=['yes', 'no'])
                    if a == 'yes':
                        return ''


                if(pause):
                    
                    if event.key == pygame.K_SPACE:
                        count += 1
                        
                        return 'newGame'
                
                if(successPause):
                    
                    if event.key == pygame.K_SPACE:
                        obstacles = []
                        count = 0
                        
                        return 'newGame'
                    
                
                if(not pause and not successPause):
                    if(user[0] >=  600):
                        user = [650 + 70, 300]

                        successPause = True
                    elif(ispressed):
                        if event.key == pygame.K_UP:
                            userLocation += 1
                            user = [50*userLocation + 150 - 30, 250 + 20]
                            if userLocation != 0:
                                
                                if not obstacles[(userLocation-1)*2]['isReal']:
                                    obstacles[(userLocation-1)*2]['color'] = (20, 20, 20)
                                    pause = True
                        elif event.key == pygame.K_DOWN:
                            userLocation += 1
                            user = [50*userLocation + 150 - 30, 310 + 20]
                            if userLocation != 0:
                                
                                if not obstacles[(userLocation-1)*2+1]['isReal']:
                                    obstacles[(userLocation-1)*2+1]['color'] = (20, 20, 20)
                                    pause = True
                    
        for obstacle in obstacles:
            pygame.draw.rect(screen, obstacle['color'], obstacle['location'])
            pygame.draw.rect(screen, (0,0,0), obstacle['location'], 2)
        pygame.draw.rect(screen, (255,255,255), start)
        pygame.draw.rect(screen, (0,0,0), start, 2)

        pygame.draw.rect(screen, (255,255,255), end)
        pygame.draw.rect(screen, (0,0,0), end, 2)

        pygame.draw.circle(screen, (255,0,0), user, 10)
        pygame.draw.circle(screen, (0,0,0), user, 10, 1)
        
        fail_Rect = fail.get_rect()
        fail_Rect.centerx = round(800 / 2)
        fail_Rect.y = 50

        success_Rect = success.get_rect()
        success_Rect.centerx = round(800 / 2)
        success_Rect.y = 50

        count_Rect = countFont.get_rect()
        count_Rect
        count_Rect.y = 50

        if pause:
            screen.blit(fail, fail_Rect)
        elif successPause:
            screen.blit(success, success_Rect)
        screen.blit(countFont, (0, 0))
        pygame.display.flip()
        
        ispressed = False

    
while(gameStart() == 'newGame'):
    print("----- end -----")
    

pygame.quit()