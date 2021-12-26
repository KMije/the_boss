#!/usr/bin/env python3
import pygame
import sys


class Figura:
  def __init__(self, img, position):
    self.surface = pygame.image.load(img).convert_alpha()
    self.rect = self.surface.get_rect()
    self.rect.x, self.rect.y = position
    self.mask = pygame.mask.from_surface(self.surface)

  def colliding_with(self, other):
    """Restituisce True in caso di collisione, False altrimenti
    other: altro oggetto di tipo Figura con cui controllare la collisione
    """
    return self.rect.colliderect(other.rect) \
      and self.mask.overlap(other.mask, (
        other.rect.x - self.rect.x,
        other.rect.y - self.rect.y,
      ))


def main():
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((900, 700))


  mike = Figura("img/michele.png", (20, 400))

  mostri = [
    Figura("img/ragno.png", (300, 570)),
    Figura("img/ragno.png", (600, 570))
  ]

  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    screen.fill((125, 125, 125)) # schermo bigio

    screen.blit(mike.surface, mike.rect)

    for m in mostri:
      screen.blit(m.surface, m.rect)

    #print(mike.colliding_with(mostri[0]))

    pygame.display.update()
    clock.tick(30)

if __name__ == '__main__':
  sys.exit(main())
