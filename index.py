import pygame
import random
import pyautogui

#초기화
pygame.init()

count = 0
obstacles = []
#시도 횟수 제한
limit = 4

def gameStart():
    #외부 변수 가져오기
    global count
    global obstacles
    global limit

    #시작
    print("----- new game -----")

    
    #종료 여부 변수
    done = False

    #스크린 구성
    size  = [800,600]
    screen= pygame.display.set_mode(size)

    #게임 시작, 끝 사각형
    start = [0, 100, 140, 400]
    end =   [650, 100, 140, 400]

    #사용자 정보
    user = [70, 300]
    userLocation = 0

    #keydown 트리거
    ispressed = False

    #멈춤 변수
    pause = False
    successPause = False

    #시도 횟수 처리: 변수 초기화
    if count == limit:
        a = pyautogui.confirm('주어진 기회가 끝났습니다.\n게임을 다시 시작하시겠습니까?', buttons=['yes', 'no'])
        if a == 'yes':
            pass
        else:
            b = pyautogui.confirm('주어진 기회가 끝났습니다.\n게임을 끝내시겠습니까?', buttons=['yes', 'no'])
            if b == 'yes':
                return ''
            else:
                return 'newGame'
        obstacles = []
        count = 0
    #시도 횟수 처리: 다리 정보 재설정
    if count == 0:
        for i in range(10):
            oneIsReal = random.choice([True, False])
            
            obstacles.append({'location' : [50*i + 150,250,40,40], 'isReal' : oneIsReal, 'color' : (255,255,255)})
            obstacles.append({'location' : [50*i + 150,310,40,40], 'isReal' : not oneIsReal, 'color' : (255,255,255)})

    #text 노출
    myFont = pygame.font.SysFont( "arial", 30, True, False)
    fail = myFont.render("Fail (SPACE BAR: continue, ESC : exit)", False, (255,0,0))
    success = myFont.render("Success (SPACE BAR: continue, ESC : exit)", False, (0,255,0))
    countFont = myFont.render("<> " * (limit-count), False, (255,255,255))

    #게임 로직
    while not done:
        #회색 채움
        screen.fill((20,20,20))
        
        #이벤트 처리
        for event in pygame.event.get():
            #게임 종료
            if event.type == pygame.QUIT:
                done=True
            #keydown 시 실행
            elif event.type == pygame.KEYDOWN:
                #keydown 트리거 활성화
                ispressed = True

                #esc 나가기
                if event.key == pygame.K_ESCAPE:
                    a = pyautogui.confirm('게임을 끝내시겠습니까?', buttons=['yes', 'no'])
                    if a == 'yes':
                        return ''

                #게임 진행
                if(pause):
                    
                    if event.key == pygame.K_SPACE:
                        count += 1
                        
                        return 'newGame'
                #게임 재시작 및 초기화
                if(successPause):
                    
                    if event.key == pygame.K_SPACE:
                        obstacles = []
                        count = 0
                        
                        return 'newGame'
                    
                #게임 진행 순서
                if(not pause and not successPause):
                    #끝에 도달했을때
                    if(user[0] >=  600):
                        user = [650 + 70, 300]
                        successPause = True
                    #keydown 트리거 활성화 시
                    elif(ispressed):
                        #위쪽 화살표 : 위로 이동
                        if event.key == pygame.K_UP:
                            #user 정보 업데이트
                            userLocation += 1
                            user = [50*userLocation + 150 - 30, 250 + 20]

                            #떨어짐 처리
                            if userLocation != 0:
                                
                                if not obstacles[(userLocation-1)*2]['isReal']:
                                    obstacles[(userLocation-1)*2]['color'] = (20, 20, 20)
                                    pause = True
                        #아래쪽 화살표 : 아래로 이동
                        elif event.key == pygame.K_DOWN:
                            #user 정보 업데이트
                            userLocation += 1
                            user = [50*userLocation + 150 - 30, 310 + 20]

                            #떨어짐 처리
                            if userLocation != 0:
                                
                                if not obstacles[(userLocation-1)*2+1]['isReal']:
                                    obstacles[(userLocation-1)*2+1]['color'] = (20, 20, 20)
                                    pause = True
        #다리 보여주기     
        for obstacle in obstacles:
            pygame.draw.rect(screen, obstacle['color'], obstacle['location'])
            pygame.draw.rect(screen, (0,0,0), obstacle['location'], 2)
        #시작 지점 보여주기
        pygame.draw.rect(screen, (255,255,255), start)
        pygame.draw.rect(screen, (0,0,0), start, 2)
        #끝 지점 보여주기
        pygame.draw.rect(screen, (255,255,255), end)
        pygame.draw.rect(screen, (0,0,0), end, 2)
        #사용자 보여주기
        pygame.draw.circle(screen, (255,0,0), user, 10)
        pygame.draw.circle(screen, (0,0,0), user, 10, 1)
        #실패 text
        fail_Rect = fail.get_rect()
        fail_Rect.centerx = round(800 / 2)
        fail_Rect.y = 50
        #성공text
        success_Rect = success.get_rect()
        success_Rect.centerx = round(800 / 2)
        success_Rect.y = 50
        #시도 횟수 text
        count_Rect = countFont.get_rect()
        count_Rect
        count_Rect.y = 50
        #실패시 : 실패 text 보여줌
        if pause:
            screen.blit(fail, fail_Rect)
        #성공시 : 성공 text 보여줌
        elif successPause:
            screen.blit(success, success_Rect)
        #시도 횟수 text 보여줌
        screen.blit(countFont, (0, 0))

        #업데이트
        pygame.display.flip()
        #keydown 트리거 비활성화
        ispressed = False

#안내
pyautogui.alert(f"기회는 {limit}번이며 위쪽 화살표, 아래쪽 화살표를 눌러서 전진할 수 있습니다.\n숙지하셨으면 확인을 눌러주세요");    

#게임 루프
while(gameStart() == 'newGame'):
    print("----- end -----")
    
#게임 종료
pygame.quit()