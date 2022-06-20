
import pygame
from constants import *
from objects import *

pygame.init()
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Sorting")

for x in range(40):
    Object("green", "rectangle", x*20)
run = True
runner = 0

while run:
    win.fill((0, 0, 0))
    for shape in Base.all_objects:
        shape.draw(win)
    pygame.time.delay(20)
    while runner != 39:
        runner = 0
        print('restart!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        for pos in range(len(Base.all_objects)):
            if pos <= 38:
                if Base.all_objects[pos].height > Base.all_objects[pos+1].height:
                    smaller = Base.all_objects[pos].x
                    larger = Base.all_objects[pos + 1].x
                    Base.all_objects[pos].x = larger
                    Base.all_objects[pos + 1].x = smaller
                    #print(runner, pos,"yes", smaller, larger)

                else:
                    runner += 1
                    #print(runner, pos,"no", Base.all_objects[pos].x, Base.all_objects[pos+1].x)
            win.fill((0, 0, 0))
            for shape in Base.all_objects:
                shape.draw(win)
            pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()


pygame.quit()
