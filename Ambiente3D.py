from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

global angulo, fAspect,anguloX,anguloY,NUMERO_LIVROS

anguloX=0; anguloY=0;randMax = 1;NUMERO_LIVROS = 16

class Livro:
    r=0.0;g=0.0; b=0.0; pX_Livro=0.0;

def chao():
    glColor3f(0.47, 0.79, 0.47);
    glPushMatrix();
    glTranslated(0.5, 0.2, 0.3);
    glScaled(2.0, 0.2, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeFundo():
    glColor3f(1.0, 0.72, 0.83);
    glPushMatrix();
    glTranslated(0.5, 1.10, -0.7);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(2.0, 0.03, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeFrente():
    glColor3f(1.0, 0.72, 0.83);
    glPushMatrix();
    glTranslated(-0.51, 1.10, 0.3);
    glRotated(90.0, 0.0, 1.0, 0.0);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(2.0, 0.03, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def estante():
    #Fundo
    glColor3f(0.50, 0.30, 0.10);
    glPushMatrix();
    glTranslated(0.5, 1.15, -0.7);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.7, 0.02, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
    #Lateral traseira
    glPushMatrix();
    glTranslated(-0.2, 1.15, -0.6);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.12, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
    #Lateral frontal
    glPushMatrix();
    glTranslated(1.2, 1.15, -0.6);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.12, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
    #Topo
    glPushMatrix();
    glTranslated(0.5, 1.95, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();
    #Meio
    glPushMatrix();
    glTranslated(0.5, 1.15, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();
    #Base
    glPushMatrix();
    glTranslated(0.5, 0.35, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();

def chaleira():
    glColor3f(0.96, 0.96, 0.96);
    glPushMatrix();
    glTranslated(-0.29, 0.89, 0.7);
    glRotated(-60, 0, 1, 0);
    glutSolidTeapot(0.07);
    glPopMatrix();

def livro(x, r, g, b):
    if (r == 0 and g == 0 and b == 0):
        g = 1.0;
    glColor3f(r, g, b);
    glPushMatrix();
    glTranslated(x, 1.47, -0.58);
    glScaled(0.15, 1.0, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

def quadro():
    x = -0.50; y = 1.50; z = 0.20;
    glPushMatrix();
    glColor3f(0.50, 0.30, 0.10);
    glTranslated(x,y,z);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03, 0.9, 0.9);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(1.0, 1.0, 0.0);
    glPushMatrix();
    glTranslated(x, y - 0.35, z + 0.13);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y + 0.32, z - 0.4);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y, z);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y + 0.2, z + 0.1);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y - 0.2, z - 0.1);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y - 0.24, z + 0.4);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(x, y + 0.24, z + 0.36);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.1, 0.15);
    glutSolidCube(1.0);
    glPopMatrix();

def mesa():
    glColor3f(0.50, 0.30, 0.10);
    #Tampa
    glPushMatrix();
    glTranslated(-0.29, 0.8, 0.7);
    glScaled(0.4, 0.05, 0.9);
    glutSolidCube(1.0);
    glPopMatrix();

    #Pé esquerdo fundo
    glPushMatrix();
    glTranslated(-0.43, 0.45, 0.95);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03, 0.03, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

    #Pé esquerdo frente
    glPushMatrix();
    glTranslated(-0.16, 0.45, 0.95);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03, 0.03, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

    #Pé direito fundo
    glPushMatrix();
    glTranslated(-0.43, 0.45, 0.45);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03, 0.03, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

    #Pé direito frente
    glPushMatrix();
    glTranslated(-0.16, 0.45, 0.45);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03, 0.03, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

def desenhaPrincipal():
    global anguloX, anguloY,livro
    glRotated(anguloX, 0.0, 1.0, 0.0);
    glRotated(anguloY, 1.0, 0.0, 0.0);
    chao();
    paredeFundo();
    paredeFrente();
    estante();
    quadro();
    mesa();
    chaleira();
    for i in range(NUMERO_LIVROS):
        livro(Livros[i].pX_Livro, Livros[i].r, Livros[i].g, Livros[i].b);
    glFlush();

def iluminacao():
    luzAmbiente = [0.2, 0.2, 0.2, 1]
    luzDifusa = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular = [0.5, 0.5, 0.5, 1];# "brilho"
    posicaoLuz = [1,1,1,1];#{ 50.0, 100.0, 20.0, 1.0 };
    # Capacidade de brilho do material
    especularidade = [0.4, 0.4, 0.4, 0.4];
    especMaterial = 50;
    glClearColor(0.0, 0.0, 0.0, 1.0);
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH);
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
    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);#Habilita o uso de iluminação
    glEnable(GL_LIGHT0); # Habilita a luz de número 0
    glEnable(GL_DEPTH_TEST); # Habilita o depth-buffering
    glEnable(GL_NORMALIZE);

def parametrosVisualizacao():
    global fAspect
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    # Especifica a projeção perspectiva
    gluPerspective(angulo, fAspect, 0.1, 500);
    #gluPerspective(angulo, 1, 0.5, 50);
    #glOrtho(-1.8, 1.8, -1.8, 2, 0.8, 200.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    # Especifica posição do observador e do alvo
    #gluLookAt(2.00 + anguloX, 1.00 + anguloY, 2.0, 0.0, 0.5, 0.25, 0.0, 1.0, 0.0);
    gluLookAt(5.0, 5.0, 5.0, 0, 1, 0, 0.0, 1.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

def moveCamera(key, x1, y1):
    global anguloX, anguloY
    if (key == GLUT_KEY_UP):
        anguloY -= 1;
    elif (key == GLUT_KEY_DOWN):
        anguloY += 1;
    elif (key == GLUT_KEY_LEFT):
        anguloX -= 1;
    elif (key == GLUT_KEY_RIGHT):
        anguloX += 1;

    parametrosVisualizacao();
    glutPostRedisplay();

def inicializa():
    global angulo,Livros
    Livros=[]
    iluminacao();
    angulo = 30;
    pX_Livro = -0.12;
    for i in range(NUMERO_LIVROS):
        temp= Livro()
        temp.r=random.random();temp.g=random.random();temp.b=random.random()
        temp.pX_Livro = pX_Livro;
        Livros.append(temp)
        pX_Livro += 0.078;

def alteraTamanhoJanela(w, h):
    global fAspect
    if (h == 0): h = 1; # Para previnir uma divisão por zero
    glViewport(0, 0, w, h);# Especifica o tamanho da viewport
    fAspect = w/h;
    parametrosVisualizacao();

def gerenciaMouse(button, state, x, y):
    global angulo
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo < 170):
                angulo+=5;
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo > 10):
                angulo-=5;
    #printf("%f\n",angulo);
    parametrosVisualizacao();
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(1024, 768);
    glutCreateWindow(b"Ambiente 3D");
    glutDisplayFunc(desenhaPrincipal);
    glutReshapeFunc(alteraTamanhoJanela);
    glutSpecialFunc(moveCamera);
    glutMouseFunc(gerenciaMouse);
    inicializa();
    glutMainLoop();

main()
