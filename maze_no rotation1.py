import pygame,math
pygame.init()
screen = pygame.display.set_mode([1200,1000])
#clock = pygame.time.Clock()
maze=pygame.sprite.Sprite()
maze.image=pygame.image.load('maze_geometry10.png')
maze.rect=maze.image.get_rect(center=(600,500))
ball=pygame.sprite.Sprite()
ball.image=pygame.image.load('ball.png')
ball.image=pygame.transform.scale(ball.image,(10,10))

start=pygame.image.load('start.png')
sstart=pygame.transform.scale(start,(50,20))
s_rect=sstart.get_rect(center=(962,950))

finish=pygame.image.load('finish.png')
ffinish=pygame.transform.scale(finish,(50,20))
f_rect=ffinish.get_rect(center=(367,60))


x0,y0=962.5,902.5
dx,dy=5,5
def condition(a):
    global x0,y0
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:  x0=x0-dx*a
    if button[pygame.K_RIGHT]: x0=x0+dx*a
    if button[pygame.K_UP]: y0=y0-dy*a
    if button[pygame.K_DOWN]: y0=y0+dy*a
    #print(x0,y0)
while True:
    screen.fill('gold')
    screen.blit(sstart,s_rect)
    screen.blit(ffinish,f_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    condition(0.5)
    ball.rect=ball.image.get_rect(center=(x0,y0))
    
    screen.blit(ball.image,ball.rect)
    screen.blit(maze.image,maze.rect)
    result=pygame.sprite.collide_mask(maze,ball)
    if result!=None:
        condition(-0.5)
    pygame.display.update()
    #clock.tick(100)
    
