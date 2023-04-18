# SNAKE GAME MADE BY JIS THE XENZIA
# FIRST WE DISCUSS ABOUT THE MODULES WE HAVE USED IN OUR PROJECT
# WE IMPORT PYGAME, RANDOM, OS, AND PYTTSX3

#################
import pygame  # we install it by using comand prompt "pip install pygame" it is basis of our game
import random  # this module generate random numbers in python we used it for food
import os      # it is basically used for operating the files we made
import pyttsx3  # this we use for speaking in python we also install it

#################


#######################################
engine = pyttsx3.init()  # this is the whole operation performing for "pyttsx3"
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # there is an index "0" represents the voice of the male "1" for female
engine.setProperty('rate', 250)   # here we fix the rate means the voice speed
engine.runAndWait()


def speak(str):  # define the function here so we call speak any where we want
    engine.say(str)
    engine.runAndWait()


speak("hello, how are you? You are playing JIS the xenzia.")
########################################


###################
pygame.mixer.init()  # this is used for the music we have used in our game we get this by pygame documentary

pygame.init()
###################


###########################

# Colors used in our game
white = (255, 255, 255)  # every colour has its different code in python
red = (255, 0, 0)
black = (0, 0, 0)
green = (152, 251, 152)
grey = (128, 128, 128)
blue = (0, 0, 255)

###########################


####################################

# Creating window
screen_width = 1000
screen_height = 650
# we created the window in pygame by using pygame.display.set_mode((screen_width, screen_height))
# the line below generates a screen for a while we have of our given width and height
gameWindow = pygame.display.set_mode((screen_width, screen_height))

###############################################################################


#####################################

# background
bgimg = pygame.image.load("sss.jpeg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

#####################################################################################


#####################################################################################

#  Game Title this title should be on our screen this is also from pygame documentary
pygame.display.set_caption("Snakes With JIS the Xenzia ")
pygame.display.update()  # we use this to make our screen visualize on display with our colours
clock = pygame.time.Clock()  # it is essential for our game to tell how many frames per second we want
font = pygame.font.SysFont(None, 55)  # we use font here "None" represent default font and [55] represent size


######################################################################################


###############################################

def level_screen(text, color, x, y):  # it is used to represent level on screen
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


################################################


################################################

def text_screen(text, color, x, y):  # use for showing score on screen
    screen_text = font.render(text, True, color)  # it is the syntax of it
    gameWindow.blit(screen_text, [x, y])  # We use blit here that allows easily to draw images


################################################


################################################

def fps_rate(text, color, x, y):  # use for showing score on screen
    screen_text = font.render(text, True, color)  # it is the syntax of it
    gameWindow.blit(screen_text, [x, y])  # We use blit here that allows easily to draw imag


##################################################


###########################################################

def plot_snake(gameWindow, color, snk_list, snake_size):  # define te function for plotting the snake
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


############################################################





################################################################
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                elif  event.key == pygame.K_t:
                    tips()



            gameWindow.fill(green)
            bgimg = pygame.image.load("jis.png")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))

        text_screen("You have paused the game", red, 220   , 250)
        text_screen("Press c to continue and q to quit", blue, 180, 290)
        text_screen("####### JIS #######", black, 257, 100)
        text_screen("Press t for seeing tips", grey, 242, 330)
        pygame.display.update()
        clock.tick(5)

##################################################################


#################################################################
def tips():
    tips = True
    while tips:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    tips = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            gameWindow.fill((233, 210, 229))  # color code here

        text_screen("####### JIS #######", red, 257, 100)
        text_screen("   Tip 1  use cursor keys to move the snake    ", blue, 100, 240)
        text_screen("Tip 2  you will get 10 points after eating food", red, 94, 290)
        text_screen("               Best of Luck                    ", blue, 164, 340)
        text_screen("             Press s to return                 ", black, 164, 390)
        pygame.display.update()
        clock.tick(5)

############################################################




##############################################################

def welcome():  # we made the initial set up
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 210, 229))  # color code here
        bgimg = pygame.image.load("sij.jpg")
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))
        text_screen("####### JIS #######", red, 257, 100)
        text_screen("Welcome to Snakes", black, 260, 250)  # set the text to be shown
        text_screen("Press Space Bar To Play Butter 0 for Dynamite", blue, 90, 290)
        text_screen("Press t for seeing tips", red, 247, 335)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True  # game should be exited
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # after pressing the space key
                    pygame.mixer.music.load('Butter.mp3')  # here the music will be loaded
                    pygame.mixer.music.play()  # here start playing
                    gameloop()  # throughout the gameloop
                elif event.key == pygame.K_0:
                    pygame.mixer.music.load('Dynamite.mp3')  # here the music will be loaded
                    pygame.mixer.music.play() 
                    gameloop()
                elif event.key == pygame.K_t:
                    tips()


        pygame.display.update()
        clock.tick(60)




###############################################################


