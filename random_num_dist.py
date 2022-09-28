import time
import tkinter
from random import randint

import pygame

root = tkinter.Tk()
WIDTH = root.winfo_screenwidth()  # 1366
HEIGHT = root.winfo_screenheight()  # 768
PH = HEIGHT-HEIGHT*0.2  # Proportional height

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


def random_num(num, rep=0):
    """
    This function paints rectangles using the sqr dictionary.
    The numbers in the dictionary are obtained by tossing a number.

    The function expects a positive integer argument, num. The random numbers that are drawn are numbers between 0 - num.

    The function also has a positive integer argument keyword argument, rep. It does the event of getting a random number, rep times.
    If rep is not defined, it will be the same as num.
    """
    if rep == 0:
        rep = num

    SQW = WIDTH/(2*num)
    if SQW < 1:
        raise Exception("Width is too low")

    time.sleep(0.25)

    # create a dict with all the numbers, their values are 0
    sqr = {}
    for i in range(num+1):
        sqr[i] = 0

    # get a random number from 0 til Num. And increase the value in the dict (by 1) of the number we got.
    # we do this rep times, the bigger rep is, the more acurate the graph is going to be
    for i in range(rep):
        r = randint(0, num)
        sqr[r] = sqr.get(r)+1

    # Draw a big black rectangle to clean the screen
    pygame.draw.rect(screen, BLACK, (0, 0, 2000, 2000))

    starting_height = 20
    # proportional height (with the max value, so it always going to be on the screen)
    rect_height = PH/max(sqr.values())

    # Draw the rectangles corresponding to the numbers
    for i in sqr:
        j = i*SQW
        # () tuple with 4 elements, the 2 first are the postion. The other two are the width and height
        pygame.draw.rect(screen, GREEN, (i*SQW+j, starting_height,
                                         SQW, rect_height*sqr.get(i)))
        pygame.display.update()

        time.sleep(0.002)


def random_num_sum(num, rep=0):
    """
    This function paints rectangles using the sqr dictionary.
    The numbers in the dictionary are obtained by tossing two numbers and adding them.

    The function expects a positive integer argument, num. The random numbers that are drawn are numbers between 0 - num.

    The function also has a positive integer argument keyword argument, rep. It does the event of getting a random number, rep times.
    If rep is not defined, it will be the same as num.
    """
    if rep == 0:
        rep = num

    SQW = WIDTH/(4*num)
    if SQW < 1:
        raise Exception("Width is too low")

    time.sleep(0.25)

    # create a dict with all the numbers, their values are 0
    sqr = {}
    for i in range((num*2)+1):
        sqr[i] = 0

    # get a random number from 0 til Num. And increase the value in the dict (by 1) of the number we got.
    # we do this rep times, the bigger rep is, the more acurate the graph is going to be
    for i in range(rep):
        r = randint(0, num)+randint(0, num)
        sqr[r] = sqr.get(r)+1

    # Draw a big black rectangle to clean the screen
    pygame.draw.rect(screen, BLACK, (0, 0, 2000, 2000))

    starting_height = 20
    # proportional height (with the max value, so it always going to be on the screen)
    rect_height = PH/max(sqr.values())

    # Draw the rectangles corresponding to the numbers
    for i in sqr:
        j = i*SQW
        # () tuple with 4 elements, the 2 first are the postion. The other two are the width and height
        pygame.draw.rect(screen, GREEN, (i*SQW+j, starting_height,
                                         SQW, rect_height*sqr.get(i)))
        pygame.display.update()


# initiate the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title
pygame.display.set_caption("Random Numbers Distribution")

running = True
while running:
    for ev in pygame.event.get():  # get an itarable object with all the events
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                n = 300  # if this value is too big, and the screen is too small, The graph is not going to be displayed
                r = 300000
                print("\n\n\nDistribution of Random Numbers, between 0 and ", n)
                print("'Rolled the dice ", r, " times'")
                random_num(n, r)
            elif ev.key == pygame.K_DELETE:
                n = 300  # if this value is too big, and the screen is too small, The graph is not going to be displayed
                r = 300000
                print(
                    "\n\n\nDistribution of The Sum From two Random Numbers, between 0 and ", n)
                print("'Rolled the dice ", r, " times'")
                random_num_sum(n, r)
            elif ev.key == pygame.K_ESCAPE:
                running = False
