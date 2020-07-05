import pygame, sys

# setup inicial
pygame.init()
clock = pygame.time.Clock()

#cores
branco = (255,255,255)
preto = (0,0,0)
# janela
largura = 1280
altura = 720
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("PyPong by magoninho")

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
    def updatePlayer(self):

        global moving_up, moving_down

        # cima e baixo (apertando)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        
        # cima e baixo (soltando a tecla)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False

        if moving_up == True:
            self.rect.y -= self.s_vel
        if moving_down == True:
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
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.y <= 0 or self.rect.y > window_Height - 40:
            self.y_vel *= -1 ## MUDANÇA DE DIREÇÃO

        ###### GOLS dos jogadores ######
        
        if self.rect.x >= window_Width - 40: 
            self.rect.x = largura / 2 - 20
            self.rect.y = altura / 2 - 20

        if self.rect.x <= 0: # GOL DO PLAYER 2
            self.rect.x = largura / 2 - 20
            self.rect.y = altura / 2 - 20


        if self.rect.colliderect(self.player1) or self.rect.colliderect(self.player2):
            self.x_vel *= -1 ## MUDANÇA DE DIREÇÃO

# DESENHOS
rect_bola = pygame.Rect(largura/2 - 20, altura/2 - 20, 40, 40)
rect_player1 = pygame.Rect(15, 70, 25, 140)
rect_player2 = pygame.Rect(largura - 40, 70, 25, 140)
############################## ANIMAÇÃO DA BOLA ##############################


# pegando a altura para a bolinha colidir
window_Width = screen.get_width()
window_Height = screen.get_height()


#################################################################################

## INSTANCIAS ##
player1 = Player(15, altura/2 - 70, 25, 140, rect_player1, 7)
player2 = Player(largura - 40, altura/2 - 70, 25, 140, rect_player2, 7)
bola = Bola(largura/2 - 20, altura/2 - 20, rect_bola, 7, 7, player1, player2)

# movimentação dos jogadores

moving_up = False
moving_down = False


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
    texto1 = fonte.render("0", False, branco)
    screen.blit(texto1, (largura/2 - 200, 10))
    texto2 = fonte.render("0", False, branco)
    screen.blit(texto2, (largura/2 + 200, 10))
    # os jogadores

    #Atualiza os player
    #Todo //
    player1.updatePlayer()
    player2.updatePlayer()

    #Desenha os players
    player1.drawPlayer()
    player2.drawPlayer()


    #bola
    bola.drawBola()
    bola.animation()





    pygame.display.flip()
    clock.tick(60)