import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((600, 600))
screen.fill((240, 240, 240))

circle(screen,(255, 255, 0), (300, 300), 200) # тело
circle(screen,(0, 0, 0), (300, 300), 200, 5) # контур тела

circle(screen, (255, 0, 0), (200, 250), 35) # левый глаз
circle(screen, (0, 0, 0), (200, 250), 35, 2) # контур левого глаза
circle(screen, (0, 0, 0), (200, 250), 17) # левый зрачек

circle(screen, (255, 0, 0), (400, 250), 25) # правый глаз
circle(screen, (0, 0, 0), (400, 250), 25, 2) # контур правого глаза
circle(screen, (0, 0, 0), (400, 250), 10) # правый зрачек

rect(screen, (0, 0, 0), (200, 400, 200, 50)) # рот

polygon(screen, (0, 0, 0), [(100, 110), (250, 235),
                            (240, 245), (90, 120)]) # левая бровь

polygon(screen, (0, 0, 0), [(340, 245), (500, 120),
                            (510, 130), (350, 255)]) # правая бровь

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
