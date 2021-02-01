import pygame
import random
import time
import obd

pygame.init()

# Declare color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 69, 0)
# Define pi for easy use
pi = 3.14159265

# Set the height and width of the screen, also initialize window and make 'screen' a surface
size = [1280, 720]
screen = pygame.display.set_mode(size)

# Set window name
pygame.display.set_caption("carHUD OS 0.1")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Creating different fonts for text
font = pygame.font.SysFont(None, 36)
clock_font = pygame.font.SysFont(None, 50)


# Vehicle speed text display function
def veh_speed(msg, color):
    speed_text = font.render(msg, True, color)
    screen.blit(speed_text, [180, 340])


# Vehicle rpm text display function
def veh_rpm(msg, color):
    rpm_text = font.render(msg, True, color)
    screen.blit(rpm_text, [1011, 340])


# Time text display function
def draw_time(msg, color):
    time_text = clock_font.render(msg, True, color)
    screen.blit(time_text, [120, 580])


# Initialize speed and rpm variables
v_speed = 0
v_rpm = 0


# Defining turn calculation rects for arc drawing, initialize turn_track

turn_rect_left = pygame.Rect([285, 300, 355, 420])
turn_rect_right = pygame.Rect([640, 300, 355, 420])
turn_track = 0

# Tire pressure colors, will eventually go off obd data and if/elif statements
tire_color_rr = GREEN
tire_color_rl = GREEN
tire_color_fr = ORANGE
tire_color_fl = GREEN


# Main Loop
while not done:

    clock.tick(10)
    current_time = time.strftime('%H:%M:%S')

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
# TESTING PURPOSES ONLY
    ##############################################

    v_speed = random.randint(20, 75)
    v_rpm = random.randint(1000, 1500)

    if keys[pygame.K_LEFT]:
        turn_track = turn_track + 8
    if keys[pygame.K_RIGHT]:
        turn_track = turn_track - 8
    if keys[pygame.K_UP]:
        v_speed = v_speed + 5
    if keys[pygame.K_DOWN]:
        v_speed = v_speed - 5
    if keys[pygame.K_SPACE]:
        pygame.draw.rect(screen, RED, pygame.Rect(30, 30, 60, 60)) 

    ################################################

    # Converting ints to strings to display as text
    v_speed_string = str(v_speed)
    v_rpm_string = str(v_rpm)

    # Drawing boxes around MPH and RPM
    pygame.draw.lines(screen, GREEN, True, [(178, 338), (270, 338), (279, 350), (270, 362), (178, 362)], 2)
    pygame.draw.lines(screen, GREEN, True, [(1130, 338), (1010, 338), (1001, 350), (1010, 362), (1130, 362)], 2)

    # Maxing out turn track at 90 degrees
    if turn_track > 90:
        turn_track = 90
    elif turn_track < -90:
        turn_track = -90

    # Uses 2 separate rects to draw turn calculation line based off of wheel rotation 'turn_track'
    if turn_track > 0:
        pygame.draw.arc(screen, GREEN, turn_rect_left, 0, turn_track * (pi / 180), 3)
    elif turn_track < 0:
        pygame.draw.arc(screen, GREEN, turn_rect_right, pi - (turn_track * -(pi / 180)), pi, 3)

    # Drawing tire rectangles (changing tire color up above will change this for now)
    pygame.draw.polygon(screen, tire_color_rr, [(1100, 320), (1100, 270), (1115, 270), (1115, 320)], 6)
    pygame.draw.polygon(screen, tire_color_rl, [(1030, 320), (1030, 270), (1045, 270), (1045, 320)], 6)
    pygame.draw.polygon(screen, tire_color_fr, [(1100, 170), (1100, 220), (1115, 220), (1115, 170)], 6)
    pygame.draw.polygon(screen, tire_color_fl, [(1030, 170), (1030, 220), (1045, 220), (1045, 170)], 6)

    # Drawing two vertical lines on hud
    pygame.draw.line(screen, GREEN, [285, 100], [285, 620], 2)
    pygame.draw.line(screen, GREEN, [995, 100], [995, 620], 2)
    # Displaying text of MPH and RPM with actual numbers
    veh_speed((v_speed_string + " MPH"), GREEN)
    veh_rpm((v_rpm_string + " RPM"), GREEN)
    # Displays time
    draw_time(current_time, GREEN)

    pygame.display.update()
    pygame.display.flip()