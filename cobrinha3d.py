import os
from random import randint
from random import randrange
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

largura, altura = 500, 500
widthMapa, heightMapa = 50, 50

anguloX = 0
anguloY = 0

angulo = 30
timer = 100

cobrinha = [(25, 25)]
cobrinha_direcao = (1, 0)

comida = (12, 23)
veneno = (50, 50)
super_comida = (50, 50)

objetosIniciados = False
jogoIniciado = False
jogoExecucao = False
jogoEncerrado = False

coordenadas_veneno = [(50, 50)]
x_envenenado = [50]
y_envenenado = [50]

desenha_veneno = False
envenenado = False

pontuacao = 0

def tecladoMovimentos(tecla, x, y):
    global jogoExecucao
    global anguloX, anguloY

    if (jogoExecucao):
        movimenta(1)

    if (tecla == b'w' or tecla == b'W'):
        anguloY -= 1
    elif (tecla == b's' or tecla == b'S'):
        anguloY += 1
    elif (tecla == b'a' or tecla == b'A'):
        anguloX -= 1
    elif (tecla == b'd' or tecla == b'D'):
        anguloX += 1

    parametrosVisualizacao()
    glutPostRedisplay()

def tecladoMovimentosTeclasEspeciais(tecla, x, y):
    global cobrinha_direcao

    if tecla == GLUT_KEY_UP:
        cobrinha_direcao = (0, 1)
    if tecla == GLUT_KEY_DOWN:
        cobrinha_direcao = (0, -1)
    if tecla == GLUT_KEY_LEFT:
        cobrinha_direcao = (-1, 0)
    if tecla == GLUT_KEY_RIGHT:
        cobrinha_direcao = (1, 0)

def gameOver():
    global jogoExecucao, jogoEncerrado

    jogoExecucao = False
    jogoEncerrado = True

def resetaEstados():
    global comida, envenenado, veneno
    global cobrinha, cobrinha_direcao
    global jogoExecucao, jogoEncerrado
    global t, x_envenenado, y_envenenado, coordenadas_veneno, objetosIniciados

    x_envenenado.clear()
    y_envenenado.clear()
    x_envenenado = [50]
    y_envenenado = [50]

    coordenadas_veneno.clear()
    coordenadas_veneno = [(50, 50)]

    comida = (12, 23)
    veneno = (50, 50)
    super_comida = (50, 50)

    cobrinha.clear()
    cobrinha = [(25, 25)]

    cobrinha_direcao = (1, 0)

    objetosIniciados = False
    envenenado = False
    desenha_veneno = False

    jogoIniciado = False
    jogoEncerrado = False
    jogoExecucao = False

    timer = 100

def reiniciarJogo():
    global jogoExecucao, jogoIniciado, pontuacao

    pontuacao = 0
    resetaEstados()
    jogoExecucao = True
    jogoIniciado = True

def movimenta(x):
    global comida, super_comida, veneno, envenenado
    global desenha_veneno, x_envenenado, y_envenenado
    global jogoEncerrado, jogoExecucao, jogoIniciado, objetosIniciados
    global pontuacao
    global timer

    novaPosicao = moveSnake(cobrinha[0], cobrinha_direcao)

    cobrinha.insert(0, novaPosicao)
    cobrinha.pop()

    (cabecaX, cabecaY) = cobrinha[0]

    for i in range(1, len(cobrinha)):
        coordenada_corpo = cobrinha[i]
        if cabecaX == coordenada_corpo[0] and cabecaY == coordenada_corpo[1]:
            print('Game Over: Bati no meu corpinho')
            gameOver()
            criaMenu()

    if not objetosIniciados and pontuacao == 0:
        objetosIniciados = True
        veneno = randint(1, 48), randint(1, 48)
        super_comida = randint(1, 48), randint(1, 48)

    if cabecaX == comida[0] and cabecaY == comida[1]:
        cobrinha.append(comida)
        comida = randint(1, 48), randint(1, 48)

        if randrange(5) == 2:
            desenha_veneno = True

        if randrange(7) == 5:
            super_comida = randint(1, 48), randint(1, 48)

        timer -= 2
        pontuacao += 10
        criaMenu()

    if cabecaX == super_comida[0] and cabecaY == super_comida[1]:
        desenha_veneno = True

        super_comida = [50, 50]
        if randrange(7) == 5:
            super_comida = randint(1, 48), randint(1, 48)

        cobrinha.append(super_comida)
        cobrinha.append(super_comida)
        cobrinha.append(super_comida)

        timer -= 2
        pontuacao += 20
        criaMenu()

    if cabecaX in x_envenenado:
        if cabecaY in y_envenenado:
            print('Game Over: Envenenado')
            gameOver()
            envenenado = True
            criaMenu()

    if cabecaY in y_envenenado:
        if cabecaX in x_envenenado:
            print('Game Over: Envenenado')
            gameOver()
            envenenado = True
            criaMenu()

    if jogoExecucao:
        glutTimerFunc(timer, movimenta, 1)
    elif jogoEncerrado:
        print("Jogo encerrado")


