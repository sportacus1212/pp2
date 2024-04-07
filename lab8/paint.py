import pygame
pygame.init()

# Set up the screen dimensions
screen = pygame.display.set_mode((1080, 900))
pygame.display.set_caption("PAINT")

# Initialize the game clock
clock = pygame.time.Clock()

# Define color constants
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

# Load and scale the eraser image
eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (70, 70))

# Function to draw colored rectangles for color selection
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

# Function to pick the current drawing color based on mouse position
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
        elif 130 <= x <= 170 and 0 <= y <= 40:
            return "rect"
    return color

# Function to handle painting on the screen
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color != 'rect':
            # Draw a circle with the selected color
            pygame.draw.circle(screen, color, (x, y), 27)
        else:
            # Draw a white rectangle (eraser) if 'rect' color is selected
            pygame.draw.rect(screen, WHITE, (x, y, 40, 40), 4)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Draw color selection rectangles and eraser icon
    for i in range(len(colors)):
        draw_rect(i)
    screen.blit(eraser, (1010, 0))
    pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 4)

    # Get the current drawing color
    color = pick_color()

    # Handle painting on the screen
    painting(color)

    # Control the frame rate
    clock.tick(370)
    pygame.display.update()