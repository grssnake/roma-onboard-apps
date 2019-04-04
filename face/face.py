#! /usr/bin/python3

import os, sys
import pygame
from time import sleep

cwd = os.path.dirname(os.path.realpath(__file__))

pygame.init()

SIZE = WIDTH, HEIGHT = 480, 800
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
pygame.display.set_caption('Roma Face')
clock = pygame.time.Clock()

def load_images(path):
    """
    Loads all images in directory. The directory must only contain images.
    Args:
        path: The relative or absolute path to the directory to load images from.
    Returns:
        List of images.
    """
    #print(sorted(os.listdir(path)))
    #avaible = ['g28428', 'g28302', 'g28250']


    images = []
    for file_name in sorted(os.listdir(path)):
        if True: #file_name in avaible:
            image = pygame.image.load(cwd + os.sep + path + os.sep + file_name).convert()
            images.append(image)
    return images

def main():
    images = load_images(path='eyes')

    print(images)

    images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.

    seq = [
        [images[7], 5],
        [images[4], 0.5],
        [images_left[4], 0.5],
        [images[7], 5],
        [images[4], 0.5],
        [images_left[4], 0.5],
        [images[3], 1],
    ]

    r1 = images[4].get_rect()
    r2 = images_left[4].get_rect()
    r3 = images[7].get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.

        for i in seq:
            screen.fill(BACKGROUND_COLOR)
            screen.blit(i[0], i[0].get_rect())
            pygame.display.update()
            sleep(i[1])

#        pygame.display.flip()


if __name__ == '__main__':
    main()