def moveSnake(ponto1, ponto2):
    global jogoExecucao, jogoEncerrado
    x = ponto1[0] + ponto2[0]
    y = ponto1[1] + ponto2[1]

    if x >= 49 or y >= 49 or x <= 0 or y <=0:
        print('Game Over: Bati nas bordas')
        gameOver()

    return (x, y)

def desenhaComidas():
    glColor3f(1.0, 1.0, 0.0)
    desenhaCorpo(comida[0], comida[1], 1, 1)

def desenhaSuperComida():
    glColor3f(1.0, 0.7, 0.0)
    desenhaCorpo(super_comida[0], super_comida[1], 1, 1)

def desenhaVeneno():
    global coordenadas_veneno, x_envenenado, y_envenenado, desenha_veneno
    global comida, super_comida

    glColor3f(0, 0.8, 0.0)

    if desenha_veneno:
        desenha_veneno = False

        novo_x = randrange(50)
        novo_y = randrange(50)

        cordenada_ocupada = ([novo_x, novo_y] == comida or [novo_x, novo_y] == super_comida)

        while (cordenada_ocupada):
            cordenada_ocupada = ([novo_x, novo_y] == comida or [novo_x, novo_y] == super_comida)

            novo_x = randrange(50)
            novo_y = randrange(50)

        x_envenenado.append(novo_x)
        y_envenenado.append(novo_y)
        coordenadas_veneno.append([novo_x, novo_y])

    for x, y in coordenadas_veneno:
        desenhaCorpo(x, y, 1, 1)

def desenhaCobra():
    glColor3f(0.0, 0.7, 0.0)
    for x, y in cobrinha:
        desenhaCorpo(x, y, 1, 1)

def resetaMapa(largura, altura, larguraPosicaoMapa, alturaPosicaoMapa):
    glViewport(0, 0, largura, altura)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, larguraPosicaoMapa, 0.0, alturaPosicaoMapa, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def desenhaCorpo(x, y, largura, altura):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glTranslatef(x + largura, y, 0.0)
    glTranslatef(x + altura, y + altura, 0.0)
    glTranslatef(x, y + altura, 0.0)
    glutSolidCube(25.0)
    glPopMatrix()

def desenha():
    global anguloX, anguloY
    global comida, veneno, super_comida
    global jogoIniciado, jogoEncerrado, jogoExecucao, envenenado, desenha_veneno

    glClear(GL_COLOR_BUFFER_BIT)

    resetaMapa(largura, altura, widthMapa, heightMapa)

    parametrosVisualizacao()

    glRotated(anguloX, 0.0, 1.0, 0.0);
    glRotated(anguloY, 1.0, 0.0, 0.0);
    #Especifica sistema de coordenadas de projeção
    # if jogoIniciado == False:
    #   glMatrixMode(GL_PROJECTION);
    #   glLoadIdentity();
    #   #Especifica a projeção perspectiva
    #   gluPerspective(45, 1.1, 0.1, 600);
    #   #Especifica sistema de coordenadas do modelo
    #   glMatrixMode(GL_MODELVIEW);
    #   # Inicializa sistema de coordenadas do modelo
    #   glLoadIdentity();
    #   #Especifica posição do observador e do alvo
    #   # gluLookAt(0,80,200, 0,0,0, 0,1,0)
    #   # gluLookAt(250, 250, 250, 250, 250, 250, 1, 1, 0)
    #   # gluLookAt(0, 500, 400, 0, 0, 0, 0, 1, 0)
    #   gluLookAt(0, 300, 500, 0, 150, 100, 0, 1, 0)
    #   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    desenhaVeneno()
    desenhaComidas()
    desenhaSuperComida()
    desenhaCobra()


    if not jogoIniciado:
        desenhaTexto("Pressione o botão direito para acessar", 5, 30)
        desenhaTexto("o menu e então iniciar o jogo", 12, 27)

    else:
        if envenenado:
            gameOver()
            desenhaTexto("Game Over - Você comeu a comida envenenada", 1, 30)
            desenhaTexto("Pontuação: " + str(pontuacao), 17, 25)
            desenhaTexto("Clique com botão direito para abrir menu", 5.5, 20)

        elif jogoEncerrado:
            gameOver()
            desenhaTexto("Game Over", 17, 30)
            desenhaTexto("Pontuação: " + str(pontuacao), 17, 25)
            desenhaTexto("Clique com botão direito para abrir menu", 5.5, 20)

    glFlush()

