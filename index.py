import pygame

pygame.init()

done = False

size  = [800,600]
screen= pygame.display.set_mode(size)


start = [0, 100, 140, 400]

obstacles = []

for i in range(10):

    obstacles.append([50*i + 150,325,40,40])
    obstacles.append([50*i + 150,275,40,40])

while not done:
    screen.fill((20,20,20))

    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255,255,255), obstacle)
        pygame.draw.rect(screen, (0,0,0), obstacle, 2)
    pygame.draw.rect(screen, (255,255,255), start)
    pygame.draw.rect(screen, (0,0,0), start, 2)
    
    pygame.display.flip()

    

pygame.quit()