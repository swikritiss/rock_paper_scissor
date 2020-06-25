import os
from pygame import *
import pygame
from math import *
import random

pygame.init()

gap = 70

square_size = 100
width = square_size*6
height = square_size*4




#initialising display
screen = pygame.display.init()


#initialising variables
choice_list = [0 , 1 , 2]
list1 = ['rock', 'paper' , 'scissor']
list_dict = {"rock":0,"paper":1,"scissor":2}

size = (width,height)
largeText = pygame.font.Font('freesansbold.ttf',30)
smallText = pygame.font.Font('freesansbold.ttf',15)

img_rock = image.load("images/rock.png")
img_rock = pygame.transform.scale(img_rock, (int(square_size/1.25), int(square_size/1.25)))

img_paper = image.load("images/paper.png")
img_paper = pygame.transform.scale(img_paper, (int(square_size/1.25), int(square_size/1.25)))

img_scissor = image.load("images/scissor.png")
img_scissor = pygame.transform.scale(img_scissor, (int(square_size/1.25), int(square_size/1.25)))


#player choice determination
def get_choice(pos):
    x = pos[0]
    y = pos[1]
    if x>=gap and x<=gap+square_size and y>=2*square_size and y<=3*square_size:
        print("rock")
        return(0)

    elif x>=2*gap+square_size and x<=2*gap+2*square_size and y>=2*square_size and y<=3*square_size:
        print("paper")
        return(1)

    elif x>=3*gap+2*square_size and x<=3*gap+3*square_size and y>=2*square_size and y<=3*square_size:
        print("scissor")
        return(2)

#computer choice determination
def display_computer_choice(player_choice):
    global screen
    choice_list = [0,1,2]
    temp = choice_list
    comp_choice = random.choice(choice_list)
    temp = choice_list
    temp.remove(comp_choice)
    print(temp)
    print(comp_choice)
    pygame.draw.rect(screen,(0,0,0),(0,0,width, square_size*1.45))
    TextSurf, TextRect = text_objects("Computer chose:", largeText, (255,255,255))
    TextRect.center = ((width/2),square_size/2)
    screen.blit(TextSurf, TextRect)
    for i in temp:
        pygame.draw.rect(screen, (0,0,0),(gap+(gap +square_size)*i, 2*square_size, square_size, square_size))
    pygame.display.update()

    
    pygame.display.update()
    pygame.time.wait(2500)
    show_result(player_choice,comp_choice)

#calculate and result
def show_result(player,computer):
    global screen
    matrix = [[0,-1,1],
            [1,0,-1],
            [-1,1,0]
            ]
    # for row in matrix:
    #         for column in row:
    #                 print (column)
    screen.fill((0,0,0))
    if matrix[player][computer] == 1:
        TextSurf, TextRect = text_objects("You Win!", largeText, (255,255,255))
        TextRect.center = ((width/2), square_size*2)
        screen.blit(TextSurf, TextRect)
    elif matrix[player][computer] == -1:
        TextSurf, TextRect = text_objects("You Lost!", largeText, (255,255,255))
        TextRect.center = ((width/2), square_size*2)
        screen.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects("Draw!", largeText, (255,255,255))
        TextRect.center = ((width/2), square_size*2)
        screen.blit(TextSurf, TextRect)
    
    pygame.display.update()
    pygame.time.wait(3000)
    playing()


    
        

#define main function
def playing():
    global screen
    
    pygame.display.set_caption('Rock Paper Scissor')

    screen = pygame.display.set_mode(size)
    screen.fill((0,0,0))
    TextSurf, TextRect = text_objects("Rock Paper Scissor Game", largeText, (255,255,255))
    TextRect.center = ((width/2),square_size/2)
    screen.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Choose One", smallText, (255,255,255))
    TextRect.center = ((width/2),square_size*1.25)
    screen.blit(TextSurf, TextRect)
    pygame.draw.rect(screen,(0,255,0),(0,square_size,width,1))

    img_rock = image.load("images/rock.png")
    img_rock = pygame.transform.scale(img_rock, (int(square_size/1.25), int(square_size/1.25)))

    img_paper = image.load("images/paper.png")
    img_paper = pygame.transform.scale(img_paper, (int(square_size/1.25), int(square_size/1.25)))

    img_scissor = image.load("images/scissor.png")
    img_scissor = pygame.transform.scale(img_scissor, (int(square_size/1.25), int(square_size/1.25)))
    
    pygame.draw.rect(screen,(255,0,0),(gap,2*square_size,square_size, square_size))
    pygame.draw.rect(screen,(202, 224, 31),(2*gap+square_size,2*square_size,square_size, square_size))
    pygame.draw.rect(screen,(0,0,255),(3*gap+2*square_size,2*square_size,square_size, square_size))
    screen.blit(img_rock,((gap+10, 2*square_size+10)))
    screen.blit(img_paper,((2*gap+square_size+10, 2*square_size+10)))
    screen.blit(img_scissor,((3*gap+2*square_size+10, 2*square_size+10)))
    pygame.display.update()
    while True:
        #to prevent crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if pygame.mouse.get_pressed() == (1,0,0):
            print(pygame.mouse.get_pos())
            choice = get_choice(pygame.mouse.get_pos())
            
            display_computer_choice(choice)
        pygame.display.update()
        

#define text   
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()         


playing()