def criaMenu():
    # iluminacao()

    menu = glutCreateMenu(MenuPrincipal)
    glutAddMenuEntry("Iniciar Jogo", 0)
    glutAddMenuEntry("Reiniciar Jogo", 1)
    glutAddMenuEntry("Pausar/voltar ao jogo", 2)
    glutAddMenuEntry("Encerrar", 3)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def MenuPrincipal(acao):
    global pontuacao, jogoExecucao, jogoIniciado

    if acao == 0:
        if not jogoIniciado:
            pontuacao = 0
            jogoExecucao = True
            jogoIniciado = True
        else:
            reiniciarJogo()

    elif acao == 1:
        reiniciarJogo()
    elif acao == 2:
        jogoExecucao = not jogoExecucao
    elif acao == 3:
        os._exit(1)
    else:
        return 0

    if (jogoExecucao):
        movimenta(1)

    return 0

def desenhaTexto(string, x, y):
    glPushMatrix()
    glColor3f(1, 0, 0)
    glRasterPos2f(x, y)

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

    glPopMatrix()

def iluminacao():
    luzAmbiente = [0.2, 0.2, 0.2, 1]
    luzDifusa = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular = [0.5, 0.5, 0.5, 1];# "brilho"
    posicaoLuz = [0,0,1,0];
    luzAmbiente1 = [0.2, 0.2, 0.2, 1]
    luzDifusa1 = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular1 = [0.5, 0.5, 0.5, 1];# "brilho"
    posicaoLuz1 = [1,0,0,0];
    posicaoLuz2 = [0,1,0,0];
    posicaoLuz3 = [1,1,0,0];
    # Capacidade de brilho do material
    especularidade = [0.5, 0.5, 0.5, 0];
    especMaterial = 5;
    glClearColor(0.0, 0.0, 0.0, 1.0);
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH);
    #glShadeModel(GL_FLAT);
    # Define a refletância do material
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade);
    #// Define a concentração do brilho
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial);
    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente);
    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz);
    # Define os parâmetros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1);
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1);
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1);
    # Define os parâmetros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2);
    # Define os parâmetros da luz de número 3
    glLightfv(GL_LIGHT3, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT3, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT3, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT3, GL_POSITION, posicaoLuz3);

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);#Habilita o uso de iluminação
#    glEnable(GL_LIGHT0); # Habilita a luz de número 0
#    glEnable(GL_LIGHT1); # Habilita a luz de número 0
#    glEnable(GL_LIGHT2); # Habilita a luz de número 0
#    glEnable(GL_LIGHT3); # Habilita a luz de número 0
    glEnable(GL_DEPTH_TEST); # Habilita o depth-buffering
    glEnable(GL_NORMALIZE);

def parametrosVisualizacao():
    global angulo

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    # Especifica a projeção perspectiva
    gluPerspective(angulo, 1, 0.1, 600);
    #gluPerspective(angulo, 1, 0.5, 50);
    #glOrtho(-1.8, 1.8, -1.8, 2, 0.8, 200.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    # Especifica posição do observador e do alvo
    #gluLookAt(2.00 + anguloX, 1.00 + anguloY, 2.0, 0.0, 0.5, 0.25, 0.0, 1.0, 0.0);
    gluLookAt(0, 300, 500, 0, 150, 100, 0, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

def gerenciaMouse(button, state, x, y):
    global angulo

    print("zoom")
    print(angulo)

    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo < 170):
                angulo += 5
            else:
                angulo = 5

    parametrosVisualizacao()
    glutPostRedisplay()

def main():
    print("Jogo da Cobrinha")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(largura, altura)
    glutInitWindowPosition(600, 400)
    glutCreateWindow(b"Jogo da Cobrinha 2D")
    glutMouseFunc(gerenciaMouse)
    glutDisplayFunc(desenha)
    glutIdleFunc(desenha)
    glutKeyboardFunc(tecladoMovimentos)
    glutSpecialFunc(tecladoMovimentosTeclasEspeciais)
    criaMenu()
    glutMainLoop()

main()