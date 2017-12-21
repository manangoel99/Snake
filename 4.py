import pygame
import time

'''displayheight = input("Enter Height of Screen")
displaywidth = input("Enter Width of Screen")'''
pygame.init()
#Make Surface and give name to it
displayheight = 720
displaywidth = 1280
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Slither')
pygame.display.update()

white = (255,255,255)
red = (255,0,0)
#give color as a tuple in order RGB

#Make Font Object
font = pygame.font.SysFont(None,45)

FPS = 45
blocksize = 10

#Display Message
def MessageDisplay(msg,color):
    text = font.render(msg,True,color)                          #Render Text of Specific Color and Size
    gameDisplay.blit(text, [displaywidth/2,displayheight/2])    #Render The Message to the gameDisplay

clock = pygame.time.Clock()
#make a clock object

#Actual Game Loop
def GameLoop():
    gameExit = True
    x_coordinate = displaywidth/2
    x_coordinate_change = 0
    y_coordinate_change = 0
    y_coordinate = displayheight/2
    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_coordinate_change = -blocksize
                    y_coordinate_change = 0
                if event.key == pygame.K_RIGHT:
                    x_coordinate_change = blocksize
                    y_coordinate_change = 0
                if event.key == pygame.K_UP:
                    y_coordinate_change = -blocksize
                    x_coordinate_change = 0
                if event.key == pygame.K_DOWN:
                    y_coordinate_change = blocksize
                    x_coordinate_change = 0


            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    x_coordinate_change = 0
                if event.key == event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_coordinate_change = 0
            #print(event)'''


        x_coordinate += x_coordinate_change
        y_coordinate += y_coordinate_change

        if x_coordinate > displaywidth:
            gameExit = False
        if  x_coordinate < 0:
            gameExit = False
        if y_coordinate > displayheight:
            gameExit = False
        if y_coordinate < 0:
            gameExit = False
        gameDisplay.fill(white)


        #pygame.draw.rect(gameDisplay,red,[640,360,10,100])
        #surface,colour,position of top left,width,height    


        gameDisplay.fill(red,rect = [x_coordinate,y_coordinate,blocksize,blocksize])
        #faster way to make shape


        pygame.display.update()


        clock.tick(FPS)                  
        #specify number of frames per second

    MessageDisplay("You Lose HAHAHAHAHA",red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

GameLoop()