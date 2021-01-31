import pygame, random, time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Set the height and width of the screen
size = [1280, 720]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)


def veh_speed(msg, color):
    speed_text = font.render(msg, True, color)
    screen.blit(speed_text, [180, 340])


v_speed = 0


while not done:

    clock.tick(5)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(BLACK)

    keys = pygame.key.get_pressed()

    #vSpeed = random.randint(20, 75)

    if keys[pygame.K_LEFT]:
        vSpeed = vSpeed - 1
    if keys[pygame.K_RIGHT]:
        vSpeed = vSpeed + 1
    if keys[pygame.K_UP]:
        vSpeed = vSpeed + 5
    if keys[pygame.K_DOWN]:
        vSpeed = vSpeed - 5

    vSpeedString = str(vSpeed)
    pygame.draw.lines(screen, GREEN, True, [(178, 338), (270, 338), (279, 350), (270, 362), (178, 362)], 2)
    pygame.draw.line(screen, GREEN, [285, 100], [285, 620], 2)
    veh_speed((vSpeedString + " MPH"), GREEN)

    pygame.display.update()
    pygame.display.flip()