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
snake_pos_1 = [100, 50]
snake_body_1 = [[100, 50], [90, 50], [80, 50]]
snake_direction_1 = 'RIGHT'
change_to_1 = snake_direction_1

snake_pos_2 = [200, 50]
snake_body_2 = [[200, 50], [190, 50], [180, 50]]
snake_direction_2 = 'RIGHT'
change_to_2 = snake_direction_2

# Matposition
food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
food_spawn = True

# Hastighet och poäng
speed = 15
score_1 = 0
score_2 = 0

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

# Huvudmeny
def main_menu():
    while True:
        screen.fill((0, 0, 0))
        show_text("Snake Game", 50, (0, 255, 0), WIDTH // 4, HEIGHT // 4)
        show_text("1. Start Game", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2)
        show_text("2. View Highscore", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2 + 40)
        show_text("3. Exit", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2 + 80)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Start Game
                    choose_players()
                if event.key == pygame.K_2:  # View Highscore
                    show_highscore()
                if event.key == pygame.K_3:  # Exit
                    pygame.quit()
                    sys.exit()

# Spela med 1 eller 2 spelare
def choose_players():
    global speed
    while True:
        screen.fill((0, 0, 0))
        show_text("Choose Players", 40, (0, 255, 0), WIDTH // 4, HEIGHT // 4)
        show_text("1. One Player", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2)
        show_text("2. Two Players", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2 + 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # One Player
                    choose_difficulty(1)
                if event.key == pygame.K_2:  # Two Players
                    choose_difficulty(2)

# Välj svårighetsgrad
def choose_difficulty(players):
    global speed
    while True:
        screen.fill((0, 0, 0))
        show_text("Choose Difficulty", 40, (0, 255, 0), WIDTH // 4, HEIGHT // 4)
        show_text("1. Easy", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2)
        show_text("2. Medium", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2 + 40)
        show_text("3. Hard", 30, (255, 255, 255), WIDTH // 4, HEIGHT // 2 + 80)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Easy
                    speed = 10
                    main(players)
                if event.key == pygame.K_2:  # Medium
                    speed = 15
                    main(players)
                if event.key == pygame.K_3:  # Hard
                    speed = 20
                    main(players)

# Visa Highscore
def show_highscore():
    while True:
        screen.fill((0, 0, 0))
        show_text("Highscore", 50, (255, 255, 0), WIDTH // 3, HEIGHT // 4)
        show_text(f"Highscore: {highscore}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 2)
        show_text("Press B to go back", 20, (255, 255, 255), WIDTH // 3, HEIGHT // 1.5)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  # Back to Main Menu
                    return

# Game Over-funktion
def game_over():
    global highscore

    # Uppdatera highscore om nödvändigt
    if score_1 > highscore:
        highscore = score_1
        with open(highscore_file, "w") as f:
            f.write(str(highscore))
    if score_2 > highscore:
        highscore = score_2
        with open(highscore_file, "w") as f:
            f.write(str(highscore))

    # Visa Game Over-skärm
    screen.fill((0, 0, 0))
    show_text("Game Over", 50, (255, 0, 0), WIDTH // 3, HEIGHT // 4)
    show_text(f"Player 1 Score: {score_1}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 3)
    show_text(f"Player 2 Score: {score_2}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 2)
    show_text(f"Highscore: {highscore}", 30, (255, 255, 255), WIDTH // 3, HEIGHT // 1.5)
    show_text("Press R to Restart or Q to Quit", 20, (255, 255, 255), WIDTH // 4, HEIGHT // 1.8)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main(1)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Huvudspel
def main(players):
    global snake_pos_1, snake_body_1, snake_direction_1, change_to_1, food_pos, food_spawn, score_1, snake_pos_2, snake_body_2, snake_direction_2, change_to_2, score_2

    # Återställ spelet
    snake_pos_1 = [100, 50]
    snake_body_1 = [[100, 50], [90, 50], [80, 50]]
    snake_direction_1 = 'RIGHT'
    change_to_1 = snake_direction_1

    if players == 2:
        snake_pos_2 = [200, 50]
        snake_body_2 = [[200, 50], [190, 50], [180, 50]]
        snake_direction_2 = 'RIGHT'
        change_to_2 = snake_direction_2

    food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
    food_spawn = True
    score_1 = 0
    score_2 = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Hantera tangentbord för spelare 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not change_to_1 == 'DOWN':
                    change_to_1 = 'UP'
                if event.key == pygame.K_DOWN and not change_to_1 == 'UP':
                    change_to_1 = 'DOWN'
                if event.key == pygame.K_LEFT and not change_to_1 == 'RIGHT':
                    change_to_1 = 'LEFT'
                if event.key == pygame.K_RIGHT and not change_to_1 == 'LEFT':
                    change_to_1 = 'RIGHT'

            # Hantera tangentbord för spelare 2
            if players == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and not change_to_2 == 'DOWN':
                        change_to_2 = 'UP'
                    if event.key == pygame.K_s and not change_to_2 == 'UP':
                        change_to_2 = 'DOWN'
                    if event.key == pygame.K_a and not change_to_2 == 'RIGHT':
                        change_to_2 = 'LEFT'
                    if event.key == pygame.K_d and not change_to_2 == 'LEFT':
                        change_to_2 = 'RIGHT'

        # Uppdatera riktning för spelare 1
        snake_direction_1 = change_to_1
        if snake_direction_1 == 'UP':
            snake_pos_1[1] -= 20
        if snake_direction_1 == 'DOWN':
            snake_pos_1[1] += 20
        if snake_direction_1 == 'LEFT':
            snake_pos_1[0] -= 20
        if snake_direction_1 == 'RIGHT':
            snake_pos_1[0] += 20

        # Växande orm för spelare 1
        snake_body_1.insert(0, list(snake_pos_1))

        # Kontrollera om ormens huvud träffar maten för spelare 1
        if abs(snake_pos_1[0] - food_pos[0]) < 20 and abs(snake_pos_1[1] - food_pos[1]) < 20:
            score_1 += 10
            food_spawn = False
        else:
            snake_body_1.pop()

        # Generera ny mat om den ätits
        if not food_spawn:
            food_pos = [random.randrange(0, (WIDTH // 20)) * 20, random.randrange(0, (HEIGHT // 20)) * 20]
            food_spawn = True

        # Kontrollera om ormen kolliderar med sig själv eller väggarna för spelare 1
        if snake_pos_1[0] < 0 or snake_pos_1[0] >= WIDTH or snake_pos_1[1] < 0 or snake_pos_1[1] >= HEIGHT:
            game_over()
        for block in snake_body_1[1:]:
            if snake_pos_1 == block:
                game_over()

        # Uppdatera riktning för spelare 2 (om två spelare)
        if players == 2:
            snake_direction_2 = change_to_2
            if snake_direction_2 == 'UP':
                snake_pos_2[1] -= 20
            if snake_direction_2 == 'DOWN':
                snake_pos_2[1] += 20
            if snake_direction_2 == 'LEFT':
                snake_pos_2[0] -= 20
            if snake_direction_2 == 'RIGHT':
                snake_pos_2[0] += 20

            # Växande orm för spelare 2
            snake_body_2.insert(0, list(snake_pos_2))

            # Kontrollera om ormens huvud träffar maten för spelare 2
            if abs(snake_pos_2[0] - food_pos[0]) < 20 and abs(snake_pos_2[1] - food_pos[1]) < 20:
                score_2 += 10
                food_spawn = False
            else:
                snake_body_2.pop()

            # Kontrollera om ormen kolliderar med sig själv eller väggarna för spelare 2
            if snake_pos_2[0] < 0 or snake_pos_2[0] >= WIDTH or snake_pos_2[1] < 0 or snake_pos_2[1] >= HEIGHT:
                game_over()
            for block in snake_body_2[1:]:
                if snake_pos_2 == block:
                    game_over()

        # Uppdatera skärmen
        screen.blit(background_image, (0, 0))
        for pos in snake_body_1:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))

        if players == 2:
            for pos in snake_body_2:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[1], 20, 20))

        screen.blit(apple_image, (food_pos[0], food_pos[1]))

        show_text(f"Player 1 Score: {score_1}", 20, (255, 255, 255), 10, 10)
        if players == 2:
            show_text(f"Player 2 Score: {score_2}", 20, (255, 255, 255), WIDTH - 200, 10)

        pygame.display.flip()
        clock.tick(speed)

# Starta spelet
main_menu()
