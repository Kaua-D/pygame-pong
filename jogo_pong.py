import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Raquetes
paddle_width, paddle_height = 15, 100
player1 = pygame.Rect(30, (HEIGHT - paddle_height) // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 30 - paddle_width, (HEIGHT - paddle_height) // 2, paddle_width, paddle_height)

# Bola
ball_size = 15
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_size, ball_size)
ball_speed_x = 5
ball_speed_y = 5

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += 5
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += 5

    # Movimentação da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisão com as paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Redesenhar a tela
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

    # Controle de FPS
    pygame.time.Clock().tick(60)

