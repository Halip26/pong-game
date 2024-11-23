import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (245, 194, 66)
GREEN = (66, 245, 81)
BLUE = (18, 172, 255)
RED = (255, 18, 93)

# Set up game variables
ball_radius = 15
paddle_width, paddle_height = 20, 100
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
paddle1_y, paddle2_y = (
    HEIGHT // 2 - paddle_height // 2,
    HEIGHT // 2 - paddle_height // 2,
)
paddle1_dy, paddle2_dy = 0, 0
paddle_speed = 6
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)


# Function to display text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# Function to display welcome screen
def welcome_screen():
    win.fill(BLACK)
    draw_text("Welcome to Pong Game", font, WHITE, win, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("by Mr. Halip", font, WHITE, win, WIDTH // 2, HEIGHT // 2 - 25)
    draw_text("Press any key to start", font, YELLOW, win, WIDTH // 2, HEIGHT // 2 + 50)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


# Main game loop
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, paddle1_dy, paddle2_dy, score1, score2
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_dy = -paddle_speed
                if event.key == pygame.K_s:
                    paddle1_dy = paddle_speed
                if event.key == pygame.K_UP:
                    paddle2_dy = -paddle_speed
                if event.key == pygame.K_DOWN:
                    paddle2_dy = paddle_speed
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle1_dy = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle2_dy = 0

        # Update paddle positions
        paddle1_y += paddle1_dy
        paddle2_y += paddle2_dy

        # Ensure paddles stay on screen
        paddle1_y = max(min(paddle1_y, HEIGHT - paddle_height), 0)
        paddle2_y = max(min(paddle2_y, HEIGHT - paddle_height), 0)

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top and bottom walls
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
            ball_dy = -ball_dy

        # Ball collision with paddles
        if (
            ball_x - ball_radius <= paddle_width
            and paddle1_y <= ball_y <= paddle1_y + paddle_height
        ) or (
            ball_x + ball_radius >= WIDTH - paddle_width
            and paddle2_y <= ball_y <= paddle2_y + paddle_height
        ):
            ball_dx = -ball_dx

        # Ball goes out of bounds
        if ball_x < 0:
            score2 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
        if ball_x > WIDTH:
            score1 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

        # Clear the screen
        win.fill(BLACK)

        # Draw paddles and ball
        pygame.draw.rect(win, BLUE, (0, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(
            win, RED, (WIDTH - paddle_width, paddle2_y, paddle_width, paddle_height)
        )
        pygame.draw.circle(win, YELLOW, (ball_x, ball_y), ball_radius)

        # Draw scores
        draw_text(f"Player one: {score1}", font, BLUE, win, WIDTH // 4, 30)
        draw_text(f"Player two: {score2}", font, RED, win, 3 * WIDTH // 4, 30)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# Run the game
welcome_screen()
game_loop()
