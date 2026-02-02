import pygame
import random
import os

# Initialize Pygame
pygame.init()

try:
    # Initialize mixer
    pygame.mixer.init()

    # Load music file
    BG_SOUND = pygame.mixer.Sound("assets/music/space-120280.mp3")
    BG_SOUND.set_volume(0.5)  # Set the volume to 50%
except Exception as ds:
    print("Warning: Sound disabled:", ds)
    BG_SOUND = None

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Constants
INTRO_BG = pygame.image.load(os.path.join("assets/images/bg_pong_game.png"))
WIN_BG = pygame.image.load(os.path.join("assets/images/bg_pong_game.png"))
TIE_BG = pygame.image.load(os.path.join("assets/images/bg_pong_game.png"))

# Scale image to fit the window
SET_BG = pygame.transform.scale(INTRO_BG, (WIDTH, HEIGHT))
SET_BG_WIN = pygame.transform.scale(WIN_BG, (WIDTH, HEIGHT))
SET_BG_TIE = pygame.transform.scale(TIE_BG, (WIDTH, HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (245, 194, 66)
GREEN = (66, 245, 81)
BLUE = (18, 172, 255)
RED = (255, 18, 93)

# Set up game variables
ball_radius = 15
paddle_width, paddle_height = 140, 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-5, 5]), -5
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 50
paddle_speed = 6
score = 0
font = pygame.font.Font(None, 36)
start_time = pygame.time.get_ticks()  # Start


# Function to display text
def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(None, size)
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# Function to display welcome screen
def welcome_screen():
    # Set the background of welcome screen
    window.blit(SET_BG, (0, 0))

    # Add semi-transparent overlay to make text more readable
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(100)  # 128 is semi-transparent
    window.blit(overlay, (0, 0))

    draw_text("Welcome to Pong Game", 60, WHITE, window, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("by Raka", 36, GREEN, window, WIDTH // 2, HEIGHT // 2 - 10)
    draw_text(
        "Press any key to start", 36, YELLOW, window, WIDTH // 2, HEIGHT // 2 + 50
    )
    pygame.display.flip()
    BG_SOUND.play()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                BG_SOUND.stop()
                # reset_game()
                game_loop()


# Function to display player's score
def player_wins():

    # Set the background of win screen
    window.blit(SET_BG_WIN, (0, 0))

    # Add semi-transparent overlay to make text more readable
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(100)  # 128 is semi-transparent
    window.blit(overlay, (0, 0))

    draw_text("Game Over", 72, RED, window, WIDTH // 2, HEIGHT // 2 - 70)
    draw_text(f"Final Score: {score}", 45, BLUE, window, WIDTH // 2, HEIGHT // 2 - 5)

    draw_text("Press Esc key to exit", 30, RED, window, WIDTH // 2, HEIGHT // 2 + 60)
    draw_text(
        "Press Space key to play again",
        30,
        GREEN,
        window,
        WIDTH // 2,
        HEIGHT // 2 + 95,
    )
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                # set to play again
                elif event.key == pygame.K_SPACE:
                    waiting = False
                    reset_game()
                    welcome_screen()


# Function to reset the game
def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, score
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
    ball_dx, ball_dy = random.choice([-5, 5]), -5
    paddle_x = WIDTH // 2 - paddle_width // 2
    score = 0
    BG_SOUND.play()  # play the music


# Main game loop
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, score
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and paddle_x > 0:
            paddle_x -= paddle_speed
        if (
            keys[pygame.K_RIGHT] or keys[pygame.K_d]
        ) and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top, right, and left walls
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_dx = -ball_dx

        if ball_y - ball_radius <= 0:
            ball_dy = -ball_dy

        # Ball collision with paddles
        if (
            ball_y + ball_radius >= paddle_y
            and paddle_x <= ball_x <= paddle_x + paddle_width
        ):

            ball_dy = -abs(ball_dy)
            score += 1
            ball_dx *= 1.02
            ball_dy *= 1.02

        # Ball goes out of bounds
        if ball_y > HEIGHT:
            if BG_SOUND:
                BG_SOUND.stop()
            player_wins()
            running = False

        # Clear the screen
        window.fill(BLACK)

        # Draw paddles and ball
        pygame.draw.rect(
            window, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height)
        )

        # The pong ball
        pygame.draw.circle(window, YELLOW, (ball_x, ball_y), ball_radius)

        # Draw scores
        draw_text(f"Score: {score}", 36, WHITE, window, WIDTH // 2, 60)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

        # Check for the player's score
        if ball_y > HEIGHT:
            BG_SOUND.stop()
            player_wins()
            running = False


welcome_screen()
pygame.quit()
