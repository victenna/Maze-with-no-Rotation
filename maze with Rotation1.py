import pygame,math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1650,900])
ball=pygame.image.load('ball.png')
ball=pygame.transform.scale(ball,(30,30))
start=pygame.image.load('start.png')
sstart=pygame.transform.scale(start,(50,20))
s_rect=sstart.get_rect(center=(300,420))

finish=pygame.image.load('finish.png')
ffinish=pygame.transform.scale(finish,(50,20))
f_rect=ffinish.get_rect(center=(800,420))

GREY=(211,211,211)
class Obstacle():
    def __init__(self):
        super().__init__()
        self.obstacle_image=pygame.image.load('obstacle11.png')
        self.image=self.obstacle_image
        self.rect = self.image.get_rect(center=(800, 450))
        self.angle = 0
        #self.d_angle =0.7
    def rot(self,d_angle):#,angle):
        self.image = pygame.transform.rotate(self.obstacle_image, self.angle)
        self.angle += d_angle
        #self.angle = self.angle % 360
        self.rect = self.image.get_rect(center=self.rect.center)
    def draw(self):
        screen.blit(self.image,self.rect)
obstacle=Obstacle()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=ball
        self.x=300
        self.y=450
        self.rect=self.image.get_rect(center=(self.x,self.y))
    def update(self,a):
        button=pygame.key.get_pressed()
        if button[pygame.K_LEFT]:
            self.x-=a
        if button[pygame.K_RIGHT]:
            self.x+=a
        if button[pygame.K_UP]:
            self.y-=a
        if button[pygame.K_DOWN]:
            self.y+=a
        self.rect=self.image.get_rect(center=(self.x,self.y))
        
    def update1(self,b):
        self.x+=b
        self.x-=b
        self.y+=b
        self.y-=b
        
    
    def draw(self):
        screen.blit(self.image,self.rect)
bball=Ball()
while True:
    screen.fill(GREY)
    screen.blit(sstart,s_rect)
    screen.blit(ffinish,f_rect)
    obstacle.rot(-2)
    obstacle.draw()
    button=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    bball.update(15)
    bball.draw()
    result=pygame.sprite.collide_mask(obstacle,bball)
    print(result)
    if result!=None:
        bball.x,bball.y=300,450
        #bball.update1(-40)
    clock.tick(150)  
    pygame.display.update()
