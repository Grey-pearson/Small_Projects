import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Visual Sorter")
running = True

# width of bar
width = 50  # ?
# initial position
y = 1
x = 50

height = np.array(
    [  # 20 heights
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100,
        110,
        120,
        130,
        140,
        150,
        160,
        170,
        180,
        190,
        200,
    ]
)  # 20 at the mo
np.random.shuffle(height)


def show(height):

    for i in range(len(height)):
        pygame.draw.rect(screen, "green", (x * i, 500 - height[i], width, height[i]), 1)


while running:

    execute = False

    pygame.time.delay(10)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        screen.fill((0, 0, 0))
        show(height)
        pygame.display.update()

    # if execute flag is true
    else:
        # start sort with bubble sort
        for i in range(len(height) - 1):
            # max element will come at last
            for j in range(len(height) - i - 1):
                # starting is greater than next element
                if height[j] > height[j + 1]:
                    # save and swap int with temp variable
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t

                screen.fill((0, 0, 0))
                show(height)
                pygame.time.delay(50)
                pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()
