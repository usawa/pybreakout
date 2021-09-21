#!/bin/env python3
import sys
import time
import random
import pygame

"""
# Ceci fait cela
for a in range (1,11):
    print("table des " + str(a))
    for b in range(1,11):
        c=a*b
        print (str(a)+"*"+str(b)+"="+str(c))


for a in (1,2,3,4,5,6,7,8,9,10):
    print(a)
    for b in range(1,a+1):
        print("*",end='')

    print('')

a = 1
while a <= 10:

    if a==5:
        print(a)
    else:
        print('toto')
    a=(1+a)

import math

# a : base, h : hauteur y : hypoténuse
# y = racine carrée de ( a^2 + h^2)
def hypotenuse(a, h):
    y = math.sqrt(a**2 + h**2)
    return(y)

def aire_triangle(b,h):
    aire = (b*h)/2
    return(aire)

print(hypotenuse(5,4))
print(aire_triangle(5,4))

def perimetre_carre(c):
    perimetre=(c*4)
    return(perimetre)

print(perimetre_carre(9))

def perimetre_rectangle(c1,c2):
    if c1==c2:
        perimetre=perimetre_carre(c1)
    else:
        perimetre=c1*2+c2*2
    return(perimetre)

print(perimetre_rectangle(2,2))

"""
class Brique(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.rect = self.rect.move(self.speed)


class balle(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.my_speed = random.randint(-5,5)
        self.incline = random.randint(1,5)
        self.speed = [ self.my_speed + self.incline, self.my_speed ]

        self.image = pygame.Surface((16,16), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (8,8), 8)

        #self.image = pygame.image.load("intro_ball.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]

        if self.rect.bottom > height:
            self.kill()

class Raquette(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((64,12), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (200,200,200), (0,0,64,12))

        #self.image = pygame.image.load("intro_ball.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 456


    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if pygame.mouse.get_focused():
            self.rect.x=mouse_x

        if self.rect.left < 0:
            self.rect.x=0
            
        if self.rect.right > width:
            self.rect.x=576


def main():
    print("Dans main") 

    pygame.init()
    clock = pygame.time.Clock()

    FPS = 60
    global width
    global height
    global size
    global all_sprites

    size = width, height = 640, 480

    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    ball_list = [] 
    for nb in range(1,50):
       ball_list.append( balle(  (random.randint(0,255), random.randint(0,255) ,random.randint(0,255) ) , random.randint(0,640),random.randint(0,480)) )

    all_sprites.add(ball_list)

    raquette = Raquette(288)
    all_sprites.add(raquette)

    pygame.mouse.set_visible(False)


    while 1:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if(len(all_sprites) <= 0):
            break

        collide_list = pygame.sprite.spritecollide(raquette, ball_list, False)
        if len(collide_list):
            for sprite in collide_list:
                #sprite.speed[0] = -sprite.speed[0]
                sprite.speed[1] = -sprite.speed[1]
                # On repositionne la basse pile au-dessus de la raquette pour éviter des collisions permanentes.
                sprite.rect.bottom = raquette.rect.top

        screen.fill(black)
        # Update
        all_sprites.update()

        all_sprites.draw(screen)

        pygame.display.flip()
   

if __name__ == "__main__":
    # execute only if run as a script
    main()
   