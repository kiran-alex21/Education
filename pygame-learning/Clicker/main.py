import pygame

# set CONSTANTS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MID_WIDTH = SCREEN_WIDTH/2
MID_HEIGHT = SCREEN_HEIGHT/2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Atkinson Hyperlegible Next", 30, bold=True)

# bool flags
running = True
face_clicked = False

# vars
time_click = None
score = 0

# setup image surfaces
normal_face = pygame.image.load("C:\\Users\\Kiran Wood\\Documents\\Computing\\Coding_with_python\\Education\\pygame-learning\\Clicker\\data\\emotional.png").convert_alpha() # preserves empty space
NORMAL_FACE_WIDTH = normal_face.get_width()
NORMAL_FACE_HEIGHT = normal_face.get_height()
normal_face_rect = pygame.Rect((MID_WIDTH-(NORMAL_FACE_WIDTH/2)), (MID_HEIGHT-(NORMAL_FACE_HEIGHT/2)), NORMAL_FACE_WIDTH, NORMAL_FACE_HEIGHT) #create tupple with correct sizing and placement

happy_face = pygame.image.load("C:\\Users\\Kiran Wood\\Documents\\Computing\\Coding_with_python\\Education\\pygame-learning\\Clicker\\data\\happy.png").convert_alpha()
HAPPY_FACE_WIDTH = happy_face.get_width()
HAPPY_FACE_HEIGHT = happy_face.get_height()
happy_face_rect = pygame.Rect((MID_WIDTH-(HAPPY_FACE_WIDTH/2)), (MID_HEIGHT-(HAPPY_FACE_HEIGHT/2)), HAPPY_FACE_WIDTH, HAPPY_FACE_HEIGHT)

# main running loop
while running:
    for event in pygame.event.get(): # check for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

        # image choice and render logic
        if event.type == pygame.MOUSEBUTTONDOWN: # check mouse has been clicked
            if normal_face_rect.collidepoint(event.pos): # see if mouse is on face
                face_clicked = True
                score += 1 # add to score
                time_click = pygame.time.get_ticks() # gets miliseconds since initiation

    if face_clicked and (pygame.time.get_ticks() - time_click < 250): # if face clicked and time displayed is less that 0.25 seconds
        screen.fill((150, 150, 150)) # fill the screen with a color
        pygame.draw.circle(screen, (200, 100, 50), (MID_WIDTH, MID_HEIGHT), (HAPPY_FACE_HEIGHT/1.5)) # create circular background
        screen.blit(happy_face, happy_face_rect) # add happy face to display
    else:
        screen.fill((150, 150, 150)) # fill the screen with a color
        screen.blit(normal_face, normal_face_rect) # add normal face to display
    
    # score render
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    score_rect = pygame.Rect(25, 25, score_text.get_width(), score_text.get_height())
    screen.blit(score_text, score_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()