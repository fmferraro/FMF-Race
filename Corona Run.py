#Importando Bibliotecas necessárias para o jogo
import os
import sys
import pygame
from random import randint
from pygame import mixer

#Superfície do jogo
tamanho_tela = (600, 600)
superficie = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("FMF Game")#Título da tela do jogo
CINZA=(127, 127, 127)  #Cor de fundo
FPS = 65
#velocidade= 0.2

#Classes do jogo

class Fundo_intro(pygame.sprite.Sprite):
    def __init__(self,texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8, cor_da_letra, tamanho_do_titulo,tamanho_da_instrucao, cor_fundo):
        tela_jogo2 = pygame.display.set_mode(tamanho_tela)
        tela_jogo2.fill(cor_fundo)
        self.fonte_texto1 = pygame.font.SysFont(None, tamanho_do_titulo)
        self.superficie1 = self.fonte_texto1.render(texto1, True, cor_da_letra)
        tela_jogo2.blit(self.superficie1, ((tela_jogo2.get_width()-self.superficie1.get_width())/2, 60))
        self.fonte_texto2 = pygame.font.SysFont(None, tamanho_do_titulo)
        self.superficie2 = self.fonte_texto2.render(texto2, True, cor_da_letra)
        tela_jogo2.blit(self.superficie2, ((tela_jogo2.get_width()-self.superficie2.get_width())/2, 120))
        self.fonte_texto3 = pygame.font.SysFont(None, tamanho_do_titulo)
        self.superficie3 = self.fonte_texto3.render(texto3, True, cor_da_letra)
        tela_jogo2.blit(self.superficie3, ((tela_jogo2.get_width()-self.superficie3.get_width())/2, 180))
        self.fonte_texto4 = pygame.font.SysFont(None, tamanho_da_instrucao)
        self.superficie4 = self.fonte_texto4.render(texto4, True, cor_da_letra)
        tela_jogo2.blit(self.superficie4, ((tela_jogo2.get_width()-self.superficie3.get_width())/2, 300))
        self.fonte_texto5 = pygame.font.SysFont(None, tamanho_da_instrucao)
        self.superficie5 = self.fonte_texto5.render(texto5, True, cor_da_letra)
        tela_jogo2.blit(self.superficie5, ((tela_jogo2.get_width()-self.superficie5.get_width())/2, 360))
        self.fonte_texto6 = pygame.font.SysFont(None, tamanho_da_instrucao)
        self.superficie6 = self.fonte_texto6.render(texto6, True, cor_da_letra)
        tela_jogo2.blit(self.superficie6, ((tela_jogo2.get_width()-self.superficie6.get_width())/2, 420))
        self.fonte_texto7 = pygame.font.SysFont(None, tamanho_da_instrucao)
        self.superficie7 = self.fonte_texto7.render(texto7, True, cor_da_letra)
        tela_jogo2.blit(self.superficie7, ((tela_jogo2.get_width()-self.superficie7.get_width())/2, 480))
        self.fonte_texto8 = pygame.font.SysFont(None, tamanho_da_instrucao)
        self.superficie8 = self.fonte_texto8.render(texto8, True, cor_da_letra)
        tela_jogo2.blit(self.superficie8, ((tela_jogo2.get_width()-self.superficie8.get_width())/2, 540))
        pygame.display.update()

class Fundo(pygame.sprite.Sprite):
    def __init__(self,velocidade_fundo):
        super().__init__()
        img_dir = os.path.join(os.path.dirname(__file__), 'Imagens')
        try: #tenta ler os arquivos
            self.image = pygame.image.load(os.path.join(img_dir,'road.png'))
        except pygame.error: #Se der errado
            print("Erro ao tentar ler a imagem do fundo") #Avisa se der errado
            sys.exit() #Sai pela rotina do sistema
        self.image = pygame.transform.scale(self.image, (600, 600)).convert()
        self.rect = self.image.get_rect()
        self.velocidade_fundo = velocidade_fundo

    def update(self):
        self.velocidade_fundo -= 0
        self.rel_y = self.velocidade_fundo % self.rect.height
        self.superficieblit = superficie.blit(self.image,(self.rel_y-self.rect.height ,0))
        if self.rel_y < 600:
            self.tela_jogoblit = superficie.blit(self.image,(self.rel_y,0))

    def go_fundo(self):
        self.update()


