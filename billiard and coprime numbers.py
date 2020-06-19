import pygame
import sys
import random
from math import sqrt

pygame.init()


coprimeList = tuple(open('coprime numbers list.txt', 'r').read().split('\n'))
LENGTH = 5
SIZE = random.choice(coprimeList)
SIZE = tuple(i*LENGTH for i in (map(int, SIZE.split())))
print(SIZE)
WHITE = (255, 255, 255)
DOTCOLOR = (5, 60, 70)
x, y = 0, 0
vector = 'br'
draw = True

print(LENGTH)

screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
event = pygame.event.poll()

while event.type != pygame.QUIT:
    event = pygame.event.poll()
    if vector == 'br':
        xn, yn = x + LENGTH, y + LENGTH
    elif vector == 'bl':
        xn, yn = x - LENGTH, y + LENGTH
    elif vector == 'tr':
        xn, yn = x + LENGTH, y - LENGTH
    elif vector == 'tl':
        xn, yn = x - LENGTH, y - LENGTH
    if draw:
        pygame.draw.line(screen, DOTCOLOR, (x, y), (xn, yn), 2)
        draw = False
    else:
        draw = True
    print(xn, yn)

    x, y = xn, yn
    if (x, y) in [(0, 0), (SIZE[0], 0), (0, SIZE[1]), SIZE]:
        while event.type != pygame.QUIT:
            event = pygame.event.poll()
        if input('DO YOU WANT TO SAVE THIS PATTERN?\n y/n: ') == 'y':
            filename = "billiard"
            fileFormat = '.png'
            n = 0
            while True:
                n+=1
                try:
                    checkFile = open(filename+str(n)+fileFormat)
                    checkFile.close()
                except FileNotFoundError:
                    filename = filename+str(n)+fileFormat
                    break
            pygame.image.save(screen, filename)
            print("file {} has been saved".format(filename))
        break
    elif x <= 0:
        if vector == 'tl':
            vector = 'tr'
        else:
            vector = 'br'
    elif x >= SIZE[0]:
        if vector == 'br':
            vector = 'bl'
        else:
            vector = 'tl'
    elif y <= 0:
        if vector == 'tr':
            vector = 'br'
        else:
            vector = 'bl'
    elif y >= SIZE[1]:
        if vector == 'bl':
            vector = 'tl'
        else:
            vector = 'tr'




    pygame.display.flip()


