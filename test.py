import pygame

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

rect(screen, (0, 255, 255), (0, 0, 600, 400))    #голубой фон
rect(screen, (0, 255, 0), (0,400, 600,400))   #зеленый фон

circle(screen, (255, 232, 36), (550, 70), 110) #солнце

rect(screen, (255, 255, 255), (100, 400, 40, 200)) #ствол дерева

ellipse(screen, (0, 102, 0), (30, 120, 200, 210)) #овал1
ellipse(screen, (0, 102, 0), (-20, 230, 300, 200)) #овал2
ellipse(screen, (0, 102, 0), (35, 370, 180, 140)) #овал3

ellipse(screen, (255, 204, 204), (140, 160, 50, 45)) #яблочки1
ellipse(screen, (255, 204, 204), (-20, 310, 50, 45)) #яблочки2
ellipse(screen, (255, 204, 204), (210, 310, 50, 45)) #яблочки3
ellipse(screen, (255, 204, 204), (150, 450, 45, 45)) #яблочки4

rect(screen, (255, 255, 255), (420, 480, 60, 110)) #шейка
ellipse(screen, (255, 255, 255), (440, 440, 90, 45)) #голова
ellipse(screen, (255, 255, 255), (430, 430, 70, 50)) #где_рог
polygon(screen, (255, 255, 255), [(455, 577), (461, 453),(351, 557)])#сложно
polygon(screen, (255, 102, 255), [(480, 316), (450, 436),(472, 436)])#рог
ellipse(screen, (255, 0, 127), (465, 450, 20, 20))#глазыыы
ellipse(screen, (0, 0, 0), (475, 455, 10, 10))#глазыыы

ellipse(screen, (255, 229, 204), (420, 435, 40, 20)) #кружки
ellipse(screen, (255, 0, 204), (415, 445, 40, 30)) #кружки
ellipse(screen, (255, 202, 204), (400, 450, 40, 20)) #кружки
ellipse(screen, (255, 202, 204), (390, 450, 40, 25)) #кружки
ellipse(screen, (200, 202, 204), (390, 470, 50, 25)) #кружки
ellipse(screen, (200, 202, 204), (390, 490, 60, 34)) #кружки
ellipse(screen, (200, 0, 204), (370, 490, 60, 34)) #кружки
ellipse(screen, (200, 110, 100), (360, 510, 60, 20)) #кружки
ellipse(screen, (100, 150, 204), (335, 520, 60, 34)) #кружки
ellipse(screen, (200, 36, 204), (330, 515, 55, 40)) #кружки
ellipse(screen, (200, 58, 10), (320, 530, 60, 20)) #кружки
ellipse(screen, (200, 0, 150), (300, 515, 55, 40)) #кружки
ellipse(screen, (255, 230, 10), (320, 530, 60, 20)) #кружки




ellipse(screen, (200, 202, 204), (250, 620, 60, 45)) #хвост
ellipse(screen, (200, 202, 2), (230, 620, 55, 20)) #хвост
ellipse(screen, (200, 22, 2), (210, 625, 40, 20)) #хвост
ellipse(screen, (20, 202, 204), (250, 650, 40, 45)) #хвост
ellipse(screen, (251, 202, 2), (230, 630, 55, 20)) #хвост
ellipse(screen, (100, 22, 2), (190, 625, 40, 20)) #хвост
ellipse(screen, (200, 20, 24), (250, 660, 60, 45)) #хвост
ellipse(screen, (200, 202, 26), (230, 620, 55, 20)) #хвост
ellipse(screen, (200, 22, 45), (210, 700, 40, 20)) #хвост
ellipse(screen, (20, 202, 168), (250, 690, 40, 45)) #хвост
ellipse(screen, (251, 202,37), (230, 680, 55, 20)) #хвост
ellipse(screen, (100, 92, 78), (230, 670, 40, 20)) #хвост


ellipse(screen, (255, 255, 255), (260, 550, 230, 120)) #тело_еденорожка

rect(screen, (255, 255, 255), (280, 615, 20, 120)) #ножка1
rect(screen, (255, 255, 255), (325, 605, 23, 120)) #ножка2
rect(screen, (255, 255, 255), (400, 615, 20, 120)) #ножка3
rect(screen, (255, 255, 255), (450, 590, 17, 130)) #ножка4

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()