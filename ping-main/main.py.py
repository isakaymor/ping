import pygame 
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ping Pong')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Variáveis da bola
bola_x = largura // 2
bola_y = altura // 2
bola_raio = 10
bola_vel_x = 5
bola_vel_y = 5

# Variáveis dos jogadores
largura_raquete = 10
altura_raquete = 100

# Jogador 1
jogador1_x = 10
jogador1_y = altura // 2 - altura_raquete // 2

# Jogador 2
jogador2_x = largura - largura_raquete - 10
jogador2_y = altura // 2 - altura_raquete // 2

velocidade_jogador = 7

# Placar
placar1 = 0
placar2 = 0
fonte = pygame.font.SysFont('Arial', 30)

# Relógio
clock = pygame.time.Clock()

# Loop principal
while True: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento dos jogadores
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and jogador1_y > 0:
        jogador1_y -= velocidade_jogador
    if teclas[pygame.K_s] and jogador1_y < altura - altura_raquete:
        jogador1_y += velocidade_jogador
    if teclas[pygame.K_UP] and jogador2_y > 0:
        jogador2_y -= velocidade_jogador
    if teclas[pygame.K_DOWN] and jogador2_y < altura - altura_raquete:
        jogador2_y += velocidade_jogador

    # Movimento da bola
    bola_x += bola_vel_x
    bola_y += bola_vel_y

    # Colisão com as bordas superiores e inferiores
    if bola_y - bola_raio <= 0 or bola_y + bola_raio >= altura:
        bola_vel_y *= -1

    # Colisão com as raquetes
    if (jogador1_x < bola_x - bola_raio < jogador1_x + largura_raquete and
        jogador1_y < bola_y < jogador1_y + altura_raquete):
        bola_vel_x *= -1

    if (jogador2_x < bola_x + bola_raio < jogador2_x + largura_raquete and
        jogador2_y < bola_y < jogador2_y + altura_raquete):
        bola_vel_x *= -1

    # Pontuação
    if bola_x < 0:
        placar2 += 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x *= -1
    if bola_x > largura:
        placar1 += 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x *= -1

    # Desenhar tudo
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, (jogador1_x, jogador1_y, largura_raquete, altura_raquete))
    pygame.draw.rect(tela, BRANCO, (jogador2_x, jogador2_y, largura_raquete, altura_raquete))
    pygame.draw.circle(tela, BRANCO, (bola_x, bola_y), bola_raio)

    # Mostrar o placar
    texto = fonte.render(f"{placar1}   {placar2}", True, BRANCO)
    tela.blit(texto, (largura//2 - texto.get_width()//2, 20))

    pygame.display.flip()
    clock.tick(60)