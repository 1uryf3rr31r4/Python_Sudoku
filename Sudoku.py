import pygame as pg
import pandas as pd
import random
import math

# Cores
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul_claro = (200, 200, 255)
azul = (100, 100, 255)
branco = (255, 255, 255)

# Tela do Jogo
window = pg.display.set_mode((975, 675))

# Inicializando fonte do Jogo
pg.font.init()

# Escolhendo uma fonte e tamanho
fonte = pg.font.SysFont('Courier New', 50, bold=True)


tabuleiro_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ]


jogo_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ]

escondendo_numeros = True
tabuleiro_preenchido = True
click_last_status = False
click_position_x = -1
click_position_y = -1
numero = 0

def Tabuleiro_Hover(window, mouse_position_x, mouse_position_y):
    quadrado = 66.7
    ajuste = 50
    x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)

    pg.draw.rect(window, branco, (0, 0, 975, 675))

    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul_claro, ((ajuste + x * quadrado,
                     ajuste + y * quadrado, quadrado, quadrado)))

def Celula_Selecionada(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    quadrado = 66.7
    ajuste = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_position_x - ajuste)/quadrado)-1)
        y = (math.ceil((mouse_position_y - ajuste)/quadrado)-1)

    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul, ((ajuste + x * quadrado,
                     ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)

    # Declerando Variaveis de Posição
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declerando Variavel do mouse
    click = pg.mouse.get_pressed()

    # Jogo
    Tabuleiro_Hover(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = Celula_Selecionada(
        window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()