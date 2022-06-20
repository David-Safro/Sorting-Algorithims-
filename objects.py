import pygame
import random


class Base:
    all_objects = []

    def __init__(self):
        Base.all_objects.append(self)


class Object(Base):
    def __init__(self, color, shape, x):
        super().__init__()
        self.color = color
        self.shape = shape
        self.height = random.randint(10, 700)
        self.x = x
        self.y = 800-self.height
        self.width = 18

    def draw(self, win):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, rect)

