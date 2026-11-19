import pygame #(1)get pygme library

pygame.init() #(1)start pygame running

screen = pygame.display.set_mode((1080, 640)) #(1)create a special display surface which is the main window
clock = pygame.time.Clock() #(4)creates a clock to help regulate framerates

test_image = pygame.image.load("C:\\Users\\Kiran Wood\\Documents\\Computing\\Coding_with_python\\Education\\pygame-learning\\imgs\\platform1.gif").convert() #(3)load an image into a pygame surface. convert into fastest pixel format for rendering

#(6)use in-built functions to get the height and width of the image
test_img_height = test_image.get_height()
test_img_width = test_image.get_width()

test_image = pygame.transform.scale(test_image,(test_img_width * 2, test_img_height * 2)) #(6)scales the image to double its original size

## (1)Main running loop
running = True #(1)set a boolean variable for the loop
x=0 #(3.1)setting an x co-ord
while running: #(1)
    screen.fill((209, 169, 232)) #(5)fills the screen with a colour using an RGB value (this is a light purple)

    screen.blit(test_image, (x, 30)) #(3)put image surface onto screen surface, co-ods are top left corner for placement
    x += 1 #(3.1)updating the x co-ord to move over by 1

    for event in pygame.event.get(): #(2)gets a list of events that have happened since last call
        if event.type == pygame.QUIT: #(2)QUIT event happens when the windows 'X' button is pressed
            running= False #(2)stops loop running
    
    pygame.display.flip() #(3)updates the actual display (renders the display screen) does not clear previous screen
    clock.tick(60) #(4)slows game to desired framerate (usually 60fps)

pygame.quit() #(2)ends pygame running and quits neatly.

