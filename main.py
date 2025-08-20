# Ветка: cycle-code
# Реализован игровой цикл, обработка выхода и обновление экрана

import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра Тир")

# Фиксированный цвет фона (для демонстрации)
color = (135, 206, 235)  # Светло-голубой

# Переменная для управления циклом
running = True
while running:
    # Заливка фона
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()