class Police(pygame.sprite.Sprite):

    def __init__(self,velocidade, posX_police, posY_police):
        super().__init__()
        img_dir = os.path.join(os.path.dirname(__file__), 'Imagens')
        try:
            self.image = pygame.image.load(os.path.join(img_dir,'police.png')).convert_alpha()     
        except pygame.error:
            print('Erro ao tentar ler imagem: police.png')
            sys.exit()

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(200,100)).convert_alpha()
        self.rect.x = posX_police
        self.rect.y = posY_police
        self.velocidade_police = velocidade    

    def update(self, delta_time):
        
        largura, altura = pygame.display.get_surface().get_size()
        self.rect.y += self.velocidade_police * delta_time

        if self.rect.y > 2000:
            self.rect.y = 0
            self.rect.x = randint(80, 320)
            self.rect.y += self.velocidade_police * delta_time

class Oil(pygame.sprite.Sprite):

    def __init__(self,velocidade, posX_oil, posY_oil):
        super().__init__()
        img_dir = os.path.join(os.path.dirname(__file__), 'Imagens')
        try:
            self.image = pygame.image.load(os.path.join(img_dir,'oil.png')).convert_alpha()     
        except pygame.error:
            print('Erro ao tentar ler imagem: enemy.png')
            sys.exit()

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(80,80)).convert_alpha()
        self.rect.x = posX_oil
        self.rect.y = posY_oil
        self.velocidade_oil = velocidade    

    def update(self, delta_time):
        
        largura, altura = pygame.display.get_surface().get_size()
        self.rect.y += self.velocidade_oil * delta_time

        if self.rect.y > 800:
            self.rect.y = 0
            self.rect.x = randint(80, 430)
            self.rect.y += self.velocidade_oil * delta_time

class Tree(pygame.sprite.Sprite):

    def __init__(self,velocidade, posX_tree, posY_tree):
        super().__init__()
        img_dir = os.path.join(os.path.dirname(__file__), 'Imagens')
        try:
            self.image = pygame.image.load(os.path.join(img_dir,'tree.png')).convert_alpha()     
        except pygame.error:
            print('Erro ao tentar ler imagem: enemy.png')
            sys.exit()

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(100,100)).convert_alpha()
        self.rect.x = posX_tree
        self.rect.y = posY_tree
        self.velocidade_tree = velocidade    

    def update(self, delta_time):
        
        largura, altura = pygame.display.get_surface().get_size()
        self.rect.y += self.velocidade_tree * delta_time

        if self.rect.y > 1600:
            self.rect.y = 0
            self.rect.x = randint(80, 430)
            self.rect.y += self.velocidade_tree * delta_time
            
            
