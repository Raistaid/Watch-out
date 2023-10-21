from pygame import*
from random import randint
from time import time as timer

font.init()
font1 = font.SysFont('Arial',80)
lose = font1.render('Проигрыш!',True,(252, 255, 56))
font2 = font.SysFont('Arial',36)

img_back = 'polyana.jpg'
img_hero = 'volk.png'
img_enemy1 = 'apple.png'
img_enemy2 = 'pear.png'

score = 0
lost = 0
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost+1

win_width = 700
win_height = 500
display.set_caption('Watch_out!')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),(win_width, win_height))
wolk = Player(img_hero, 5, win_height-130, 120, 120, 10)

apples = sprite.Group()
for i in range(1,6):
    apple = Enemy(img_enemy1,randint(80, win_width-80),-40,80,50,randint(1,5))
    apples.add(apple)

pears = sprite.Group()
for i in range(1,3):
    pear = Enemy(img_enemy2,randint(30, win_width-30),-40,80,50,randint(1,5))
    pears.add(pear)

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        wolk.update()
        apples.update()
        pears.update()
        wolk.reset()
        apples.draw(window)
        pears.draw(window)
        collides = ()
        for c in collides:
            score = score+1
            apple = Enemy(img_enemy1, randint(80,win_width-80),-40,80,50, randint(1,5))
            apples.add(apple)
        if sprite.spritecollide(wolk,apples,False) or sprite.spritecollide(wolk,pears,False):
            sprite.spritecollide(wolk,apples,True)
            sprite.spritecollide(wolk,pears,True)
            life = life-1
        if life == 0:
            finish = True
            window.blit(lose,(140,200))
        if life == 3:
            life_color = (0,150,0)
        if life == 2:
            life_color = (150,150,0)
        if life == 1:
            life_color = (150,0,0)
        text_chet = font2.render('Счет: '+str(lost),1,(255,255,255))
        window.blit(text_chet,(10,120))
        text_life = font2.render(str(life),1,life_color)
        window.blit(text_life,(140,160))
        text_life2 = font2.render('Жизни:',1,(255,255,255))
        window.blit(text_life2,(10,160))
        display.update()

    else:
        finish = False
        score = 0
        lost = 0
        life = 3
        for m in apples:
            m.kill()
        for a in pears:
            a.kill()
        time.delay(3000)
        for i in range(1,6):
            apple = Enemy(img_enemy1,randint(80,win_width-80),-40,80,50,randint(1,5))
            apples.add(apple)
        for i in range(1,3):
            pear = Enemy(img_enemy2,randint(30,win_width-30),-40,80,50,randint(1,7))
            pears.add(pear)
    time.delay(50)
