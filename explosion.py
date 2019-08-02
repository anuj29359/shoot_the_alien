import pygame
from pygame.sprite import Sprite



class Explosion(Sprite):
    """Class to animate explosions"""
    def __init__(self, size, center):
        """initialise the explosion class"""
        super(Explosion, self).__init__()
        self.size = size  # size of the explosion, small/large
        self.center = center  # center of where to do explosion
        self.image = self.explosion_anim[size][0]
        self.rect = pygame.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.explosion_anim = {} # empty list to store the images to create the animation of explosion
        self.explosion_anim['sm'] = []
        self.explosion_anim['lg'] = []

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = pygame.time.get_ticks()
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                self.center = self.image.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = self.center


    def load_explosion_amin(self):
        for i in range(8):
            filename = 'images\\img_explosion0{}.png'.format(i)
            img_explosion = pygame.image.load(filename)
          # img_explosion.set_colorkey(0,0,0)

            #transform the image size to 75x75 px and append it to the list of large images
            img_lg = pygame.transform.scale(img_explosion, (75, 75))
            self.explosion_anim['lg'].append(img_lg)

            #transform the image size to 35x35 px and append it to the list of small images
            img_lg = pygame.transform.scale(img_explosion, (35, 35))
            self.explosion_anim['sm'].append(img_lg)



