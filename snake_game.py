import pygame
import sys
import random
import os

# Initiera Pygame
pygame.init()

# Skärminställningar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Ladda bakgrundsbild (gräsmatta)
background_image = pygame.image.load("grass_background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Ladda äpplebild
apple_image = pygame.image.load("apple.png")
apple_image = pygame.transform.scale(apple_image, (20, 20))

# Ormens startposition och storlek
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Matposition
food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
food_spawn = True

# Hastighet och poäng
speed = 15
score = 0

# Highscore hantering
highscore_file = "highscore.txt"
if not os.path.exists(highscore_file):
    with open(highscore_file, "w") as f:
        f.write("0")

with open(highscore_file, "r") as f:
    highscore = int(f.read())

# Funktion för att visa text
def show_text(text, size, color, x, y):
    font = pygame.font.SysFont('arial', size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Game Over-funktion
def game_over():
    global highscore

    # Uppdatera highscore om nödvändigt
    if score > highscore:
        highscore = score
        with open(highscore_file, "w") as f:
            f.write(str(highscore))

    # Visa Game Over-skärm
    screen.fill((0, 0, 0))
    show_text("Game Over", 50, (255, 0, 0), WIDTH // 3, HEIGHT // 4)
    show_text(f"Your Score: {score}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 3)
    show_text(f"Highscore: {highscore}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 2)
    show_text("Press R to Restart or Q to Quit", 20, (255, 255, 255), WIDTH // 4, HEIGHT // 1.5)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Huvudspel
def main():
    global snake_pos, snake_body, snake_direction, change_to, food_pos, food_spawn, score

    # Återställ spelet
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_direction = 'RIGHT'
    change_to = snake_direction
    food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
    food_spawn = True
    score = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Hantera tangentbord
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not change_to == 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and not change_to == 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and not change_to == 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and not change_to == 'LEFT':
                    change_to = 'RIGHT'

        # Uppdatera riktning
        snake_direction = change_to
        if snake_direction == 'UP':
            snake_pos[1] -= 20
        if snake_direction == 'DOWN':
            snake_pos[1] += 20
        if snake_direction == 'LEFT':
            snake_pos[0] -= 20
        if snake_direction == 'RIGHT':
            snake_pos[0] += 20

        # Växande orm
        snake_body.insert(0, list(snake_pos))

        # Kontrollera om ormens huvud träffar maten
        if abs(snake_pos[0] - food_pos[0]) < 20 and abs(snake_pos[1] - food_pos[1]) < 20:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Generera ny mat om den ätits
        if not food_spawn:
            food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
            food_spawn = True

        # Spelet över: träffar väggen eller sig själv
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
                snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            game_over()
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        # Rita skärmen
        screen.blit(background_image, (0, 0))
        for block in snake_body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(block[0], block[1], 20, 20))

        screen.blit(apple_image, (food_pos[0], food_pos[1]))

        # Visa poäng och highscore
        show_text(f"Score: {score}", 20, (255, 255, 255), 10, 10)
        show_text(f"Highscore: {highscore}", 20, (255, 255, 255), 10, 30)

        pygame.display.flip()
        clock.tick(speed)

# Starta spelet
if __name__ == "__main__":
    main()
