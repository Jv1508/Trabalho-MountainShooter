#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, ENEMY_MOVEMENT, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, ENEMY_MOVEMENT):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.ENEMY_MOVEMENT = ENEMY_MOVEMENT
        self.up = True

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.ENEMY_MOVEMENT == ENEMY_MOVEMENT[1]:
            if self.up:
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.centery <= 0:
                    self.up = False
            else:
                self.rect.centery += ENTITY_SPEED[self.name]*2
                if self.rect.centery >= WIN_HEIGHT:
                    self.up = True



















    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


