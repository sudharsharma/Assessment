import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Dinosaur settings
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = HEIGHT - dino_height - 50
dino_velocity_y = 0
is_jumping = False
gravity = 1
jump_force = -15

# Obstacle settings
obstacle_width = 20
obstacle_height = 50
obstacle_speed = 7
obstacles = []

# Score settings
score = 0
font = pygame.font.SysFont('Arial', 24)

# Game loop flag
run = True
game_over = False  # New flag to indicate game over

# Function to create obstacles
def create_obstacle():
    x = WIDTH + random.randint(0, 300)
    y = HEIGHT - obstacle_height - 50
    return pygame.Rect(x, y, obstacle_width, obstacle_height)

# Start with one obstacle
obstacles.append(create_obstacle())

# Main game loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not game_over:
        # Handle jumping
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            dino_velocity_y = jump_force

        # Apply gravity
        if is_jumping:
            dino_velocity_y += gravity
            dino_y += dino_velocity_y
            if dino_y >= HEIGHT - dino_height - 50:
                dino_y = HEIGHT - dino_height - 50
                is_jumping = False
                dino_velocity_y = 0

        # Move and manage obstacles
        for obstacle in obstacles:
            obstacle.x -= obstacle_speed

        # Remove obstacles that went off-screen
        obstacles = [ob for ob in obstacles if ob.x + ob.width > 0]

        # Add new obstacles
        if len(obstacles) == 0 or obstacles[-1].x < WIDTH - 200:
            obstacles.append(create_obstacle())

        # Check for collision
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        for obstacle in obstacles:
            if dino_rect.colliderect(obstacle):
                game_over = True  # Set game over flag
                break

        # Update score
        score += 1

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, dino_rect)  # Dino
        for obstacle in obstacles:
            pygame.draw.rect(screen, GREEN, obstacle)  # Obstacles

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (WIDTH - 150, 10))

    else:
        # Display Game Over message
        screen.fill(WHITE)
        game_over_font = pygame.font.SysFont('Arial', 48)
        game_over_text = game_over_font.render("Game Over", True, BLACK)
        final_score_text = font.render(f"Final Score: {score}", True, BLACK)
        restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)

        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 3))
        screen.blit(final_score_text, ((WIDTH - final_score_text.get_width()) // 2, HEIGHT // 2))
        screen.blit(restart_text, ((WIDTH - restart_text.get_width()) // 2, HEIGHT // 2 + 40))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game variables
            dino_y = HEIGHT - dino_height - 50
            dino_velocity_y = 0
            is_jumping = False
            obstacles = [create_obstacle()]
            score = 0
            game_over = False
        elif keys[pygame.K_q]:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()