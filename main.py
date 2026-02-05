import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check_line(p, a, b):
    return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)

def test_check_line():
    val = check_line(Point(250, 250), Point(0, 250), Point(500, 250))
    assert(val == 0)

    val = check_line(Point(250, 150), Point(0, 250), Point(500, 250))
    assert(val < 0)

    val = check_line(Point(250, 350), Point(0, 250), Point(500, 250))
    assert (val > 0)

def draw_line_1(surf, x0, x1, y0, y1, color):
    y = y0
    for x in range(x0, x1):
        surf.set_at((x, y), color)
        if check_line(Point(x + 1, y + 0.5), Point(x0, y0), Point(x1,  y1)) < 0:
            y += 1

def draw_line_gradient(surf, a, b, color_a, color_b):
    y = a.y
    for x in range(a.x, b.x):
        denom = (a.x - b.x)
        if denom == 0.0:
            t_x = 1.0
        else:
            t_x = (a.x - x) / (a.x - b.x)
        denom = (a.y - b.y)
        if denom == 0.0:
            t_y = 1.0
        else:
            t_y = (a.y - y) / (a.y - b.y)

        t = (t_x + t_y) / 2.0

        red = color_a[0] * (1 - t) + color_b[0] * t
        green = color_a[1] * (1 - t) + color_b[1] * t
        blue = color_a[2] * (1 - t) + color_b[2] * t

        surf.set_at((x, y), (red, green, blue))

        if check_line(Point(x + 1, y + 0.5), a, b) < 0:
            y += 1

def draw_triangle(surf, a, b, c, color):
    min_x = min(a.x, b.x, c.x)
    max_x = max(a.x, b.x, c.x)
    min_y = min(a.y, b.y, c.y)
    max_y = max(a.y, b.y, c.y)

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if check_line(Point(x, y), a, b) < 0:
                continue
            if check_line(Point(x, y), b, c) < 0:
                continue
            if check_line(Point(x, y), c, a) < 0:
                continue
            surf.set_at((x, y), color)


# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello Pygame")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    #draw_line_1(screen, 0, 500, 250, 250, (0, 0, 0))

    #draw_triangle(screen, Point(100, 100), Point(300, 200), Point(150, 350), (0, 0, 0))

    draw_line_gradient(screen, Point(0, 250), Point(500, 250), (0, 0, 0,), (255, 0, 0))
    pygame.display.update()

# Quit Pygame
pygame.quit()
