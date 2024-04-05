import pygame
import random

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 75
        self.speed = 1   #test 0.06

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed_x = 1 #test 0.06
        self.speed_y = 1

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def hit(self):
        self.x = -self.speed_x
        self.y = -self.speed_y

# Stats
class Stats:
    def __init__(self):
        self.bounce = 0
        self.score_left = 0
        self.score_right = 0

pygame.init()

# Set up the display
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Create the paddles and ball
paddle_left = Paddle(50, screen_height / 2 - 37)
paddle_right = Paddle(screen_width - 60, screen_height / 2 - 37)
ball = Ball(screen_width / 2, screen_height / 2)
stats = Stats()

def check_collision(ball, paddle):
    if (ball.x + ball.radius >= paddle.x and ball.x - ball.radius <= paddle.x + paddle.width) and (ball.y + ball.radius >= paddle.y and ball.y - ball.radius <= paddle.y + paddle.height):
        return True
    else:
        return False

# Font Object
font = pygame.font.Font('freesansbold.ttf', 20)

#screen.fill((0, 0, 0))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles and ball
    keys = pygame.key.get_pressed()
    # Auto Play---
    if (ball.y < paddle_right.y + paddle_right.height * 0.5 and paddle_right.y >= 0):
       paddle_right.move_up()
    elif (ball.y > paddle_right.y + paddle_right.height * 0.5 and paddle_right.y + paddle_right.height <= screen_height):
        paddle_right.move_down()

    if (ball.y <= paddle_left.y + paddle_left.height * 0.5 and paddle_left.y >= 0):
       paddle_left.move_up()
    elif (ball.y > paddle_left.y + paddle_left.height * 0.5 and paddle_left.y + paddle_left.height <= screen_height):
        paddle_left.move_down()
    # ---
    if keys[pygame.K_w]:
        paddle_left.move_up()
    if keys[pygame.K_s]:
        paddle_left.move_down()
    if keys[pygame.K_UP]:
        paddle_right.move_up()
    if keys[pygame.K_DOWN]:
        paddle_right.move_down()

    # Collision Paddle
    if check_collision(ball, paddle_right) or check_collision(ball, paddle_left):
        if ball.speed_x < 0:
            #ball.speed_x -= 0.03
            ball.radius += 0.1
        else:
            #ball.speed_x += 0.03
            ball.radius += 0.1
            
        ball.speed_x = -ball.speed_x
        stats.bounce = stats.bounce + 1
    # Collision Screen
    if (ball.y + ball.radius >= screen_height and ball.y - ball.radius <= screen_height) or (ball.y + ball.radius >= 0 and ball.y - ball.radius <= 0):
        ball.speed_y = -ball.speed_y
        stats.bounce = stats.bounce + 1
    # Score Point
    if (ball.x - ball.radius <= 0):
        stats.score_right += 1
        ball.speed_x = 0.2
        ball.x = screen_width / 2
        ball.y = screen_height / 2
    if (ball.x + ball.radius >= screen_width):
        stats.score_left += 1
        ball.speed_x = 0.2
        ball.x = screen_width / 2
        ball.y = screen_height / 2
    

    ball.move()

    # Text Font (for Bounce Count)
    text_bounce = font.render('Bounces ' + str(stats.bounce), True, (0, 255, 0), (0, 0, 128))
    text_score = font.render(str(stats.score_right) + " vs " + str(stats.score_left), True, (0, 255, 0), (0, 0, 128))
    text_speed = font.render("Speed " + str(ball.speed_x), True, (0, 255, 0), (0, 0, 128))
    text_radius = font.render("Radius " + str(ball.radius), True, (0, 255, 0), (0, 0, 128))

    textRect_bounce = text_bounce.get_rect()
    textRect_score = text_score.get_rect()
    textRect_speed = text_speed.get_rect()
    textRect_radius = text_radius.get_rect()

    textRect_bounce.center = (screen_width // 2, screen_height * 0.025)
    textRect_score.center = (screen_width // 2, screen_height * 0.075)
    textRect_speed.center = (screen_width // 2, screen_height * 0.125)
    textRect_radius.center = (screen_width // 2, screen_height * 0.175)

    #color
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)

    # Draw the paddles and ball
    screen.fill((0, 0, 0))
    screen.blit(text_bounce, textRect_bounce)
    screen.blit(text_score, textRect_score)
    screen.blit(text_speed, textRect_speed)
    screen.blit(text_radius, textRect_radius)
    pygame.draw.rect(screen, (255, 255, 255), (paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height))
    pygame.draw.circle(screen, (red, blue, green), (int(ball.x), int(ball.y)), ball.radius)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()