###############################################

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    # the game will be exited only when we want to exit it cannot exit it self
    game_over = False
    # we used it as false because when it is true the game will be exited we ask user to exit or not
    snake_x = 45  # it is the length of snake use in pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []  # we introduce an empty list in which snake length is to be stored
    snk_length = 1  # snake length is initially one
    level = 1  # initializing the level

    # Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:  # it will automaticaly create the file
            f.write("0")

    with open("hiscore.txt", "r") as f:  # the file should be read
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)  # here food is generated within our screen it will not go out
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5  # we have given the velocity to snake after we press keys
    snake_size = 20  # we specify the snake size here
    fps = 50

    # now we make a loop for our game that will include all the function in our game
    # while not exit game means the game is true running when then the operations to be performed are below in loop
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:  # the hiscore should be write mean the file should be modified
                f.write(str(hiscore))  # here file is modified
            gameWindow.fill(white)  # this is the colour shown on our window

            text_screen("####### JIS #######", black, 257, 100)
            text_screen("Game Over! Press Enter To Continue", red, 108, 250)

            for event in pygame.event.get():  # this for loop will tell us the all the events using pygame in while loop each and every moment in game
                if event.type == pygame.QUIT:  # we use pygame.QUIT to exit game here
                    exit_game = True  # "pygame.QUIT" we got this by pygame documentry

                if event.type == pygame.KEYDOWN:  # KEYDOWN refers that some key is pressed
                    if event.key == pygame.K_RETURN:  # and if key is pressed then the loop goes to the next statement
                        welcome()  # it will now go to welcome func



        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity  # the snake will move in x-direction
                        velocity_y = 0  # no movement along y axis resist diagonal motion

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity  # the sanke will move in left
                        velocity_y = 0  # no movement along y axis resist diagonal motion

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity  # the snake will move along y-direction up
                        velocity_x = 0  # no movement along x axis resist diagonal motion

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity  # the snake will move along y-direction down
                        velocity_x = 0  # no movement along x axis resist diagonal motion

                    if event.key == pygame.K_a:  # a cheat
                        score += 10

                    if event.key == pygame.K_p:
                        pause()

                    if event.key == pygame.K_t:
                        tips()

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            snake_x = snake_x + velocity_x  # we give the velocity in x direction to snake
            snake_y = snake_y + velocity_y  # we give the velocity in y direction to snake

            if abs(snake_x - food_x) < 15 and abs(
                    snake_y - food_y) < 15:  # we use abs which give approx w   e also change it
                score += 10  # score increase by 10
                food_x = random.randint(20, screen_width / 2)  # again the food generated
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score > int(hiscore):  # setting condition for hiscore
                    hiscore = score

                if level == 1 and score == 50:
                    level += 1  # increment in levels on the basis of scores

                if level == 2 and score == 100:
                    level += 1  # increment in levels on the basis of scores

                if level == 3 and score == 150:
                    level += 1  # increment in levels on the basis of scores

                if level == 4 and score == 200:
                    level += 1  # increment in levels on the basis of scores

                if level == 5 and score == 250:
                    level += 1  # increment in levels on the basis of scores

                if level == 6 and score == 300:
                    level += 1  # increment in levels on the basis of scores

                if level == 7 and score == 350:
                    level += 1  # increment in levels on the basis of scores

                if level == 8 and score == 400:
                    level += 1  # increment in levels on the basis of scores

                if level == 9 and score == 450:
                    level += 1  # increment in levels on the basis of scores

                #fps with levels
                if level == 1:
                    fps=50
                if level == 2:
                    fps=60
                if level == 3:
                    fps=70
                if level == 4:
                    fps=80
                if level == 5:
                    fps=90
                if level == 6:
                    fps=100
                if level == 7:
                    fps=100
                if level == 8:
                    fps=100
                if level == 9:
                    fps=100
                if level == 10:
                    fps=100
                ############################




            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen(
                "Score: " + str(score) + "  Hiscore: " + str(hiscore) + "  level: " + str(level) + " fps: " + str(fps) +  "  # JIS # ", green,
                3, 3)
            # all text on screen in above line
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            # pygame.draw.rect this is the simplest way to make a rectangle in python we explain food and snake size

            head = []  # we made a head in list that is empty
            head.append(snake_x)  # now we append snake in it through the food eaten along x axis
            head.append(snake_y)  # now we append snake in it through the food eaten along y axis
            snk_list.append(head)  # at end we append head in that list that we have made earlier

            if len(snk_list) > snk_length:  # this condition is preventing snake from incresing beyond its length
                del snk_list[0]  # the extra head should be cut down

            if head in snk_list[
                       :-1]:  # it means that if head should be any of the element of list except it then game over
                game_over = True
                pygame.mixer.music.load('hassan.mp3')  # here the game over sound and we define it at start
                pygame.mixer.music.play()
                speak("ooops you died you have cut your self")  # we also define speak
                print("Score: " + str(score) + "  Hiscore: " + str(hiscore) + "  level: " + str(level) + " fps: " + str(fps)+ " # JIS # ")
                print(" i hope you enjoyed the game!!!!!!")

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:  # 2nd snake out condition
                game_over = True
                pygame.mixer.music.load('hassan.mp3')
                pygame.mixer.music.play()
                speak("oops you died, i hope you will do better next time")  # same function caling
                print("  Score: " + str(score) + "\n  Hiscore: " + str(hiscore) + "\n  level: " + str(
                    level) + "\n fps: " + str(fps)+  "\n   # JIS # ")
                print(" i hope you enjoyed the game!!!!!!")


            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()  # whenever the loop will be exited the game should be quited
    quit()  # these two lasts are used for exiting the loop



welcome()
#################################### END ############################################
