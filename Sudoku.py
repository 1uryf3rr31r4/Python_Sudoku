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
window = pg.display.set_mode((950, 650))

# Inicializando fonte do Jogo
pg.font.init()

# Escolhendo uma fonte e tamanho
fonte = pg.font.SysFont('Courier New', 50, bold=True)

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

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()