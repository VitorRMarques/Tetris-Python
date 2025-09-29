#tetris.py
# Implementação simples de Tetris em Python usando pygame.
# Estruturas usadas:
# - Matriz (lista de listas) para grid de tabuleiro
# - dicionários para as peças (nome -> rotação)
# - listas para rotação e sequência
# set para posições travadas (ocupadas)
#
# Executar: python tetris.py

import pygame
import random
import sys

# -------------- CONFIGURAÇÕES ---------------
CELL_SIZE = 30                # tamanho do quadrado em pixels
COLUMNS = 10                  # largura do tabuleiro (tetris padrão)
ROWS = 20                     # altura do tabuleiro
WIDTH = CELL_SIZE * COLUMNS
HEIGHT = CELL_SIZE * ROWS
FPS = 60

# cores (R,G,B)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
# cores das peças
COLORS = [
    (0, 255, 255),      # I - ciano
    (0, 0, 255),        # J - azul
    (255, 165, 0),      # L - laranja
    (255, 255, 0),      # O - amarelo
    (0, 255, 0),        # S - verde
    (128, 0, 128),      # T - roxo
    (255, 0, 0),        # Z -vermelho
]

# ------------- DEFINIÇÃO DAS PEÇAS ------------------
# Cada peça tem uma lista de rotações; cada rotação é uma lista de strings 4x4
# '0' = vazio, 'X' = bloco
# Usamos 4x4 para simplificar rotação e alinhamento
SHAPES = {
    'I': [
        ["0000",
         "XXXX",
         "0000",
         "0000"],
        ["00X0",
         "00X0",
         "00X0",
         "00X0"]
    ],
    'J': [
        ["X00",
         "XXX",
         "000"],
        ["0XX",
         "0X0",
         "0X0"],
        ["000",
         "XXX",
         "00X"],
        ["0X0",
         "0X0",
         "XX0"]
    ],
    'L': [
        ["00X",
         "XXX",
         "000"],
        ["0X0",
         "0X0",
         "0XX"],
        ["000",
         "XXX",
         "X00"],
        ["XX0",
         "0X0",
         "0X0"]
    ],
    'O': [
        ["00",
         "00"],
    ],
    'S': [
        ["0XX",
         "XX0",
         "000"],
        ["0X0",
         "0XX",
         "00X"]
    ],
    'T': [
        ["0X0",
         "XXX",
         "000"],
        ["0X0",
         "0XX",
         "0X0"],
        ["000",
         "XXX",
         "0X0"],
        ["0X0",
         "XX0",
         "0X0"]
    ],
    'Z': [
        ["XX0",
         "0XX",
         "000"],
        ["00X",
         "00X",
         "0X0"]
    ]
}

# Para facilitar vamos transformar cada rotação em formado de lista de coordenadas (x, y)
# relativas ao topo-esquerdo de seu bounding box.
def shape_to_coords(shape_rot):
    """Converts a rotation (list of strings) to a list of (x, y) coordinate tuples."""
    coords = []
    rows = len(shape_rot)
    cols = len(shape_rot[0])
    for y in range(rows):
        for x in range(cols):
            if shape_rot[y][x] == 'X':
                coords.append((x, y))
    return coords, cols, rows # retornamos também largura/altura do bounding box

