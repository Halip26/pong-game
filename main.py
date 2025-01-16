import pygame
import random

# Initialize Pygame
pygame.init()

# Initialize mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load("music/space-120280.mp3")
pygame.mixer.music.set_volume(0.1)  # Set the volume to 10%
pygame.mixer.music.play(-1)  # Play the music in loop

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
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
start_time = pygame.time.get_ticks()  # Start time


# Function to display text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# Function to reset the game
def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, paddle1_dy, paddle2_dy, score1, score2, start_time
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
    paddle1_y, paddle2_y = (
        HEIGHT // 2 - paddle_height // 2,
        HEIGHT // 2 - paddle_height // 2,
    )
    paddle1_dy, paddle2_dy = 0, 0
    score1, score2 = 0, 0
    start_time = pygame.time.get_ticks()
    # play the music
    pygame.mixer.music.play()


# Function to display welcome screen
def welcome_screen():
    window.fill(BLACK)
    draw_text("Welcome to Pong Game", font, WHITE, window, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("by Mr. Halip", font, GREEN, window, WIDTH // 2, HEIGHT // 2 - 20)
    draw_text(
        "Press any key to start", font, YELLOW, window, WIDTH // 2, HEIGHT // 2 + 50
    )
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                reset_game()
                game_loop()


# Function to display player one wins
def playerone_wins():
    window.fill(BLACK)
    draw_text("Game Over", font, WHITE, window, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("Player one wins!", font, BLUE, window, WIDTH // 2, HEIGHT // 2 - 20)

    # Still show the scores at top screen
    draw_text(f"Player one: {score1}", font, BLUE, window, WIDTH // 4, 30)
    draw_text(f"Player two: {score2}", font, RED, window, 3 * WIDTH // 4, 30)

    draw_text(
        "Press Esc key to exit", font, YELLOW, window, WIDTH // 2, HEIGHT // 2 + 50
    )
    draw_text(
        "Press Space key to play again",
        font,
        GREEN,
        window,
        WIDTH // 2,
        HEIGHT // 2 + 85,
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


# Function to display player two wins
def playertwo_wins():
    window.fill(BLACK)
    draw_text("Game Over", font, WHITE, window, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("Player two wins!", font, RED, window, WIDTH // 2, HEIGHT // 2 - 25)

    # Still show the scores at top screen
    draw_text(f"Player one: {score1}", font, BLUE, window, WIDTH // 4, 30)
    draw_text(f"Player two: {score2}", font, RED, window, 3 * WIDTH // 4, 30)

    draw_text(
        "Press Esc key to exit", font, YELLOW, window, WIDTH // 2, HEIGHT // 2 + 50
    )
    draw_text(
        "Press Space key to play again",
        font,
        GREEN,
        window,
        WIDTH // 2,
        HEIGHT // 2 + 85,
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


# Function to display tie screen
def tie_screen():
    window.fill(BLACK)
    draw_text("TIE", font, WHITE, window, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text(
        f"Player one: {score1} | Player two: {score2}",
        font,
        YELLOW,
        window,
        WIDTH // 2,
        HEIGHT // 2,
    )

    draw_text(
        "Press Esc key to exit", font, YELLOW, window, WIDTH // 2, HEIGHT // 2 + 50
    )
    draw_text(
        "Press Space key to play again",
        font,
        GREEN,
        window,
        WIDTH // 2,
        HEIGHT // 2 + 85,
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


# Main game loop
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, paddle1_dy, paddle2_dy, score1, score2
    running = True
    clock = pygame.time.Clock()
    countdown_time = 120

    while running:
        current_time = pygame.time.get_ticks()  # Current time
        elapsed_time = (current_time - start_time) // 1000  # Elapsed time in seconds

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

        # update the countdown timer
        countdown_time -= 1 / 60

        # Clear the screen
        window.fill(BLACK)

        # Draw paddles and ball
        pygame.draw.rect(window, BLUE, (0, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(
            window, RED, (WIDTH - paddle_width, paddle2_y, paddle_width, paddle_height)
        )
        # the pong ball
        pygame.draw.circle(window, YELLOW, (ball_x, ball_y), ball_radius)

        # Draw scores
        draw_text(f"Player one: {score1}", font, BLUE, window, WIDTH // 4, 30)
        draw_text(f"Player two: {score2}", font, RED, window, 3 * WIDTH // 4, 30)

        # Draw countdown timer
        minutes = int(countdown_time) // 60
        seconds = int(countdown_time) % 60
        draw_text(f"{minutes:02}:{seconds:02}", font, WHITE, window, WIDTH // 2, 30)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

        # Check for game over or tie
        if score1 >= 5:
            elapsed_time = 0
            pygame.mixer.music.stop()
            playerone_wins()
            running = False

        if score2 >= 5:
            elapsed_time = 0
            pygame.mixer.music.stop()
            playertwo_wins()
            running = False

        if elapsed_time >= 120:  # 2 minutes = 120 seconds
            if score1 == score2:
                pygame.mixer.music.stop()
                tie_screen()
            running = False

    pygame.quit()


# Run the game
welcome_screen()
game_loop()
