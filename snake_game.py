import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0 ,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

speed = 15
score = 0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not change_to == 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and not change_to == 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and not change_to == 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and not change_to == 'LEFT':
                change_to = 'RIGHT'
    

    snake_direction = change_to
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    if (snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or
            snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10):
        running = False
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False

    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Visa poäng
    font = pygame.font.SysFont('arial', 25)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, [10, 10])
    

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
