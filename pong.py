import pygame, sys, time, os

# setup inicial
pygame.init()
clock = pygame.time.Clock()

pygame.mixer.music.load('data\song-for-denise.mp3')
pygame.mixer.music.play(-1)

#cores
branco = (255,255,255)
red = (255, 0, 0)
preto = (0,0,0)
# janela
largura = 1280
altura = 720
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("PyPong by magoninho")

start_time = 300

pontos_p_1 = 0
pontos_p_2 = 0

#### CLASSES ####

class Player:
    def __init__(self, x, y, size_x, size_y, rect, s_vel):
        """
        Essa função é chamada quando o objeto Player é chamada

        Ex: player = Player(10, 10, 5, 5)
        agora a variavel player contem esse objeto inteiro
        Ex: player.pos_x, player.pos_y etc...
        """ 
        
        self.pos_x = x
        self.pos_y = y
        self.size_x = size_x
        self.size_y = size_y
        self.rect = rect
        self.s_vel = s_vel

    def drawPlayer(self):
        """
        Essa função vai ser executada no GAME LOOP para desenhar o player
        """
        pygame.draw.rect(screen, branco, self.rect)

    #Da para passar argumentos tbm, mas nunca esqueça do self antes, esse self é como se tivesse passando a variavel do player
    #Exemplo: player = Player(args**)
    #player.updatePlayer()
    #esse player antes do ponto é oque o self representa ali embaixo
    def updatePlayer(self, p):

        global moving_up1, moving_down1, moving_up2, moving_down2
        keys = pygame.key.get_pressed()
        if p == 1:
            # cima e baixo (apertando)
            if keys[pygame.K_w]:
                self.rect.y -= self.s_vel
            if keys[pygame.K_s]:
                self.rect.y += self.s_vel
                

            if self.rect.y > altura - 140:          ## colisões para nao sair do cenário
                self.rect.y = altura - 140
            if self.rect.y < 0:
                self.rect.y = 0
        if p == 2:  
            # cima e baixo (apertando)
            if keys[pygame.K_UP]:
                self.rect.y -= self.s_vel
            if keys[pygame.K_DOWN]:
                self.rect.y += self.s_vel

            if self.rect.y > altura - 140:          ## colisões para nao sair do cenário
                self.rect.y = altura - 140
            if self.rect.y < 0:
                self.rect.y = 0
class Bola:
    def __init__(self, x, y, rect, x_vel, y_vel, player1, player2):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.player1 = player1
        self.player2 = player2
        self.rect = rect
    def drawBola(self):
        pygame.draw.rect(screen, branco, self.rect)
    def animation(self):
        global pontos_p_1, pontos_p_2

        self.y_vel += 0.01
        if self.x_vel < 0:
            self.x_vel -= 0.01
        else:
            self.x_vel += 0.001

        if self.x_vel > 12:
            self.x_vel = 12

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.y <= 0 or self.rect.y > window_Height - 40:
            self.y_vel *= -1 ## MUDANÇA DE DIREÇÃO

        ###### GOLS dos jogadores ######
        
        if self.rect.x >= window_Width - 40: # GOL DO PLAYER 1
            ponto = pygame.mixer.Sound('data\ponto.wav')
            ponto.play()
            self.rect.x = largura / 2 - 20
            self.rect.y = altura / 2 - 20
            pontos_p_1 += 1
        if self.rect.x <= 0: # GOL DO PLAYER 2
            ponto = pygame.mixer.Sound('data\ponto.wav')
            ponto.play()
            self.rect.x = largura / 2 - 20
            self.rect.y = altura / 2 - 20
            pontos_p_2 += 1

        if self.rect.colliderect(self.player1):
            impacto = pygame.mixer.Sound('data\impacto1.wav')
            impacto.play()
            self.x_vel *= -1 ## MUDANÇA DE DIREÇÃO
        if self.rect.colliderect(self.player2):
            impacto = pygame.mixer.Sound('data\impacto2.wav')
            impacto.play()
            self.x_vel *= -1 ## MUDANÇA DE DIREÇÃO
# DESENHOS
rect_bola = pygame.Rect(largura/2 - 20, altura/2 - 20, 40, 40)
rect_player1 = pygame.Rect(15, 140, 25, 140)
rect_player2 = pygame.Rect(largura - 40, 140, 25, 140)
############################## ANIMAÇÃO DA BOLA ##############################

# pegando a altura para a bolinha colidir
window_Width = screen.get_width()
window_Height = screen.get_height()


#################################################################################



## INSTANCIAS ##
player1 = Player(15, altura/2 - 70, 25, 140, rect_player1, 8)
player2 = Player(largura - 40, altura/2 - 70, 25, 140, rect_player2, 8)
bola = Bola(largura/2 - 20, altura/2 - 20, rect_bola, 7, 7, player1, player2)

# movimentação dos jogadores

moving_up1 = False
moving_down1 = False
moving_up2 = False
moving_down2 = False
pode = True

## GAME LOOP ##
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Limpa a tela com a cor
    screen.fill(preto)

    # Linha divisória dos oponentes
    for c in range(0, 30):
        pygame.draw.rect(screen, branco, (largura/2 - 7.5, c*35, 15, 15))
    ###############################
    
    


    fonte = pygame.font.SysFont('Comic Sans MS', 48)
    texto1 = fonte.render(str(pontos_p_1), False, branco)
    screen.blit(texto1, (largura/2 - 200, 10))
    texto2 = fonte.render(str(pontos_p_2), False, branco)
    screen.blit(texto2, (largura/2 + 200, 10))
    # os jogadores

    #Atualiza os player
    #Todo //
    player1.updatePlayer(1)
    player2.updatePlayer(2)

    #Desenha os players
    player1.drawPlayer()
    player2.drawPlayer()


    #bola
    bola.drawBola()

    start_time -= 1
    
    if pode:
        segundos = fonte.render(str(start_time / 100), False, red)
        screen.blit(segundos, (largura/2 - 150, 200))
    if start_time <= 0:
        bola.animation()
        pode = False
    
    pygame.display.flip()
    clock.tick(60)
    