#Função principal
def main():
    """Rotina principal do jogo"""
    
    pygame.init() #Inicia rotinas do pygame

    #Cores para o jogo
    CINZA = (127, 127, 127)
    AZUL = (0, 0, 255)
    AMARELO = (255, 255, 0)
    BRANCO = (255, 255, 255)



    #Superfície do jogo
    tamanho_tela = (600, 600)
    superficie = pygame.display.set_mode(tamanho_tela, pygame.RESIZABLE)
    pygame.display.set_caption("FMF Game")#Título da tela do jogo
    PRETO=(0, 0, 0)  #Cor de fundo
    FPS = 60

    #Placar de tempo
    font = pygame.font.SysFont("arial black", 25)
    texto = font.render("Tempo: ", True, (255,255,255), (0, 0, 0))
    pos_texto = texto.get_rect()
    pos_texto.center = (55, 15) 
    timer = 0
    tempo_segundo = 0

    # Fonte para a tela pausada
    font_pause = pygame.font.SysFont("arial black", 40)

    #Implementando Música de fundo
    musica=os.path.join("Sons", "MusicaFundo.oga")
    mixer.music.load(musica)
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

    #Altera a velocidade e posições iniciais dos sprites
    fundo = Fundo(0)
    """player = Player(0.2, 250, 400)"""
    police = Police(0.2, 200, 0) 
    oil = Oil(0.2, 430, 601)
    tree = Tree(0.2, 80, 701) 
    sprites = pygame.sprite.Group()
    """sprites.add(player)"""
    sprites.add(police)
    sprites.add(oil)
    sprites.add(tree)
    
    
    intro = Fundo_intro("Bem Vindo","ao","Corona Run","Vamos ver se você é um bom piloto...","Corra o maior tempo possível sem bater!","Caso encoste em um obstáculo, sua corrida acaba","Pressione DIREITA ou ESQUERDA para mover o carro","Pressione ENTER para continuar", (BRANCO), 80,30, (CINZA))


    #Arquivos
    img_dir = os.path.join(os.path.dirname(__file__), 'Imagens')

    #Tenta ler e implementa as imagens
    try:
        player=pygame.image.load(os.path.join(img_dir,'ferrari.png')).convert_alpha()
    except pygame.error: #Se der errado
        print("Erro ao tentar ler a imagem") #Avisa se der errado
        sys.exit() #Sai pela rotina do sistema
    player = pygame.transform.scale(player,(100,207)).convert_alpha()
    
    #Player
    pos_player = [250, 400] #max 410 min 90
    delta_player =  {"esquerda":0, "direita":0}
    vel_player = 0.2
    rect_player = player.get_rect()

    
    #Objeto para controle da atualizações de imagens
    clock = pygame.time.Clock() 
    FPS=60 #Velocidade que atualiza as imagens

    RODANDO = 0
    PAUSADO = 1

    jogo = RODANDO

    #Loop da tela inicial
    loop = True
    while loop:
        Intro = True
        while Intro:
            intro.__init__
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_RETURN]:
                    Intro = False
                elif event.type == pygame.QUIT:
                    pygame.quit()

        #Loop pricipal
        JOGANDO = True
        while JOGANDO:

            delta_time=clock.tick(FPS)

            #Eventos do jogo
            eventos=pygame.event.get()
            
            for evento in eventos:
                
                #Fecha o jogo
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                    pygame.quit() #Encerra a aplicação pygame
                    sys.exit() #Sai pela rotina do sistema

                #Controla o player
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        delta_player["esquerda"] = 1
                    if evento.key == pygame.K_RIGHT:
                        delta_player["direita"] = 1
                    #Pausa o jogo
                    if evento.key == pygame.K_p:
                        if jogo != PAUSADO:
                            mixer.music.pause()
                            pause = font_pause.render("PAUSE", True, PRETO, BRANCO)
                            superficie.blit(pause, ((superficie.get_width()-pause.get_width())/2, (superficie.get_height()-pause.get_height())/2))
                            jogo = PAUSADO
                        else:
                            mixer.music.unpause()
                            jogo = RODANDO

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        delta_player["esquerda"] = 0
                    if evento.key == pygame.K_RIGHT:
                        delta_player["direita"] = 0
            
            #Posição do player
            pos_player[0] += (delta_player["direita"] - delta_player["esquerda"]) * vel_player * delta_time

            #Placar de tempo
            if timer<60 and jogo!= PAUSADO:
                timer += 1
            elif timer>=60 and jogo!= PAUSADO:
                tempo_segundo += 1
                texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0, 0, 0))
                timer = 0
                    
            if jogo == PAUSADO:
                pygame.display.flip()
                continue

            #Preenche a tela com a cor definida
            superficie.fill(PRETO)
            
            
            #Desenha as imagens nas coordenadas determinadas
            fundo.go_fundo()
            sprites.update(delta_time)
            sprites.draw(superficie)
            superficie.blit(player, pos_player)
            superficie.blit(texto, pos_texto)


            #Faz a atualização da tela
            pygame.display.flip()
            pygame.display.update()

#Executa o jogo se for o arquivo correto
if __name__ == "__main__":
    main()